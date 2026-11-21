# BI-BUGS EMPIRE OS-X 2.0
# MASTER SPECIFICATION — 31
# BI-BUGS PEST CONTROL WEBSITE REQUIREMENTS BASELINE

**Specification ID:** BBEOSX-MS-31
**Specification status:** DRAFT FOR REVIEW — REQUIREMENTS INVENTORY INCOMPLETE
**Implementation status:** PARTIAL — responsive static frontend foundation created; business workflows not implemented
**Testing status:** FRONTEND FOUNDATION UNIT TESTS PASS — see `testing/test_website_shell.py`
**Production status:** NOT VERIFIED — preview only; no deployment evidence
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Scope decision:** `DEC-BBE-001`
**Related:** `01_PROJECT_VISION.md`, `03_MASTER_BLUEPRINT.md`, `15_SECURITY.md`, `17_UI_UX_SYSTEM.md`, `18_TESTING.md`, `20_FEATURE_REGISTRY.md`, `21_MODULE_REGISTRY.md`, `22_API_REGISTRY.md`, `23_DATABASE_REGISTRY.md`, `29_RELEASE_PROCESS.md`, `30_ROADMAP_20_YEARS.md`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose

This document establishes the requirements baseline for the BI-BUGS Pest Control Services website and the business workflows directly supporting it.

It separates confirmed project scope from candidate workflows, unknown business facts, and requirements that still need the project owner's confirmation. It is deliberately not a generic website template and must not invent company details, service offerings, prices, contact information, policies, or integrations.

## 2. Controlling project scope

The controlling scope is defined by accepted decision `DEC-BBE-001`:

- BI-BUGS EMPIRE OS-X 2.0 is for BI-BUGS Pest Control Services Pvt Ltd.
- The BI-BUGS Pest Control Services website is the primary customer-facing product.
- Supporting backend, data, staff administration, communications, security, deployment, reporting, AI, and automation capabilities are in scope only when they serve the website or the company's pest-control business workflows.
- SAHIBEX and unrelated projects are excluded.
- A generic multi-industry platform is not the current delivery objective.
- Existing future architecture ideas are retained as ideas; they are not automatically approved requirements.

## 3. Confirmed facts

| ID | Confirmed fact | Evidence |
|---|---|---|
| WREQ-C-001 | The business owner is BI-BUGS Pest Control Services Pvt Ltd. | Project identity and owner record in the existing master blueprint. |
| WREQ-C-002 | The primary product is the BI-BUGS Pest Control Services website. | Project owner's explicit scope instruction; DEC-BBE-001. |
| WREQ-C-003 | The website is the primary customer-facing entry point. | Project Vision and Master Blueprint aligned under DEC-BBE-001. |
| WREQ-C-004 | Supporting technology must serve the pest-control website/business purpose. | DEC-BBE-001. |

These facts do not define the website's exact pages, wording, visual design, service catalogue, or transaction rules.

**Identity clarification:** WREQ-C-001 supports the recorded business identity `BI-BUGS Pest Control Services Pvt Ltd`. This is a source-confirmed project fact, not approval of a logo, brand system, or exact public-facing display treatment; those remain owner-review items in OI-01.

## 4. Candidate first customer journey — not yet approved in detail

The following is a planning candidate only:

1. A visitor opens the BI-BUGS website.
2. The visitor reads company and pest-control service information approved by BI-BUGS.
3. The visitor uses a contact or service-enquiry path confirmed by BI-BUGS.
4. The system validates and securely records the submitted enquiry, if enquiry capture is confirmed as the first workflow.
5. Authorized staff can review and follow up, if this staff workflow is confirmed.
6. Any acknowledgement or response channel uses only a method approved by BI-BUGS.

Do not implement this candidate until the website requirements, data fields, consent/privacy wording, staff roles, and acceptance criteria are reviewed.

## 5. Requirements still unknown — do not guess

The following information has not been established by the inspected repository documents. Each item remains **UNKNOWN / OWNER INPUT REQUIRED** until supported by an approved source.

### 5.1 Website identity and access
- Official production domain/URL. **New-build route confirmed (DEC-BBE-002, 2026-11-17); production domain/URL remains UNKNOWN / OWNER INPUT REQUIRED.** No domain or hosting provider is approved yet.
- Existing-site migration/redesign: **NOT APPLICABLE to the approved new-build route**; owner confirmed the new official website must be built from scratch.
- Approved logo, brand assets, colours, typography, imagery, and design references.
- Supported languages and exact language versions.
- Target geographic/service coverage and branch details.

### 5.2 Website information architecture
- Approved sitemap and page list.
- Official company/about content.
- Exact pest-control service catalogue and approved service descriptions.
- Approved pest information, treatment explanations, FAQs, and safety notices.
- Testimonials, certifications, licences, guarantees, and claims that may legally be published.
- Required downloads, galleries, case studies, or educational content.

### 5.3 Customer actions
- Whether the first release supports contact enquiries, service enquiries, quote requests, direct bookings, or a combination.
- Exact form fields and validation rules.
- Required contact channels and official contact details.
- Whether customers need accounts or guest access.
- Whether online prices, quotations, deposits, or payments are required.
- Confirmation messages, response-time promises, and notification channels.
- Consent, privacy notice, terms, and data-retention requirements.

### 5.4 Staff and business operations
- Staff roles and access permissions.
- Who receives, reviews, assigns, and closes enquiries.
- Whether appointment scheduling is required and its rules.
- Whether technicians need a mobile interface in the first release.
- Whether customer history, invoices, payments, inventory, AMC/renewals, or reports are required in the first release or later.
- Required audit trail and management reporting.

### 5.5 Technology and operations
- Hosting/provider and deployment target.
- Domain/DNS and existing hosting constraints.
- Required integrations (for example messaging, maps, payment, analytics, or CRM); none are assumed.
- Backup, recovery, monitoring, security, accessibility, and performance acceptance targets.
- Data residency, privacy, and applicable legal/compliance requirements.

## 6. Source-of-truth and evidence rules

- Business facts and published content must come from BI-BUGS-approved sources.
- Do not fabricate service names, treatment claims, pricing, guarantees, addresses, phone numbers, email addresses, licences, or customer testimonials.
- Keep confirmed facts, proposed ideas, assumptions, and unknowns visibly separate.
- Every accepted requirement must have a stable ID, owner/source, scope, priority, dependencies, acceptance criteria, and review status.
- A website screenshot or existing website may be used as evidence only after its source and currency are established.
- Changes to primary scope require a new owner-approved decision linked to DEC-BBE-001.

## 7. Requirements lifecycle

Use these states for each website requirement:

- `UNKNOWN` — required information is not available.
- `PROPOSED` — candidate idea awaiting review.
- `UNDER_REVIEW` — source and impact are being checked.
- `APPROVED` — BI-BUGS owner has accepted the requirement.
- `IMPLEMENTED_UNVERIFIED` — code exists but acceptance evidence is incomplete.
- `VERIFIED` — acceptance criteria pass on a recorded revision.
- `RELEASED` — included in an approved release.
- `REJECTED` / `DEFERRED` — not included now, with reason recorded.

Never promote an unknown or proposed requirement directly to implemented or released.

## 8. First requirements-capture deliverables

Before implementation planning is approved, produce:

1. Confirmed source route (RESOLVED by DEC-BBE-002: new website build) and owner-approved production domain/hosting decision; an existing-site assessment is NOT APPLICABLE to the approved new-build route.
2. Owner-approved sitemap and navigation structure.
3. Owner-approved service catalogue and publishable content sources.
4. Customer journey and exact enquiry/contact/booking decision.
5. Form fields, validation, consent/privacy wording, and data lifecycle.
6. Staff roles and enquiry handling/follow-up workflow.
7. UI/UX references, responsive and accessibility expectations.
8. First-release scope, explicit exclusions, and measurable acceptance criteria.
9. Security, deployment, backup, monitoring, and release requirements.

## 9. Acceptance criteria for this baseline

- The primary project scope matches DEC-BBE-001.
- Confirmed facts are traceable to a source.
- Unknown information is not presented as approved.
- The candidate journey is clearly labelled as unapproved until reviewed.
- No invented company content, services, prices, contacts, or integrations appear.
- Website requirements link to the Feature, Module, API, Database, UI/UX, Security, Testing, and Roadmap records as they are approved.
- Implementation status must reflect verified code and test evidence; the current static frontend foundation is PARTIAL and does not imply complete website functionality.

## 10. Current status and limitations

- Scope alignment: RECORDED in DEC-BBE-001.
- Requirements inventory: INITIAL BASELINE CREATED; detailed owner inputs remain incomplete.
- Sitemap and service catalogue: UNKNOWN.
- Enquiry/booking rules: UNKNOWN; candidate journey only.
- Website implementation: PARTIAL — responsive static frontend foundation exists in `frontend/`; no backend, database, enquiry, booking, payment, or staff workflow is implemented.
- Frontend foundation tests: 6 unit tests PASS; complete project-control test suite: 19 tests PASS.
- Production: NOT VERIFIED — the frontend is a development preview and is not approved for public launch.

This document is a requirements inventory, not a completed website specification and not evidence of a working website.


## 11. Repository evidence audit — 2026-11-17

A read-only audit of the current repository working copy was completed before selecting an implementation task.

| Evidence check | Result | Requirement impact |
|---|---|---|
| Non-placeholder files in `frontend/`, `backend/`, `database/`, `deployment/`, `cloud/`, `mobile/`, `hardware/`, `ai-core/`, `scripts/`, and `testing/` | 0 files found | There is no existing application implementation in these areas to assess or safely extend. |
| Tracked implementation files across those ten areas | 0 | No existing frontend/backend/database source code is available for a migration or feature audit. |
| Brand/design assets (`png`, `jpg`, `jpeg`, `webp`, `svg`, `fig`, `pdf`) in the repository | 0 files found | No approved logo, imagery, or design reference was located in the repository. |
| Official website URL/domain, company contact details, approved service catalogue | Not found in the inspected project documentation at the time of the audit | Owner later confirmed the new-build route via DEC-BBE-002; public domain/contact details and approved service catalogue remain UNKNOWN. |
| Project documentation | Present | Documentation describes intended architecture and scope, not a functioning website. |

**Audit boundary:** This is a repository inventory, not a claim that the company has no website or brand assets elsewhere. It does not inspect private hosting accounts, domain registrar accounts, company devices, or unprovided files. A public search did not establish a verified official domain. Any external candidate must be confirmed by the project owner before it is treated as BI-BUGS property.

## 12. Historical source gate and next owner inputs

The source decision recorded in this earlier requirements baseline was resolved by the owner on 2026-11-17 through accepted decision `DEC-BBE-002`: build a new official BI-BUGS website from scratch. The decision is recorded in `32_WEBSITE_DISCOVERY_WORKBOOK.md` and passes `scripts/validate_website_source_gate.py --strict`.

Remaining inputs include approved brand assets, official public contact details, service catalogue, service area, sitemap, and first-release customer action. If website/assets are held in a private account, use an owner-approved export or scoped access route; do not share passwords or secret keys in chat or repository files.

The static frontend foundation may be developed using confirmed facts and clearly labelled placeholders. Do not implement customer data collection, booking, payment, or public claims until the owner approves the relevant content, customer journey, privacy, and operational requirements.


## 15. Public identity search follow-up — 2026-11-17

A further exact-name public web search did not establish an official BI-BUGS website/domain. A LinkedIn directory result contains a profile text entry mentioning “BI BUGS PEST CONTROL SERVICES”, but this is not proof of domain ownership, legal identity, or an official website. Other search results were unrelated directory/listing material. Therefore:

- At the time of that public-search follow-up, no official website URL/domain had been verified.
- The owner subsequently confirmed the new-build route in DEC-BBE-002; no external candidate URL was adopted as the source.
- Public domain registration/selection and contact details remain separate open decisions.

This is a limited historical public-search result, not proof that no external website exists. Do not copy third-party contact details or claims into BI-BUGS content.


## 16. Frontend foundation implementation update — 2026-11-17

The initial repository audit in section 11 predates the first frontend implementation. The current working tree now contains a static frontend shell at `frontend/index.html`, styles at `frontend/assets/css/styles.css`, and accessible mobile navigation at `frontend/assets/js/main.js`. The earlier zero-file inventory remains a historical snapshot and is not the current inventory.

The preview contains only the confirmed company name and clearly marked pending content. It intentionally has no enquiry form, booking, payment, customer-data collection, public contact details, approved service descriptions, backend, database, or deployment. See `frontend/README.md` for local preview instructions and `testing/test_website_shell.py` for six passing foundation checks.

## 17. Documentation review and owner-input status — 2026-11-19

This requirements baseline has been reviewed against DEC-BBE-001/002, the Discovery Workbook, UI/UX, Security, Testing, Feature/Module/API/Database registries, Release Process, and current repository inventory.

**Confirmed:** BI-BUGS Pest Control Services website is the primary product; the owner selected a new website build from scratch; a limited static frontend shell exists as a preview foundation.

**Still unknown and requiring owner evidence:** approved legal/display name and brand assets; service catalogue and publishable treatment claims; service geography; public phone/WhatsApp/email/address and business hours; sitemap and page content; first customer action (contact/enquiry/quote/booking); exact form fields; privacy/consent/retention; staff roles and enquiry handling; language/accessibility expectations; domain/DNS/hosting/provider/budget; analytics/integrations; operational and release owners.

The candidate first customer journey and candidate sitemap remain proposals, not approved requirements. The workbook is the capture mechanism; once a decision is accepted, transfer it into a stable `WREQ-*` requirement with source, owner, scope, priority, acceptance criteria, dependencies, risk, and lifecycle. Link only justified feature/module/API/data/test records. No registry should be populated from assumptions.

**Review result:** Scope and unknowns are internally consistent. This document is not complete for implementation planning until the owner supplies and accepts the required business inputs and measurable first-release acceptance criteria.


## 18. Requirement record template and owner approval evidence — 2026-11-19

No new business requirements are created from unknown workbook fields. When an owner decision is received and approved, add one record using this minimum schema:

| Field | Required content |
|---|---|
| Requirement ID | Stable unique `WREQ-*` identifier |
| Title / statement | One testable requirement, with one primary outcome |
| Source / evidence | Owner statement, approved source document, or authoritative company asset |
| Approval | Approver role/name as authorized, approval date, approval status |
| Scope | Website page, customer journey, staff workflow, data or operational boundary |
| Priority | Owner-confirmed priority and rationale |
| Acceptance criteria | Observable, testable pass/fail conditions |
| Dependencies | Related requirements, policy, content, API/data or external provider |
| Risk / privacy | Data classification, security/privacy implications and mitigations |
| Lifecycle | `PROPOSED`, `OWNER_APPROVED`, `IMPLEMENTED`, `TESTED`, `RELEASED`, `PRODUCTION_VERIFIED` as evidence supports |

`RECEIVED` is not `OWNER_APPROVED`; `OWNER_APPROVED` is not `IMPLEMENTED`; implementation is not `TESTED`; test pass is not release or production verification. Do not skip lifecycle states. Keep a requirement in the workbook until its evidence and approval are traceable here.

**Current owner-approved website requirement records:** No service/content/customer-journey requirements have yet been approved beyond the project-level scope facts WREQ-C-001 through WREQ-C-004 and the new-build delivery decision DEC-BBE-002. The customer journey and sitemap remain candidates.
