# BI-BUGS EMPIRE OS-X 2.0
# MASTER SPECIFICATION — 32
# WEBSITE DISCOVERY AND OWNER INPUT WORKBOOK

**Specification ID:** BBEOSX-MS-32
**Specification status:** DRAFT — OWNER INPUT IN PROGRESS; SOURCE DECISION RESOLVED
**Implementation status:** PARTIAL — static frontend foundation exists; customer/business workflows are not implemented
**Testing status:** SOURCE-GATE STRICT VALIDATION PASS; frontend/project-control test evidence recorded in `99_PROJECT_PROGRESS.md`
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related:** `31_WEBSITE_REQUIREMENTS.md`, `17_UI_UX_SYSTEM.md`, `20_FEATURE_REGISTRY.md`, `21_MODULE_REGISTRY.md`, `22_API_REGISTRY.md`, `23_DATABASE_REGISTRY.md`, `30_ROADMAP_20_YEARS.md`, `99_PROJECT_PROGRESS.md`
**Controlling decisions:** `DEC-BBE-001`, `DEC-BBE-002`

---

## 1. Purpose and use

This workbook converts the unknowns in Specification 31 into a traceable owner-review checklist. It is a capture aid, not an approval of any proposed feature or business fact.

For every item, record one of:
- `UNKNOWN` — no reliable information supplied.
- `OWNER_INPUT_RECEIVED` — information supplied but not yet verified/reviewed.
- `APPROVED` — explicitly accepted by the BI-BUGS project owner.
- `SOURCE_CONFIRMED — DISPLAY APPROVAL PENDING` — a company identity fact is supported by the canonical project record, but its exact public-facing presentation is not yet owner-approved.
- `DEFERRED` — intentionally excluded from the first release.
- `NOT_APPLICABLE` — owner confirms it does not apply.

Do not fill blank values with guesses. Keep evidence/source and approval date beside every accepted business fact. Do not put passwords, API keys, payment secrets, or other credentials in this workbook or Git.

## 2. First blocking decision — existing website or new build

| Field | Current value | Required evidence/action |
|---|---|---|
| Official website URL | NO OFFICIAL WEBSITE — OWNER CONFIRMED | Owner explicitly directed a new official website build from scratch; no existing official site is to be used as the source. |
| Website ownership | NOT APPLICABLE — NO OFFICIAL WEBSITE | No existing official website/domain is being claimed or migrated. |
| Delivery path | OWNER APPROVED — NEW_WEBSITE_BUILD | New BI-BUGS official website build from scratch. |
| Existing hosting/CMS/source access | NOT APPLICABLE — NEW_BUILD | Hosting/CMS selection remains a separate open decision. |
| Current website status | NO OFFICIAL WEBSITE — OWNER CONFIRMED | Recorded from the owner's explicit decision; no external domain ownership is inferred. |
| Owner decision evidence | Project owner (user confirmation in ChatGPT conversation); 2026-11-17; explicit instruction: “BI-BUGS के लिए नई official website शुरू से बनानी है।” | Non-secret owner decision evidence; no credentials recorded. |

**Gate WDG-01:** The existing-site versus new-build decision is resolved as NEW WEBSITE BUILD. Do not register/connect a domain, change DNS, select paid hosting, or publish to production until the domain, provider, ownership, budget, and release authority are separately approved.

For automated validation, use exactly one of these owner-controlled decision patterns:
- Existing site: `Official website URL` is the exact `https://` URL; `Website ownership` is `OWNER VERIFIED`; `Delivery path` is one of `OWNER APPROVED — EXISTING_SITE_AUDIT`, `OWNER APPROVED — MIGRATION`, or `OWNER APPROVED — REDESIGN`.
- New site: `Official website URL` is `NO OFFICIAL WEBSITE — OWNER CONFIRMED`; `Website ownership` is `NOT APPLICABLE — NO OFFICIAL WEBSITE`; `Delivery path` is `OWNER APPROVED — NEW_WEBSITE_BUILD`.
- `Owner decision evidence` must identify the approver, date, and non-secret evidence/reference. Do not enter credentials.

Run `python scripts/validate_website_source_gate.py` for a status report or add `--strict` to make an unresolved source decision fail a gate check. A PASS resolves only the source decision; it does not approve the full sitemap, content, customer journey, privacy, security, acceptance tests, or production release.

## 3. Company identity and brand

| Input | Owner value | Status | Evidence / notes |
|---|---|---|---|
| Exact legal/business identity on project record | BI-BUGS Pest Control Services Pvt Ltd | SOURCE_CONFIRMED — DISPLAY APPROVAL PENDING | Matches confirmed project identity WREQ-C-001 in `31_WEBSITE_REQUIREMENTS.md`; owner must still confirm exact public display wording before publication. |
| Approved logo file/source |  | UNKNOWN |  |
| Brand colours |  | UNKNOWN |  |
| Typography/font preference |  | UNKNOWN |  |
| Approved photos/videos |  | UNKNOWN |  |
| Brand/design reference sites |  | UNKNOWN |  |
| Languages required (e.g. English/Hindi) |  | UNKNOWN |  |
| Tone and writing style |  | UNKNOWN |  |

Do not create or publish an unapproved logo, certification, testimonial, guarantee, or brand claim.

## 4. Comprehensive pest-control service catalogue — owner-directed candidate scope

**Owner direction received 2026-11-21:** “Jo jo pest control service hoti h sab dalo isme” — include the broad range of pest-control services in the BI-BUGS website catalogue. The catalogue below is the comprehensive planning taxonomy requested by the owner. It is **not** evidence that BI-BUGS currently performs every listed treatment, holds every required licence, or approves every public claim. Each service remains `CANDIDATE — PROVIDER CAPABILITY / OWNER PUBLICATION CHECK REQUIRED` until BI-BUGS confirms availability, delivery method, geographic coverage, safety controls, and publishable wording. Do not show an unverified candidate as an active bookable service.

### 4.1 Residential and general pest management

| Catalogue ID | Candidate service | Pest / scope | Publication status |
|---|---|---|---|
| WDS-001 | General Pest Control | General household pest inspection and control | CANDIDATE — VERIFY |
| WDS-002 | Cockroach Control | Cockroaches | CANDIDATE — VERIFY |
| WDS-003 | Ant Control | Ants and ant colonies | CANDIDATE — VERIFY |
| WDS-004 | Bed Bug Control | Bed bugs | CANDIDATE — VERIFY |
| WDS-005 | Rat and Mouse Control | Rats and mice | CANDIDATE — VERIFY |
| WDS-006 | Mosquito Control | Mosquitoes and breeding-site management | CANDIDATE — VERIFY |
| WDS-007 | Housefly and Other Fly Control | Houseflies and nuisance flies | CANDIDATE — VERIFY |
| WDS-008 | Lizard Management | Lizards/geckos; humane exclusion where lawful | CANDIDATE — VERIFY |
| WDS-009 | Spider Control | Common nuisance spiders | CANDIDATE — VERIFY |
| WDS-010 | Silverfish Control | Silverfish | CANDIDATE — VERIFY |
| WDS-011 | Flea Control | Fleas | CANDIDATE — VERIFY |
| WDS-012 | Tick Control | Ticks | CANDIDATE — VERIFY |
| WDS-013 | Moth Control | Clothes and pantry moths | CANDIDATE — VERIFY |
| WDS-014 | Carpet Beetle Control | Carpet beetles and fabric pests | CANDIDATE — VERIFY |
| WDS-015 | Centipede and Millipede Management | Occasional crawling pests | CANDIDATE — VERIFY |
| WDS-016 | Silverfish and Booklice Management | Moisture-associated nuisance pests | CANDIDATE — VERIFY |
| WDS-017 | Wasp Management | Wasps and nests, specialist handling only | CANDIDATE — VERIFY |
| WDS-018 | Bee Management / Relocation Referral | Bees; safe relocation through qualified specialists where applicable | CANDIDATE — VERIFY |

### 4.2 Termite, wood and structural pest treatments

| Catalogue ID | Candidate service | Pest / scope | Publication status |
|---|---|---|---|
| WDS-019 | Termite Control | Termite inspection and treatment | CANDIDATE — VERIFY |
| WDS-020 | Pre-Construction Anti-Termite Treatment | Pre-construction soil treatment, subject to applicable standards | CANDIDATE — VERIFY |
| WDS-021 | Post-Construction Anti-Termite Treatment | Treatment for existing buildings | CANDIDATE — VERIFY |
| WDS-022 | Wood Borer Control | Wood-boring insects | CANDIDATE — VERIFY |
| WDS-023 | Furniture Pest Treatment | Pest treatment for affected furniture | CANDIDATE — VERIFY |
| WDS-024 | Structural Pest Inspection | Building and structural pest assessment | CANDIDATE — VERIFY |

### 4.3 Commercial, industrial and institutional programmes

| Catalogue ID | Candidate service | Customer/site type | Publication status |
|---|---|---|---|
| WDS-025 | Office Pest Management | Offices and business premises | CANDIDATE — VERIFY |
| WDS-026 | Retail and Shop Pest Management | Shops, showrooms and retail stores | CANDIDATE — VERIFY |
| WDS-027 | Hotel and Hospitality Pest Management | Hotels, guest houses and hospitality | CANDIDATE — VERIFY |
| WDS-028 | Restaurant and Food-Service Pest Management | Restaurants, cafes and food-service areas | CANDIDATE — VERIFY |
| WDS-029 | Commercial Kitchen Pest Management | Commercial kitchens | CANDIDATE — VERIFY |
| WDS-030 | Hospital and Healthcare Pest Management | Healthcare premises, subject to strict site protocols | CANDIDATE — VERIFY |
| WDS-031 | School and Educational Premises Pest Management | Schools, colleges and campuses | CANDIDATE — VERIFY |
| WDS-032 | Factory and Manufacturing Pest Management | Industrial premises | CANDIDATE — VERIFY |
| WDS-033 | Warehouse and Godown Pest Management | Warehouses and storage facilities | CANDIDATE — VERIFY |
| WDS-034 | Food Processing Facility Pest Management | Food production/processing facilities | CANDIDATE — VERIFY |
| WDS-035 | Pharmaceutical Facility Pest Management | Pharmaceutical premises, subject to site qualification | CANDIDATE — VERIFY |
| WDS-036 | Cold Storage Pest Management | Cold storage facilities | CANDIDATE — VERIFY |
| WDS-037 | Logistics and Transport Facility Pest Management | Logistics hubs and transport premises | CANDIDATE — VERIFY |
| WDS-038 | Mall and Shopping Complex Pest Management | Common and commercial areas | CANDIDATE — VERIFY |
| WDS-039 | Cinema and Entertainment Venue Pest Management | Entertainment premises | CANDIDATE — VERIFY |
| WDS-040 | Residential Society / Apartment Pest Management | Common areas and approved residences | CANDIDATE — VERIFY |

### 4.4 Rodent, flying pest, bird and vector management

| Catalogue ID | Candidate service | Pest / scope | Publication status |
|---|---|---|---|
| WDS-041 | Integrated Rodent Management | Rodent inspection, proofing and control | CANDIDATE — VERIFY |
| WDS-042 | Rodent Proofing and Entry-Point Sealing | Exclusion and proofing work | CANDIDATE — VERIFY |
| WDS-043 | Mosquito and Vector Management | Mosquito/vector monitoring and control | CANDIDATE — VERIFY |
| WDS-044 | Fly Management Programme | Fly monitoring and source reduction | CANDIDATE — VERIFY |
| WDS-045 | Bird Proofing and Deterrent Installation | Lawful exclusion/deterrent systems | CANDIDATE — VERIFY |
| WDS-046 | Pigeon Management | Humane, lawful pigeon exclusion and deterrence | CANDIDATE — VERIFY |

### 4.5 Stored-product, grain, fabric and agricultural-adjacent pest management

| Catalogue ID | Candidate service | Pest / scope | Publication status |
|---|---|---|---|
| WDS-047 | Stored Grain Pest Management | Insects affecting stored grain | CANDIDATE — VERIFY |
| WDS-048 | Stored-Product Pest Management | Pantry and stored-commodity pests | CANDIDATE — VERIFY |
| WDS-049 | Warehouse Commodity Pest Inspection | Stored goods and commodity inspection | CANDIDATE — VERIFY |
| WDS-050 | Textile and Fabric Pest Management | Fabric/textile pests | CANDIDATE — VERIFY |
| WDS-051 | Lawn and Garden Pest Management | Garden/landscape pests, within lawful scope | CANDIDATE — VERIFY |

### 4.6 Specialist and controlled treatments

| Catalogue ID | Candidate service | Scope / prerequisite | Publication status |
|---|---|---|---|
| WDS-052 | Fumigation Services | Only where trained, licensed/authorized and site requirements are met | CANDIDATE — SPECIALIST / COMPLIANCE CHECK |
| WDS-053 | Container Fumigation | Qualified container fumigation only | CANDIDATE — SPECIALIST / COMPLIANCE CHECK |
| WDS-054 | Warehouse / Commodity Fumigation | Qualified facility and commodity fumigation only | CANDIDATE — SPECIALIST / COMPLIANCE CHECK |
| WDS-055 | Bee / Wasp Nest Specialist Response | Qualified specialist handling; no unsafe DIY instructions | CANDIDATE — SPECIALIST CHECK |
| WDS-056 | Snake Sighting Referral / Rescue Coordination | Referral to authorized wildlife rescuers only; not routine pest extermination | CANDIDATE — REFERRAL ONLY / VERIFY |
| WDS-057 | Weed Management | Separate vegetation-control service; include only if BI-BUGS confirms scope | CANDIDATE — ADJACENT SERVICE / VERIFY |

### 4.7 Inspection, prevention and ongoing service programmes

| Catalogue ID | Candidate service | Scope | Publication status |
|---|---|---|---|
| WDS-058 | Pest Inspection and Survey | Site inspection and findings | CANDIDATE — VERIFY |
| WDS-059 | Pest Identification and Assessment | Identification and risk assessment | CANDIDATE — VERIFY |
| WDS-060 | Integrated Pest Management (IPM) | Monitoring, prevention and targeted control programme | CANDIDATE — VERIFY |
| WDS-061 | Preventive Pest Management | Preventive site programme | CANDIDATE — VERIFY |
| WDS-062 | Pest Monitoring and Reporting | Monitoring records and reports | CANDIDATE — VERIFY |
| WDS-063 | Annual Maintenance Contract (AMC) | Scheduled pest-management programme | CANDIDATE — VERIFY |
| WDS-064 | Scheduled / Periodic Pest Control | Recurring service visits | CANDIDATE — VERIFY |
| WDS-065 | Emergency Pest-Control Response | Only with confirmed service hours and response policy | CANDIDATE — VERIFY |
| WDS-066 | Follow-up Inspection and Treatment Review | Post-treatment review, subject to policy | CANDIDATE — VERIFY |
| WDS-067 | Site-Specific Pest Management Plan | Documented plan for a customer/site | CANDIDATE — VERIFY |

### 4.8 Separate allied services — not automatically classified as pest control

| Catalogue ID | Candidate service | Boundary | Publication status |
|---|---|---|---|
| WDS-068 | Disinfection | Separate hygiene service; approved method and claims required | ALLIED SERVICE — VERIFY |
| WDS-069 | Sanitization | Separate hygiene service; define exact scope and claims | ALLIED SERVICE — VERIFY |
| WDS-070 | Water Tank Cleaning | Separate facility-cleaning service; not pest control | ALLIED SERVICE — VERIFY |
| WDS-071 | Drain / Sewer Cleaning or Treatment | Separate specialist service; distinguish pest treatment from cleaning | ALLIED SERVICE — VERIFY |

**Catalogue total:** 71 candidate entries across core pest control, specialist treatments, inspection/programmes and separately labelled allied services. This is a discovery catalogue, not a statement of 71 currently offered BI-BUGS services.

**Owner-approved catalogue direction:** Include a broad, comprehensive pest-control service catalogue rather than limiting the website to a few common pests. The owner has not yet confirmed which individual entries BI-BUGS can deliver, which require partners/referrals, which should be excluded, or the approved service descriptions and claims.

Additional verification required before an entry becomes publishable:
- BI-BUGS capability: in-house / approved partner / referral / not offered.
- Target customer/site segments and actual operating coverage.
- Treatment method, qualifications, applicable licences/permissions and safety controls.
- Approved customer-facing description, preparation/re-entry guidance and limitations.
- Claims, warranties, efficacy statements, certifications and logos supported by evidence.
- Services explicitly excluded from the public catalogue.

**Content rule:** Do not publish efficacy guarantees, health/safety claims, pesticide instructions, licence claims, certification logos, or service availability without approved evidence and appropriate review. Never provide unsafe chemical-use or wildlife-handling instructions to customers.

## 5. Service geography and contact channels

| Input | Owner value | Status | Evidence / notes |
|---|---|---|---|
| Primary operating city/region |  | UNKNOWN |  |
| Full service coverage / excluded areas |  | UNKNOWN |  |
| Official business address (if to publish) |  | UNKNOWN |  |
| Public phone/WhatsApp number |  | UNKNOWN |  |
| Public email address |  | UNKNOWN |  |
| Business hours |  | UNKNOWN |  |
| Emergency/urgent enquiry policy |  | UNKNOWN |  |
| Social profile URLs |  | UNKNOWN |  |

Only publish contact details explicitly approved for public display.

## 6. First-release customer journey decision

Select and approve the required customer action; do not assume that all are needed.

| Capability | Owner decision | Status | Notes |
|---|---|---|---|
| General contact enquiry |  | UNKNOWN |  |
| Service-specific enquiry |  | UNKNOWN |  |
| Request a quote/callback |  | UNKNOWN |  |
| Direct appointment booking |  | UNKNOWN |  |
| Online payment/deposit |  | UNKNOWN |  |
| Customer account/login |  | UNKNOWN |  |
| WhatsApp/call/email handoff |  | UNKNOWN |  |

For each approved form, specify:
- Exact field labels and which fields are required.
- Whether customer name, phone, email, address, property type, pest type, preferred date/time, photos, or free-text notes are required.
- File upload rules and size/type limits, if any.
- Consent text, privacy notice, retention period, and withdrawal/contact route.
- Validation, duplicate-submission handling, confirmation message, and response-time promise.
- Which fields must never be collected.

All of these details are currently UNKNOWN until approved.

## 7. Staff enquiry handling

| Workflow question | Owner answer | Status |
|---|---|---|
| Which staff roles can view enquiries? |  | UNKNOWN |
| Who receives new-enquiry notifications? |  | UNKNOWN |
| Who assigns enquiries? |  | UNKNOWN |
| Allowed enquiry statuses and transitions |  | UNKNOWN |
| Who can edit, export, close, or delete records? |  | UNKNOWN |
| Required internal notes/audit history |  | UNKNOWN |
| Escalation and response-time rules |  | UNKNOWN |
| Staff authentication method and account lifecycle |  | UNKNOWN |

Apply least privilege. No staff account, permission, notification recipient, or workflow is assumed by this workbook.

## 8. Candidate sitemap for owner review

The following is a discussion checklist, not an approved sitemap. Mark each row APPROVED, DEFERRED, or NOT_APPLICABLE.

| Candidate page/area | Decision | Approved content source / notes |
|---|---|---|
| Home | UNKNOWN |  |
| About the company | UNKNOWN |  |
| Services overview | UNKNOWN |  |
| Individual service details | UNKNOWN |  |
| Service areas | UNKNOWN |  |
| Pest/safety information or FAQs | UNKNOWN |  |
| Contact / enquiry | UNKNOWN |  |
| Privacy notice | UNKNOWN |  |
| Terms / disclaimers | UNKNOWN |  |
| Staff-only administration | UNKNOWN |  |

Page labels and navigation must be finalized from approved content and user journeys, not copied blindly from this candidate list.

## 9. Design, accessibility, and language

Owner review required for:
- Mobile-first layout and supported device/browser expectations.
- Brand/design references and visual direction.
- English/Hindi or other language requirements and translation approver.
- Accessibility expectations, keyboard/screen-reader behavior, contrast and text sizing.
- Image permissions, copyright/usage rights, and alt text.
- Performance expectations for typical mobile networks.

Values/targets remain UNKNOWN until reviewed. Do not invent a compliance certification or claim conformance without testing.

## 10. Technical and operational decisions

| Decision | Current status | Owner-approved choice / evidence |
|---|---|---|
| Domain registrar/DNS | UNKNOWN |  |
| Hosting/provider | UNKNOWN |  |
| Existing CMS/framework | UNKNOWN |  |
| Preferred hosting region/data residency | UNKNOWN |  |
| Analytics/consent requirements | UNKNOWN |  |
| Messaging/map/payment integrations | UNKNOWN |  |
| Backup and restore objectives | UNKNOWN |  |
| Monitoring and incident contact | UNKNOWN |  |
| Release approval owner | UNKNOWN |  |

Do not request or store passwords, private keys, API tokens, payment credentials, or recovery codes. Use scoped access grants or secure secret-management channels outside Git.

## 11. First release acceptance gate

The source route is already RESOLVED by accepted decision DEC-BBE-002 (new official website build). The first release cannot be approved until the owner has accepted:
1. Production domain/registrar/DNS and hosting/provider decisions, with ownership, budget, and release authority. An existing-site migration assessment is not applicable to the approved new-build route.
2. Sitemap and page-level content sources.
3. Service catalogue and publishable claims.
4. Public contact details and service geography.
5. Exact first-release customer action and form schema.
6. Consent/privacy/retention requirements.
7. Staff roles and enquiry handling.
8. Responsive design, accessibility, and language expectations.
9. Hosting/domain, security, backup, monitoring, and release ownership.
10. Measurable acceptance tests and explicit exclusions.

## 12. Requirements traceability and change control

Every approved item must be transferred to Specification 31 as a stable requirement ID (`WREQ-...`) and linked to the relevant feature/module/API/data/test records. The workbook is not itself the sole source of truth once an item is approved.

Any material scope change requires impact review and, where appropriate, a new decision linked to `DEC-BBE-001`. Preserve old values and decision history; do not erase rejected/deferred ideas.

## 13. Current audit status — reconciled 2026-11-18

- Repository implementation inventory: a static responsive frontend shell exists in `frontend/` (`index.html`, CSS, and JavaScript). Backend, database, deployment, cloud, mobile, hardware, and AI product implementation remain unverified/not started; project-control scripts and tests are not product features.
- Repository brand/design assets: no approved company brand assets were found in the audited file types; the frontend palette is a temporary prototype.
- Official website source decision: OWNER CONFIRMED — NEW WEBSITE FROM SCRATCH (DEC-BBE-002).
- Existing website/domain: no external website or domain is being asserted or selected as the official source for this project.
- Approved service catalogue/contact details/sitemap: NOT FOUND in the inspected repository; owner approval remains required.
- Implementation: PARTIAL — static frontend foundation only; no customer/business workflow is implemented.
- Testing: frontend shell tests and project-control tests have passed locally; this is not end-to-end product acceptance.
- Production: NOT VERIFIED — no domain, hosting, deployment, or production evidence.

The new-build route is an owner decision. It does not prove that no external site or business records exist, and it does not approve domain, hosting, content, customer workflows, privacy, or production release. Earlier zero-source inventory statements are historical snapshots from before the frontend foundation was created; they are not current status.

## 14. Next action and owner gate

**WDG-01 source decision: RESOLVED — NEW WEBSITE BUILD.** The owner explicitly confirmed on 2026-11-17 that BI-BUGS needs a new official website built from scratch. The decision evidence is recorded in the table above and validated by `scripts/validate_website_source_gate.py`.

**Remaining owner inputs:** Capture company identity/brand, approved services and claims, service geography/contact channels, first-release customer action, form/privacy requirements, staff workflow, sitemap, accessibility/language, hosting/domain, and release acceptance progressively. Do not invent these details or request unrelated decisions all at once.

## 15. Workbook review and remaining owner-input gates — 2026-11-19

The workbook was reviewed against Specification 31, DEC-BBE-001/002, UI/UX, Security, Testing, registries, Release Process, and the current repository baseline. The source route is resolved: **NEW WEBSITE BUILD**. All other blank/UNKNOWN entries remain open; a source-gate PASS does not close them.

The following input groups remain unapproved: (1) company display identity, logo and brand assets; (2) exact approved pest-control service catalogue and publishable claims; (3) service geography and public contact channels; (4) first-release customer action and any form fields; (5) privacy/consent/retention; (6) staff roles and enquiry handling; (7) sitemap and page-level content; (8) language, design and accessibility targets; (9) domain/DNS/hosting/budget/data-region; and (10) monitoring, backup, incident, release and acceptance ownership.

Owner answers must be recorded with source/evidence and approval date. `OWNER_INPUT_RECEIVED` is not the same as `APPROVED`. Do not request passwords, private keys, API tokens, payment credentials, or recovery codes. Unknowns must not be converted into default assumptions to force completion.

**Review result:** Workbook structure and decision gates reviewed; actual business input remains pending. Documentation may be internally organized, but requirements/design readiness and owner acceptance are blocked until the relevant inputs are supplied.


## 16. Owner input completion register and response protocol — 2026-11-19

This section is the concise working register for completing the open business decisions. It intentionally contains no assumed values. The detailed question tables above remain the source questionnaire. An answer is not approved until the owner confirms it; record evidence/source and approval date.

| Register ID | Decision group | Required owner answer/evidence | Requirement conversion | Current status |
|---|---|---|---|---|
| OI-01 | Public company identity and brand | Exact display/legal wording, approved logo/assets, colours, typography, language, writing tone | WREQ for approved identity/brand/content rules only | PARTIALLY RESOLVED — legal/business identity source-confirmed by WREQ-C-001; public display wording and brand inputs remain OPEN |
| OI-02 | Service catalogue and claims | Comprehensive candidate taxonomy requested; confirm BI-BUGS delivery capability, partner/referral status, exclusions, coverage, treatment descriptions, claims, licences/certifications/safety wording | WREQ for each individually verified and owner-approved service/content/claim | PARTIALLY RESOLVED — owner directed broad catalogue inclusion; individual service availability and publishable claims remain OPEN |
| OI-03 | Service coverage and contact | Operating city/areas, exclusions, public phone/email/address/hours and emergency policy | WREQ for approved service-area and public-contact behavior | OPEN — OWNER INPUT REQUIRED |
| OI-04 | Customer journey | First-release customer action; whether enquiry, callback, appointment, payment, account or channel handoff is in scope | WREQ for the owner-selected first-release customer action | OPEN — OWNER INPUT REQUIRED |
| OI-05 | Customer data and privacy | Exact minimum fields, purpose, notice/consent, retention/deletion, access roles, exports and incident handling | WREQ for approved data-purpose/privacy/retention controls | OPEN — OWNER INPUT REQUIRED |
| OI-06 | Staff operations | Roles, assignment, status transitions, response/escalation, audit history and account lifecycle | WREQ for approved staff roles and workflow, if in scope | OPEN — OWNER INPUT REQUIRED |
| OI-07 | Sitemap and content | Approved pages, page owner, source material, calls-to-action and legal notices | WREQ for approved sitemap/page/content requirements | OPEN — OWNER INPUT REQUIRED |
| OI-08 | Design and accessibility | Approved visual references, mobile requirements, languages, accessibility target and acceptance method | WREQ for approved language/design/accessibility criteria | OPEN — OWNER INPUT REQUIRED |
| OI-09 | Technical and hosting | Domain/DNS owner, hosting preference, budget, data region, framework constraints and integrations | WREQ for approved technical/hosting constraints | OPEN — OWNER INPUT REQUIRED |
| OI-10 | Operations and release | Support owner, monitoring, backups/recovery, incident contact, release approver and rollback authority | WREQ for approved operational/release requirements | OPEN — OWNER INPUT REQUIRED |
| OI-11 | Acceptance | Measurable first-release acceptance criteria and explicit documentation/package approval | Acceptance criteria and explicit package-acceptance evidence; do not create a product feature ID solely for approval | OPEN — OWNER INPUT REQUIRED |

### Response and approval protocol

1. Capture the owner's answer verbatim or attach the owner-provided source; do not silently rewrite it as a stronger claim.
2. Mark it `RECEIVED — NOT APPROVED` until the owner explicitly approves the exact wording/decision.
3. Record approver role, approval date, evidence/source reference, scope, and any expiry/review condition.
4. Convert approved requirements into stable `WREQ-*` entries in Specification 31 with priority, rationale, acceptance criteria, dependencies, risk, and lifecycle state.
5. Link only necessary registry records and tests. Do not create API/database/AI records for unapproved or nonexistent capabilities.
6. Re-run the documentation and traceability audits after the approved inputs are incorporated.

**Requirement conversion rule:** OI-01 through OI-11 do not create product requirements until the owner supplies and explicitly approves the exact decision. Once approved, split combined answers into atomic, testable `WREQ-*` records; record the source, approval date, scope, priority, acceptance criteria, dependencies, risk/privacy impact, and lifecycle. If an item is explicitly deferred or not applicable, record that disposition and rationale instead of creating a requirement.

**Current partial resolutions:** OI-01 legal/business identity is source-confirmed as `BI-BUGS Pest Control Services Pvt Ltd` by existing project fact WREQ-C-001; public display/brand approval remains open. OI-02 now records the owner-directed comprehensive 71-entry candidate catalogue in Section 4; it does not confirm BI-BUGS delivery capability, partner arrangements, individual service availability, legal permissions, treatment methods, claims, coverage, or public wording.

**Current resolved decision:** OI-00 — Delivery path: `OWNER APPROVED — NEW_WEBSITE_BUILD` (DEC-BBE-002, 2026-11-17). This does not close OI-01 through OI-11.
