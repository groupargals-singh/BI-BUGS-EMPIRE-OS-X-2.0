# BI-BUGS Location Reference Data

**Catalogue:** `BBE-LOCATION-REFERENCE-DATA-001`  
**Snapshot retrieved:** 2026-11-23 (UTC timestamp and SHA-256 checksums in `LOCATION_DATA_SOURCE_MANIFEST.json`).  
**Purpose:** reference datasets for a future searchable location selector. These files do not enable locations for BI-BUGS service delivery and do not prove service coverage.

## Files

| File | Contents | Record count / status |
|---|---|---:|
| `INDIA_LGD_STATES_DISTRICTS.json` | Government of India Local Government Directory States/UTs and district hierarchy, stable LGD codes and local-language district names | 36 States/UTs (28 States + 8 UTs), 770 districts |
| `UN_M49_COUNTRY_AREA_CATALOGUE.csv` | UN Statistics Division country-or-area names, M49 codes and ISO alpha-2/alpha-3 codes | 248 country/area entries; 247 International entries after India is separated into the domestic selector |
| `INDIA_POPULATED_PLACES.tsv.gz` | GeoNames India populated-place search index with GeoNames IDs, names, coordinates, feature codes, admin codes, and cautious LGD state/district crosswalk fields | 549,031 active populated-place records |
| `LOCATION_DATA_SOURCE_MANIFEST.json` | Sources, retrieval timestamp, record counts, source archive checksum, output checksums, license and use boundaries | One manifest |

## Sources and attribution

1. **Local Government Directory (LGD), Ministry of Panchayati Raj, Government of India:** [LGD portal](https://lgdirectory.gov.in/) and [OGD catalogue](https://www.data.gov.in/catalog/local-government-directory-lgd). The OGD catalogue displayed an update date of 22 November 2026 at research time. LGD is the source of the 36 State/UT and 770 district administrative hierarchy. Consult the Government Open Data License-India and the LGD/OGD source terms before redistribution or public display. Urban Local Bodies are a separate LGD entity type and are not claimed to have been imported in this snapshot.
2. **United Nations Statistics Division, M49:** [Country or Area Codes for Statistical Use](https://unstats.un.org/unsd/methodology/m49/overview/). This is a country-*or-area* statistical list, not a declaration of sovereignty. It includes territories and other areas; the file retains the UN's names and M49/ISO identifiers.
3. **GeoNames:** [India country extract](https://download.geonames.org/export/dump/IN.zip), [download and terms](https://www.geonames.org/export/), and [about/data model](https://www.geonames.org/about.html). The data is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Attribution: “GeoNames” with a link to https://www.geonames.org/. The source describes the data as-is, without warranty of accuracy, timeliness or completeness.

## Interpretation and limitations

- The GeoNames file is a **populated-place search index**, not a city-only register. It includes cities, towns, villages, localities and other populated-place feature types. The feature code is retained so the application can distinguish administrative seats from generic populated places; do not label every row a city.
- The index contains 549,031 active `PPL*` feature records. 548,995 have an LGD State/UT crosswalk; 429,615 have an LGD district crosswalk. Where a crosswalk is absent or names do not match confidently, the LGD code remains blank. Do not guess a parent district.
- GeoNames place coordinates are source data, not verified BI-BUGS branch pins, service locations, customer locations or route directions.
- LGD State/UT and district records are the authoritative India administrative hierarchy in this snapshot. The GeoNames index supplements them with broad place-name search. It is not a replacement for LGD urban local body lists or official municipal boundaries.
- The UN M49 file uses the label “Country or Area”; it does not decide sovereignty or BI-BUGS operations.
- Every imported location remains `INACTIVE` unless separately selected in `LOCATION_AREA_REGISTER.json`. Owner-selected active areas do not prove any pest-control service is available there.
- Service availability remains a per-service, per-area evidence and approval gate. No national or international operational coverage is asserted.
- No browser geolocation, customer exact-address collection, map pin, or website selector implementation is authorized by these reference files.

## Validation and refresh

Run from repository root:

```bash
python scripts/validate_location_catalogue.py --strict
```

To refresh the source snapshots and rebuild the files:

```bash
python scripts/import_location_reference_data.py
python scripts/validate_location_catalogue.py --strict
```

Refreshes are explicit repository changes. Review source updates, row-count changes, code changes, crosswalk drift and license/source notices before committing. Do not run an unattended import that silently changes public customer choices.
