# BI-BUGS EMPIRE OS-X 2.0
# MASTER SPECIFICATION — 35
# LOCATION CATALOGUE AND COVERAGE GOVERNANCE

**Specification ID:** BBEOSX-MS-35
**Specification status:** DRAFT FOR REVIEW — OWNER SELECTIONS CAPTURED; DATASET AND IMPLEMENTATION GATES OPEN
**Implementation status:** PARTIAL — OWNER-AREA REGISTER AND READ-ONLY VALIDATOR CREATED; WEBSITE SELECTOR NOT IMPLEMENTED
**Testing status:** UNIT TESTS EXECUTED — SEE PROJECT PROGRESS
**Production status:** NOT RELEASED — NO LIVE LOCATION SELECTOR OR SERVICE COVERAGE CLAIM
**Authority:** `00_MASTER_INDEX.md` and `02_ENGINEERING_CONSTITUTION.md`
**Related:** `31_WEBSITE_REQUIREMENTS.md`, `32_WEBSITE_DISCOVERY_WORKBOOK.md`, `15_SECURITY.md`, `18_TESTING.md`, `29_RELEASE_PROCESS.md`, `LOCATION_AREA_REGISTER.json`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose and scope

Define the controlled location model for the BI-BUGS website. It separates (a) the geographic choices a visitor may select, (b) areas the owner has selected as active in the website's area register, and (c) locations where a particular pest-control service has independently verified operational coverage. These are three different states and must never be conflated.

This is a BI-BUGS pest-control website requirement, not a generic geography product or a claim of nationwide/international operations.

## 2. Selector scope

- India selector: all Indian States and Union Territories and their cities, searchable/selectable through a hierarchical State/UT → district → city experience where authoritative data supports those levels.
- International / World: a separate option and country selector; do not mix country choices into the Indian State/UT list.
- All geographic locations outside the current owner-selected active list remain selectable/searchable but default to `INACTIVE` for BI-BUGS area-selection purposes.
- The current owner-selected district list is held in `LOCATION_AREA_REGISTER.json`; do not copy it into independent competing lists.
- The selector dataset must use stable geographic identifiers, parent identifiers, official display names, source, source version/effective date, and a documented update process. Do not invent missing districts, cities, boundaries, or IDs.
### 2.1 Imported reference-data snapshot — 2026-11-23

The versioned reference datasets are stored under `data/` and described in `data/README.md` and `data/LOCATION_DATA_SOURCE_MANIFEST.json`:

- **India administrative hierarchy:** the Government of India Local Government Directory (LGD) snapshot contains 36 States/UTs (28 States + 8 UTs) and 770 districts, with LGD codes and district local-language names. This is the primary administrative hierarchy.
- **International selector:** UN Statistics Division M49 provides 248 country-or-area entries; 247 are in the International selector after India is separated into the domestic selector. The UN list includes territories/areas and is not a sovereignty classification.
- **City/town/locality search:** GeoNames India extract provides 549,031 active populated-place records, including cities, towns, villages, localities and other populated-place types. It is a broad search index, not a city-only official municipal register. 548,995 records have an LGD State/UT crosswalk and 429,615 have a district crosswalk; unmatched crosswalk fields remain blank rather than guessed.
- **Still open:** LGD Urban Local Body (ULB) records / official municipal-city cross-check have not been imported in this snapshot. The GeoNames index does not certify official municipal boundaries or exhaustive BI-BUGS city coverage. Owner approval of final labels/selector behavior also remains open.

Source attribution, licensing notes, source limits, retrieval timestamp and SHA-256 checksums are in the manifest and data README. The importer and strict validator are reproducible from the repository root.

## 3. Owner-selected active areas — current register

The owner-selected set currently contains **25 districts**:

- Madhya Pradesh: all districts in selected divisions Chambal (3), Gwalior (5), Bhopal (5), and Indore (8): **21 districts**.
- Rajasthan: Jaipur, Jaisalmer, Dholpur: **3 districts**.
- Uttar Pradesh: Agra: **1 district**.

The canonical list and IDs are in `LOCATION_AREA_REGISTER.json`. This is an owner-area selection only. All remaining Indian and international locations remain inactive until the owner explicitly changes the register.

## 4. Three-state separation

| Layer | Meaning | Example status | May assert service available? |
|---|---|---|---|
| Selector catalogue | A place can be found/selected | `SELECTABLE` | No |
| Owner area selection | Owner selected the place as an active area in the website | `ACTIVE_OWNER_SELECTED` / `INACTIVE` | No |
| Per-service coverage | A named service has verified capability and coverage there | `CONFIRMED` only after evidence and approvals | Only after every publication gate passes |

A selected district must not automatically activate all 71 candidate catalogue services. Per-service coverage requires evidence, compliance/safety review, owner service approval, and public-content approval. Until then, service availability is `UNVERIFIED` and public claims are blocked.

## 5. Data provenance and change control

- Use authoritative government administrative-boundary sources for India and reputable maintained country datasets for international country lists.
- Store source name, source URL, retrieval date, dataset version/effective date, license/usage constraints, and checksum for each imported dataset.
- Preserve stable source codes where available; do not use translated display names as primary keys.
- Record administrative reorganizations as versioned changes; do not silently remap historic enquiries or owner-selected areas.
- Owner activation/deactivation requires an attributable owner instruction and a reviewed register change.
- Do not enable browser geolocation or collect a customer's exact address merely because a geographic selector exists; OI-04/OI-05 and privacy/security approval remain required.

## 6. Validation tooling

Run both owner-area and imported-reference-data validators:

```bash
python scripts/validate_location_register.py --strict
python scripts/validate_location_catalogue.py --strict
```

To explicitly refresh source snapshots, then validate:

```bash
python scripts/import_location_reference_data.py
python scripts/validate_location_catalogue.py --strict
```

Refresh is a reviewed repository change, not an unattended production sync.

The validator checks the 4 selected Madhya Pradesh divisions, their 21 districts, the 4 additional selected districts, unique IDs, the 25-district total, separate India/International selector scope, inactive-by-default behavior, and the prohibition on treating active-area selection as service availability. It does not validate the completeness of the all-India/world catalogue, geocode addresses, prove operational coverage, or implement a website selector.

## 7. Acceptance criteria

- [x] Current owner-selected divisions and districts represented in one canonical machine-readable register.
- [x] India and International selector scopes represented separately.
- [x] Unselected locations default inactive while remaining selectable.
- [x] Active-area selection separated from per-service availability.
- [x] Read-only validator and unit tests cover missing/duplicate areas and unsafe status conflation.
- [x] Official India States/UTs and district hierarchy imported from LGD (36 States/UTs, 770 districts), versioned and strictly validated.
- [x] International UN M49 country-or-area catalogue imported (248 total; 247 International after India is separated), with M49 and ISO identifiers.
- [x] Broad India populated-place search index imported from GeoNames (549,031 active records) with CC BY 4.0 attribution and explicit limitations; this is not a city-only official list.
- [ ] LGD Urban Local Body catalogue / official municipal-city cross-check imported and reconciled against the broad populated-place index.
- [ ] All unmatched place-to-district crosswalks reviewed where the application requires a district parent; do not infer missing mappings.
- [ ] Owner approves final location labels and selector behavior.
- [ ] Approved service-by-district coverage records exist before public availability claims.
- [ ] Frontend selector is implemented and tested only after Documentation Phase acceptance.

## 8. Current lifecycle boundary

The owner-area register, imported reference datasets and validators are documentation/data artifacts. They are not a live selector, geocoder, map, branch locator, routing service, or proof that BI-BUGS provides any specific service in the selected districts. GeoNames is an as-is broad place-name index and must not be represented as official city boundaries. Documentation Phase 1 remains active; no frontend coding is authorized until its acceptance gate is satisfied.


## 9. Official LGD Urban Local Body source follow-up — 2026-11-23

The official Open Government Data Platform India exposes the Ministry of Panchayati Raj resource “Local Government Directory (LGD) — Local Bodies” at:

- https://data.gov.in/resource/local-government-directory-lgd-local-bodies
- LGD catalogue: https://data.gov.in/catalog/local-government-directory-lgd
- Ministry of Panchayati Raj LGD overview: https://panchayat.gov.in/lgd/

The OGD resource metadata describes a monthly updated local-body dataset, last shown as updated 16 November 2026 during this review, and exposes state selection before preview/download. The Ministry's LGD overview explicitly includes urban local governments such as municipalities, corporations, notified areas and cantonment boards, alongside rural local bodies.

**Acquisition result:** Source discovery is complete, but no verified ULB export file has yet been retrieved/imported into this repository. The publicly visible OGD metadata lists state/local-body codes but does not, in the retrieved metadata alone, establish a complete verified schema for local-body names, type, district parent, effective dates and status. Therefore no count, completeness claim, city-to-ULB crosswalk or ULB dataset checksum is asserted here. Do not substitute third-party mirrors or bypass CAPTCHA/access controls. The next valid acquisition step is an official state-filtered OGD/LGD export or an officially documented open API with terms and complete schema; validate the raw export and reconcile it against GeoNames before import.

This closes the source-discovery subtask only. The official ULB data import/reconciliation, unresolved place-to-district mapping review and owner selector approval remain open.
