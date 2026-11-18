# BI-BUGS EMPIRE OS-X 2.0
# MASTER SPECIFICATION — 31
# BI-BUGS PEST CONTROL WEBSITE REQUIREMENTS BASELINE

**Specification ID:** BBEOSX-MS-31
**Specification status:** DRAFT FOR REVIEW — REQUIREMENTS INVENTORY INCOMPLETE
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Scope decision:** `DEC-BBE-001`
**Related:** `01_PROJECT_VISION.md`, `03_MASTER_BLUEPRINT.md`, `17_UI_UX_SYSTEM.md`, `20_FEATURE_REGISTRY.md`, `21_MODULE_REGISTRY.md`, `30_ROADMAP_20_YEARS.md`, `99_PROJECT_PROGRESS.md`

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
- Official production website URL/domain. **Audit result (2026-11-17): NOT VERIFIED** in the repository or public search; similarly named domains/listings are not sufficient proof of ownership.
- Whether an existing website must be migrated, redesigned, replaced, or integrated.
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

1. Verified website/domain and existing-site assessment.
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
- Implementation status remains NOT STARTED until actual code and verification evidence exist.

## 10. Current status and limitations

- Scope alignment: RECORDED in DEC-BBE-001.
- Requirements inventory: INITIAL BASELINE CREATED; detailed owner inputs remain incomplete.
- Sitemap and service catalogue: UNKNOWN.
- Enquiry/booking rules: UNKNOWN; candidate journey only.
- Website implementation: NOT STARTED.
- Application tests: NOT RUN.
- Production: NOT VERIFIED.

This document is a requirements inventory, not a completed website specification and not evidence of a working website.


## 11. Repository evidence audit — 2026-11-17

A read-only audit of the current repository working copy was completed before selecting an implementation task.

| Evidence check | Result | Requirement impact |
|---|---|---|
| Non-placeholder files in `frontend/`, `backend/`, `database/`, `deployment/`, `cloud/`, `mobile/`, `hardware/`, `ai-core/`, `scripts/`, and `testing/` | 0 files found | There is no existing application implementation in these areas to assess or safely extend. |
| Tracked implementation files across those ten areas | 0 | No existing frontend/backend/database source code is available for a migration or feature audit. |
| Brand/design assets (`png`, `jpg`, `jpeg`, `webp`, `svg`, `fig`, `pdf`) in the repository | 0 files found | No approved logo, imagery, or design reference was located in the repository. |
| Official website URL/domain, company contact details, approved service catalogue | Not found in the inspected project documentation | These remain UNKNOWN; do not invent or infer them from similarly named businesses/domains. |
| Project documentation | Present | Documentation describes intended architecture and scope, not a functioning website. |

**Audit boundary:** This is a repository inventory, not a claim that the company has no website or brand assets elsewhere. It does not inspect private hosting accounts, domain registrar accounts, company devices, or unprovided files. A public search did not establish a verified official domain. Any external candidate must be confirmed by the project owner before it is treated as BI-BUGS property.

## 12. Next owner-input gate

The next implementation decision is blocked only on identifying the official website source:

- If an existing official website exists, provide its exact URL so its pages, content, customer journey, and technical constraints can be audited before migration/redesign decisions.
- If no website currently exists, explicitly confirm **new website build**; then capture approved brand assets, official contact details, service catalogue, service area, and first-release customer action before coding.
- If the website/assets are held in a file or private account, provide an owner-approved export or access route; do not share passwords or secret keys in chat or repository files.

No application implementation should be started from guessed company facts. The first code slice can be selected once the official source/new-build decision and minimum approved content are available.


## 15. Public identity search follow-up — 2026-11-17

A further exact-name public web search did not establish an official BI-BUGS website/domain. A LinkedIn directory result contains a profile text entry mentioning “BI BUGS PEST CONTROL SERVICES”, but this is not proof of domain ownership, legal identity, or an official website. Other search results were unrelated directory/listing material. Therefore:

- Official website URL/domain remains **UNKNOWN / NOT VERIFIED**.
- No candidate URL is promoted to an approved source.
- The owner must supply the exact official URL or explicitly confirm a new website build.

This is a limited public-search result, not proof that no external website exists. See the current search result references in the project conversation; do not copy third-party contact details or claims into BI-BUGS content.
