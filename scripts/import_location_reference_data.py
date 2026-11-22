#!/usr/bin/env python3
"""Import public location reference data from LGD, UN M49 and GeoNames.

Read-only source requests; writes versioned data files under
 docs/MASTER_SPECIFICATION/data. Does not change owner-selected active areas.
"""
from __future__ import annotations
import csv, gzip, hashlib, io, json, re, time, urllib.parse, urllib.request, zipfile
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs' / 'MASTER_SPECIFICATION' / 'data'
UA = 'BI-BUGS-EMPIRE-OS-X-2.0 location catalogue importer/1.0 (reference-data research)'
LGD = 'https://lgdirectory.gov.in/'
UN_M49 = 'https://unstats.un.org/unsd/methodology/m49/overview/'
GEONAMES = 'https://download.geonames.org/export/dump/'
ACTIVE_PLACE_CODES = {'PPL','PPLA','PPLA2','PPLA3','PPLA4','PPLA5','PPLC','PPLG','PPLL','PPLS','PPLX'}

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.tables=[]; self.in_table=False; self.in_row=False; self.in_cell=False; self.rows=[]; self.row=[]; self.buf=''
    def handle_starttag(self, tag, attrs):
        if tag == 'table': self.in_table=True; self.rows=[]
        elif self.in_table and tag == 'tr': self.in_row=True; self.row=[]
        elif self.in_table and self.in_row and tag in ('td','th'): self.in_cell=True; self.buf=''
    def handle_data(self, data):
        if self.in_cell: self.buf += data
    def handle_endtag(self, tag):
        if tag in ('td','th') and self.in_cell: self.row.append(' '.join(self.buf.split())); self.in_cell=False
        elif tag == 'tr' and self.in_row: self.rows.append(self.row); self.in_row=False
        elif tag == 'table' and self.in_table: self.tables.append(self.rows); self.in_table=False

def fetch(url: str, opener=None, referer=None, timeout=90) -> bytes:
    headers={'User-Agent':UA}
    if referer: headers['Referer']=referer
    req=urllib.request.Request(url,headers=headers)
    return (opener.open(req,timeout=timeout) if opener else urllib.request.urlopen(req,timeout=timeout)).read()

def js_string(raw: str) -> str:
    return json.loads('"'+raw+'"')

def dwr_call(opener, page_path: str, service: str, method: str, params: list[str]) -> str:
    body={'callCount':'1','page':page_path,'httpSessionId':'','scriptSessionId':'','instanceId':'0',
          'c0-scriptName':service,'c0-methodName':method,'c0-id':'0','batchId':'0'}
    for i, value in enumerate(params): body[f'c0-param{i}']=value
    url=LGD+'dwr/call/plaincall/'+service+'.'+method+'.dwr'
    req=urllib.request.Request(url,data=urllib.parse.urlencode(body).encode(),headers={
        'User-Agent':UA,'Referer':LGD+page_path,'Content-Type':'application/x-www-form-urlencoded',
        'X-Requested-With':'XMLHttpRequest'})
    result=opener.open(req,timeout=45).read().decode('utf-8','replace')
    if 'handleBatchException' in result or '<html' in result[:500].lower():
        raise RuntimeError(f'LGD DWR call failed: {service}.{method}: {result[:350]}')
    return result

def import_lgd() -> dict:
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    home=fetch(LGD,opener).decode('utf-8','replace')
    match=re.search(r'href="([^"]*globalviewstateforcitizen\.do[^"]*)"',home)
    if not match: raise RuntimeError('LGD public States/UTs directory link not found')
    state_page_path='/globalviewstateforcitizen.do'
    state_html=fetch(urllib.parse.urljoin(LGD,match.group(1)),opener,LGD).decode('utf-8','replace')
    parser=TableParser(); parser.feed(state_html)
    state_rows=[]
    for table in parser.tables:
        if table and 'State LGD Code' in table[0]:
            header=table[0]; indexes={name:header.index(name) for name in ['State LGD Code','State Name (In English)','State or UT','Census2011 Code']}
            for row in table[1:]:
                if len(row)>max(indexes.values()) and row[indexes['State LGD Code']].isdigit():
                    state_rows.append({'lgd_state_code':int(row[indexes['State LGD Code']]),
                        'state_name':row[indexes['State Name (In English)']],
                        'state_or_ut':row[indexes['State or UT']],
                        'census2011_code':row[indexes['Census2011 Code']]})
            break
    if not state_rows: raise RuntimeError('No State/UT records parsed from LGD public directory')
    districts=[]
    for i,state in enumerate(state_rows,1):
        response=dwr_call(opener,state_page_path,'lgdDwrDistrictService','getDistrictList',[f"number:{state['lgd_state_code']}"])
        pattern=r'\{districtCode:(\d+),districtNameEnglish:"((?:\\.|[^"\\])*)",districtNameLocal:"((?:\\.|[^"\\])*)"'
        found=re.findall(pattern,response)
        if not found: raise RuntimeError(f"No district records returned for {state['state_name']} ({state['lgd_state_code']})")
        for code,name,local in found:
            districts.append({'lgd_district_code':int(code),'district_name':js_string(name),
                'district_name_local':js_string(local),'lgd_state_code':state['lgd_state_code'],
                'state_name':state['state_name'],'state_or_ut':state['state_or_ut']})
        time.sleep(0.12)
        print(f"LGD {i}/{len(state_rows)}: {state['state_name']} — {len(found)} districts")
    if len({x['lgd_state_code'] for x in state_rows}) != len(state_rows): raise RuntimeError('Duplicate LGD State/UT codes')
    if len({x['lgd_district_code'] for x in districts}) != len(districts): raise RuntimeError('Duplicate LGD district codes')
    payload={'dataset_id':'INDIA-LGD-ADMIN-001','source':'Ministry of Panchayati Raj — Local Government Directory (LGD)',
        'source_url':'https://lgdirectory.gov.in/','catalogue_url':'https://www.data.gov.in/catalog/local-government-directory-lgd',
        'retrieved_utc':datetime.now(timezone.utc).isoformat(),'state_ut_count':len(state_rows),
        'district_count':len(districts),'state_uts':state_rows,'districts':districts,
        'limitations':'Official LGD administrative records for States/UTs and districts. This is not a complete city/town list; use the separately sourced GeoNames populated-place index for locality search.'}
    path=OUT/'INDIA_LGD_STATES_DISTRICTS.json'; path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {'path':str(path.relative_to(ROOT)),'state_ut_count':len(state_rows),'state_count':sum(x['state_or_ut'].lower()=='state' for x in state_rows),
            'ut_count':sum(x['state_or_ut'].lower()=='ut' for x in state_rows),'district_count':len(districts),'states':state_rows,'districts':districts}

def import_un_m49() -> dict:
    html=fetch(UN_M49).decode('utf-8','replace'); parser=TableParser();parser.feed(html)
    rows=next((t for t in parser.tables if t and 'M49 Code' in t[0] and 'ISO-alpha2 Code' in t[0]),None)
    if not rows: raise RuntimeError('UN M49 English table not found')
    headers=rows[0]; idx={x:headers.index(x) for x in ['Country or Area','M49 Code','ISO-alpha2 Code','ISO-alpha3 Code','Region Name','Sub-region Name']}
    records=[]
    for row in rows[1:]:
        if len(row)<=max(idx.values()): continue
        name=row[idx['Country or Area']]; m49=row[idx['M49 Code']]; a2=row[idx['ISO-alpha2 Code']]; a3=row[idx['ISO-alpha3 Code']]
        if not (name and m49.isdigit() and a2 and a3): continue
        records.append({'country_or_area':name,'m49_code':m49,'iso_alpha2':a2,'iso_alpha3':a3,
            'region':row[idx['Region Name']],'subregion':row[idx['Sub-region Name']],
            'selector_group':'DOMESTIC_INDIA' if a2=='IN' else 'INTERNATIONAL',
            'selection_status':'DOMESTIC' if a2=='IN' else 'INACTIVE_OWNER_NOT_SELECTED'})
    if len(records)<240 or len({x['m49_code'] for x in records})!=len(records): raise RuntimeError('UN M49 country/area catalogue integrity check failed')
    path=OUT/'UN_M49_COUNTRY_AREA_CATALOGUE.csv'
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
    return {'path':str(path.relative_to(ROOT)),'count':len(records),'international_count':sum(x['selector_group']=='INTERNATIONAL' for x in records)}

def import_geonames(lgd: dict) -> dict:
    archive=fetch(GEONAMES+'IN.zip',timeout=180)
    archive_sha=hashlib.sha256(archive).hexdigest()
    z=zipfile.ZipFile(io.BytesIO(archive)); member=next((x for x in z.namelist() if x.endswith('/IN.txt') or x=='IN.txt'),None)
    if not member: raise RuntimeError('GeoNames IN.txt missing from India archive')
    admin1_raw=fetch(GEONAMES+'admin1CodesASCII.txt').decode('utf-8','replace').splitlines()
    admin2_raw=fetch(GEONAMES+'admin2Codes.txt').decode('utf-8','replace').splitlines()
    admin1={}; admin2={}
    for line in admin1_raw:
        p=line.split('\t')
        if len(p)>=4 and p[0].startswith('IN.'):
            admin1[p[0].split('.',1)[1]]={'name':p[1],'ascii_name':p[2],'geoname_id':p[3]}
    for line in admin2_raw:
        p=line.split('\t')
        if len(p)>=4 and p[0].startswith('IN.'):
            admin2[p[0]]={'full_code':p[0],'name':p[1],'ascii_name':p[2],'geoname_id':p[3]}
    states_by_name={}
    for state_record in lgd['states']:
        states_by_name[re.sub(r'[^a-z0-9]','',state_record['state_name'].casefold().removeprefix('the '))]=state_record
    states_by_alias={'andamanandnicobar':'andamanandnicobarislands'}
    districts_by_name={}
    def norm(x): return re.sub(r'[^a-z0-9]','',x.casefold())
    for d in lgd['districts']: districts_by_name[(d['lgd_state_code'],norm(d['district_name']))]=d
    path=OUT/'INDIA_POPULATED_PLACES.tsv.gz'
    count=0; state_mapped=0; district_mapped=0; codes={};
    fields=['geoname_id','name','ascii_name','latitude','longitude','feature_code','admin1_code','admin1_name','lgd_state_code','admin2_code','admin2_name','lgd_district_code','population','modification_date']
    with z.open(member) as src, gzip.open(path,'wt',encoding='utf-8',newline='',compresslevel=6) as out:
        writer=csv.DictWriter(out,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader()
        for raw in src:
            p=raw.decode('utf-8').rstrip('\n').split('\t')
            if len(p)<19 or p[6]!='P' or p[7] not in ACTIVE_PLACE_CODES: continue
            a1=p[10]; a2=p[11]; a1rec=admin1.get(a1,{}); a2rec=admin2.get(a1+'.'+a2,{})
            state_name_key=norm(a1rec.get('name','').removeprefix('The '))
            state_name_key=states_by_alias.get(state_name_key,state_name_key)
            state=states_by_name.get(state_name_key)
            if state: state_mapped+=1
            district=None
            a2rec=admin2.get(f'IN.{a1}.{a2}',{}) if a1 and a2 else {}
            if state and a2rec:
                district=districts_by_name.get((state['lgd_state_code'],norm(a2rec.get('ascii_name') or a2rec.get('name',''))))
            if district: district_mapped+=1
            writer.writerow({'geoname_id':p[0],'name':p[1],'ascii_name':p[2],'latitude':p[4],'longitude':p[5],
                'feature_code':p[7],'admin1_code':a1,'admin1_name':a1rec.get('name',''),'lgd_state_code':state['lgd_state_code'] if state else '',
                'admin2_code':a2,'admin2_name':a2rec.get('name',''),'lgd_district_code':district['lgd_district_code'] if district else '',
                'population':p[14],'modification_date':p[18]})
            count+=1;codes[p[7]]=codes.get(p[7],0)+1
    if count<100000: raise RuntimeError(f'GeoNames place index unexpectedly small: {count}')
    return {'path':str(path.relative_to(ROOT)),'record_count':count,'state_mapped_records':state_mapped,
        'district_mapped_records':district_mapped,'feature_code_counts':codes,'source_archive_bytes':len(archive),
        'source_archive_sha256':archive_sha,'license':'Creative Commons Attribution 4.0 International',
        'source_url':GEONAMES+'IN.zip'}

def main() -> None:
    OUT.mkdir(parents=True,exist_ok=True)
    retrieved=datetime.now(timezone.utc).isoformat()
    print('Importing official LGD States/UTs and district records...')
    lgd=import_lgd()
    print('Importing UN M49 country/area catalogue...')
    un=import_un_m49()
    print('Importing GeoNames India populated-place search index...')
    geo=import_geonames(lgd)
    for record in (lgd,un,geo):
        file_path=ROOT/record['path']
        record['output_bytes']=file_path.stat().st_size
        record['output_sha256']=hashlib.sha256(file_path.read_bytes()).hexdigest()
    manifest={'catalogue_id':'BBE-LOCATION-REFERENCE-DATA-001','retrieved_utc':retrieved,
      'purpose':'Reference data for a searchable location selector. Not proof of BI-BUGS operational coverage.',
      'datasets':{'india_lgd':{k:v for k,v in lgd.items() if k not in ('states','districts')},'un_m49':un,'india_populated_places':geo},
      'sources':[{'name':'Local Government Directory (LGD)','publisher':'Ministry of Panchayati Raj, Government of India','url':'https://lgdirectory.gov.in/','catalogue_url':'https://www.data.gov.in/catalog/local-government-directory-lgd','license':'Government Open Data License-India applies to published OGD resources; LGD portal terms/source attribution must be checked before redistribution','role':'Official State/UT and district administrative records; urban local bodies are separate records and are not conflated with city/locality list.'},
        {'name':'UN Statistics Division M49','publisher':'United Nations Statistics Division','url':UN_M49,'role':'Country or area names, M49 and ISO alpha codes. UN list includes areas/territories and is not a sovereignty classification.'},
        {'name':'GeoNames India extract','publisher':'GeoNames','url':GEONAMES+'IN.zip','license':'CC BY 4.0','role':'Searchable populated-place/locality index; includes villages and other populated-place types, not a government city boundary or service-coverage source.'}],
      'critical_boundaries':['All locations default inactive unless separately owner-selected.','Owner-selected active areas are not proof of service availability.','GeoNames populated places are search candidates; they must not be represented as official municipal city limits.','UN M49 Country or Area is a statistical list and does not determine sovereignty.','No browser geolocation, customer exact-address collection, or service coverage is enabled by this import.']}
    mpath=OUT/'LOCATION_DATA_SOURCE_MANIFEST.json';mpath.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'LGD':{k:v for k,v in lgd.items() if k not in ('states','districts')},'UN_M49':un,'GeoNames':geo,'manifest':str(mpath.relative_to(ROOT))},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
