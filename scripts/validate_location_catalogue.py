#!/usr/bin/env python3
"""Strict integrity checks for imported BI-BUGS location reference datasets."""
from __future__ import annotations
import argparse, csv, gzip, hashlib, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'docs'/'MASTER_SPECIFICATION'/'data'
ACTIVE_PLACE_CODES={'PPL','PPLA','PPLA2','PPLA3','PPLA4','PPLA5','PPLC','PPLG','PPLL','PPLS','PPLX'}

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()

def validate(data_dir:Path=DATA)->tuple[list[str],dict]:
    errors=[];metrics={}
    try:
        lgd=json.loads((data_dir/'INDIA_LGD_STATES_DISTRICTS.json').read_text(encoding='utf-8'))
        manifest=json.loads((data_dir/'LOCATION_DATA_SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
    except Exception as exc:
        return [f'Cannot read LGD/manifest JSON: {exc}'],metrics
    states=lgd.get('state_uts',[]); districts=lgd.get('districts',[])
    state_codes={x.get('lgd_state_code') for x in states}
    district_codes={x.get('lgd_district_code') for x in districts}
    if len(states)!=36:errors.append(f'Expected 36 States/UTs; found {len(states)}')
    if sum(x.get('state_or_ut','').lower()=='state' for x in states)!=28:errors.append('Expected 28 States')
    if sum(x.get('state_or_ut','').lower()=='ut' for x in states)!=8:errors.append('Expected 8 Union Territories')
    if len(state_codes)!=len(states):errors.append('Duplicate LGD State/UT code')
    if len(districts)!=770:errors.append(f'Expected 770 LGD districts in imported snapshot; found {len(districts)}')
    if len(district_codes)!=len(districts):errors.append('Duplicate LGD district code')
    if any(x.get('lgd_state_code') not in state_codes for x in districts):errors.append('District references unknown LGD State/UT code')
    metrics.update({'state_ut_count':len(states),'state_count':sum(x.get('state_or_ut','').lower()=='state' for x in states),
                    'ut_count':sum(x.get('state_or_ut','').lower()=='ut' for x in states),'district_count':len(districts)})
    country_path=data_dir/'UN_M49_COUNTRY_AREA_CATALOGUE.csv'
    try:
        with country_path.open(encoding='utf-8',newline='') as f: countries=list(csv.DictReader(f))
    except Exception as exc:
        errors.append(f'Cannot read UN M49 CSV: {exc}');countries=[]
    if len(countries)!=248:errors.append(f'Expected 248 UN M49 country/area entries; found {len(countries)}')
    for field in ('m49_code','iso_alpha2','iso_alpha3'):
        values=[x.get(field) for x in countries]
        if len(values)!=len(set(values)):errors.append(f'Duplicate UN M49 {field}')
    india=[x for x in countries if x.get('iso_alpha2')=='IN']
    if len(india)!=1 or india[0].get('selector_group')!='DOMESTIC_INDIA':errors.append('India must be the single domestic entry, not an International selector entry')
    international=[x for x in countries if x.get('selector_group')=='INTERNATIONAL']
    if len(international)!=247:errors.append(f'Expected 247 International country/area entries; found {len(international)}')
    if any(x.get('selection_status')!='INACTIVE_OWNER_NOT_SELECTED' for x in international):errors.append('International entries must remain inactive until owner selection')
    metrics.update({'un_m49_country_area_count':len(countries),'international_country_area_count':len(international)})
    place_path=data_dir/'INDIA_POPULATED_PLACES.tsv.gz'
    place_count=state_mapped=district_mapped=0;seen=set();bad_state=bad_district=0
    try:
        district_parent={str(x['lgd_district_code']):x['lgd_state_code'] for x in districts}
        with gzip.open(place_path,'rt',encoding='utf-8',newline='') as f:
            reader=csv.DictReader(f,delimiter='\t')
            required={'geoname_id','name','ascii_name','feature_code','lgd_state_code','lgd_district_code','population'}
            if not required.issubset(set(reader.fieldnames or [])):errors.append('Populated-place TSV is missing required columns')
            for row in reader:
                place_count+=1;gid=row.get('geoname_id','')
                if not gid or gid in seen:errors.append(f'Duplicate/missing GeoNames ID at row {place_count}');break
                seen.add(gid)
                if row.get('feature_code') not in ACTIVE_PLACE_CODES:errors.append(f'Unexpected GeoNames feature code {row.get("feature_code")}');break
                sc=row.get('lgd_state_code','');dc=row.get('lgd_district_code','')
                if sc:
                    if sc not in {str(x) for x in state_codes}:bad_state+=1
                    else:state_mapped+=1
                if dc:
                    if dc not in district_parent:bad_district+=1
                    elif not sc or district_parent[dc]!=int(sc):errors.append(f'GeoNames district/state crosswalk mismatch at place ID {gid}');break
                    else:district_mapped+=1
                if not row.get('name'):errors.append(f'Missing place name at row {place_count}');break
    except Exception as exc:
        errors.append(f'Cannot read populated-place gzip TSV: {exc}')
    if place_count<100000:errors.append(f'Populated-place index unexpectedly small: {place_count}')
    if bad_state:errors.append(f'{bad_state} populated-place records reference unknown LGD state codes')
    if bad_district:errors.append(f'{bad_district} populated-place records reference unknown LGD district codes')
    geo_summary=manifest.get('datasets',{}).get('india_populated_places',{})
    if geo_summary.get('record_count')!=place_count:errors.append('Manifest populated-place record count does not match TSV rows')
    if geo_summary.get('state_mapped_records')!=state_mapped:errors.append('Manifest state crosswalk count does not match TSV rows')
    if geo_summary.get('district_mapped_records')!=district_mapped:errors.append('Manifest district crosswalk count does not match TSV rows')
    metrics.update({'populated_place_count':place_count,'state_mapped_place_count':state_mapped,
                    'district_mapped_place_count':district_mapped,'unmapped_state_place_count':place_count-state_mapped,
                    'unmapped_district_place_count':place_count-district_mapped})
    if not manifest.get('retrieved_utc'):errors.append('Missing reference-data retrieval timestamp')
    for key in ('india_lgd','un_m49','india_populated_places'):
        record=manifest.get('datasets',{}).get(key,{})
        source_path=Path(record.get('path','')).name
        actual_path=data_dir/source_path
        if not actual_path.is_file():
            errors.append(f'Missing dataset file for {key}: {source_path}')
            continue
        if record.get('output_bytes')!=actual_path.stat().st_size:errors.append(f'{key} output byte count does not match manifest')
        if record.get('output_sha256')!=sha256(actual_path):errors.append(f'{key} SHA-256 does not match manifest')
    if not any(x in geo_summary.get('license','') for x in ('CC BY 4.0','Creative Commons Attribution 4.0')):errors.append('GeoNames CC BY 4.0 attribution/license missing from manifest')
    if manifest.get('critical_boundaries') is None:errors.append('Missing dataset use/coverage boundary controls')
    return errors,metrics

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--strict',action='store_true');ap.add_argument('--data-dir',type=Path,default=DATA);args=ap.parse_args()
    errors,metrics=validate(args.data_dir)
    print('Location reference catalogue:', 'PASS' if not errors else 'FAIL')
    for k,v in metrics.items():print(f'{k}: {v}')
    print('Scope: official LGD State/UT and district hierarchy + UN M49 country/area list + GeoNames populated-place search index; not a service-coverage approval or official city-boundary dataset.')
    for e in errors:print('ERROR:',e)
    return 1 if args.strict and errors else 0
if __name__=='__main__':sys.exit(main())
