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
| Exact legal/business display name |  | UNKNOWN |  |
| Approved logo file/source |  | UNKNOWN |  |
| Brand colours |  | UNKNOWN |  |
| Typography/font preference |  | UNKNOWN |  |
| Approved photos/videos |  | UNKNOWN |  |
| Brand/design reference sites |  | UNKNOWN |  |
| Languages required (e.g. English/Hindi) |  | UNKNOWN |  |
| Tone and writing style |  | UNKNOWN |  |

Do not create or publish an unapproved logo, certification, testimonial, guarantee, or brand claim.

## 4. Service catalogue and publishable content

Create one row per service only after the owner supplies its approved name and content.

| Service ID | Exact approved service name | Customer problem/use case | Approved description | Coverage/limitations | Safety notice/source | Status |
|---|---|---|---|---|---|---|
| WDS-001 |  |  |  |  |  | UNKNOWN |
| WDS-002 |  |  |  |  |  | UNKNOWN |
| WDS-003 |  |  |  |  |  | UNKNOWN |

Additional owner inputs:
- Which customer segments are served (residential, commercial, industrial, institutional, or other): UNKNOWN.
- Which pest categories/treatments may be publicly described: UNKNOWN.
- Which treatment claims, chemical names, safety instructions, warranties, licences, and certifications are legally approved for publication: UNKNOWN.
- Which services must not be advertised: UNKNOWN.

**Content rule:** Do not publish efficacy guarantees, health/safety claims, pesticide instructions, licence claims, or certification logos without approved evidence and appropriate review.

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
