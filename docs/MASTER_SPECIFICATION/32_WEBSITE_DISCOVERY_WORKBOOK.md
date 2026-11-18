# BI-BUGS EMPIRE OS-X 2.0
# MASTER SPECIFICATION — 32
# WEBSITE DISCOVERY AND OWNER INPUT WORKBOOK

**Specification ID:** BBEOSX-MS-32
**Specification status:** DRAFT — OWNER INPUT REQUIRED
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related:** `31_WEBSITE_REQUIREMENTS.md`, `17_UI_UX_SYSTEM.md`, `20_FEATURE_REGISTRY.md`, `21_MODULE_REGISTRY.md`, `22_API_REGISTRY.md`, `23_DATABASE_REGISTRY.md`, `30_ROADMAP_20_YEARS.md`, `99_PROJECT_PROGRESS.md`
**Controlling decision:** `DEC-BBE-001`

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
| Official website URL | UNKNOWN | Owner supplies exact URL, or confirms no current official site. |
| Website ownership | NOT VERIFIED | Confirm that the supplied domain/site belongs to BI-BUGS Pest Control Services Pvt Ltd. |
| Delivery path | BLOCKED | Choose existing-site audit/migration/redesign, or new website build. |
| Existing hosting/CMS/source access | UNKNOWN | Identify provider/platform and provide a safe owner-approved export/access route if relevant. |
| Current website status | UNKNOWN | State live, offline, under construction, or no website. |

**Gate WDG-01:** No migration, redesign, DNS, hosting, or production changes until the official source and owner authority are verified.

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

The first release cannot be approved until the owner has accepted:
1. Official website source or explicit new-build decision.
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

## 13. Current audit status — 2026-11-17

- Repository implementation inventory: zero non-placeholder source files across the ten implementation areas.
- Repository brand/design assets: none found in the audited file types.
- Official website URL/domain: NOT VERIFIED.
- Public search: a professional profile result mentions “BI BUGS PEST CONTROL SERVICES”, but does not establish an official website/domain or company ownership of a candidate URL.
- Approved service catalogue/contact details/sitemap: NOT FOUND in the inspected repository.
- Implementation: NOT STARTED.
- Testing: NOT RUN.
- Production: NOT VERIFIED.

This is a repository and public-search boundary, not proof that no external website, assets, or business records exist.

## 14. Next action and owner gate

**Single blocking owner decision:** Supply the exact official website URL, or explicitly confirm that BI-BUGS needs a new website built from scratch.

Once this is known, proceed with the matching audit/build path. The remaining workbook items can be captured progressively; do not hold up the project by asking for unrelated details all at once.
