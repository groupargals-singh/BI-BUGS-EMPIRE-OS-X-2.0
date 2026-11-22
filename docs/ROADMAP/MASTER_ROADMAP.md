# Master Roadmap

**Status:** Draft planning view; dates and delivery commitments are not established.

Canonical strategy: `../MASTER_SPECIFICATION/30_ROADMAP_20_YEARS.md`.


Documentation control: use `../MASTER_SPECIFICATION/DOCUMENTATION_COMPLETION_MATRIX.md` as the document-by-document acceptance checklist. The matrix is a control artifact, not a percentage increase or owner approval.

## Ordered work themes
1. **ACTIVE — Documentation and owner-acceptance gate.** The document-by-document semantic review of Specifications 00–34 and supporting documents is recorded complete. The internal package is ready for owner review; remaining work is owner discovery (OI-01–OI-11), conversion of approved decisions into traceable requirements, final verification, and explicit owner acceptance. No new product-coding work starts before the owner-input and documentation gate is accepted. See `../MASTER_SPECIFICATION/DOCUMENTATION_COMPLETION_MATRIX.md` and `../MASTER_SPECIFICATION/34_CROSS_DOCUMENT_TRACEABILITY_AUDIT.md`.
2. Inventory actual source modules and map them to approved website/business requirements.
3. Use `32_WEBSITE_DISCOVERY_WORKBOOK.md` to capture the remaining BI-BUGS owner inputs: sitemap, approved content, customer enquiry path, staff follow-up workflow, brand, service area, and release constraints; transfer approved items into `31_WEBSITE_REQUIREMENTS.md`. The new-build source decision is recorded as `DEC-BBE-002`.
4. Existing prototype boundary: responsive static website shell is already implemented and covered by six unit tests. Treat it as a limited foundation only; do not add product features until documentation acceptance and approved requirements. Enquiry capture and staff review remain unapproved and unimplemented.
5. Establish repeatable unit, integration, contract, and acceptance checks for that journey.
6. Implement only after BI-BUGS-specific requirements and interfaces are reviewed.
7. Verify backup/restore, release, monitoring, and rollback paths before production use.
8. **COMPLETED — Lifecycle metadata standard and migration.** Specifications 01–34 declare lifecycle dimensions using canonical labels or documented legacy aliases. The read-only audit utility is `scripts/validate_spec_lifecycle.py`; preserve legacy meaning and never infer owner approval from `ACTIVE` labels. Semantic document review is recorded; owner acceptance remains separate.

9. Website source gate: RESOLVED — owner confirmed a new official BI-BUGS website from scratch on 2026-11-17; the decision is recorded in `32_WEBSITE_DISCOVERY_WORKBOOK.md` and validated by `scripts/validate_website_source_gate.py`. This resolves only the source route, not the remaining business/content/privacy/security/hosting/release approvals. Next: define and approve the first small customer journey, then create traceable requirements and implementation records.

**Documentation re-audit — 2026-11-17:** Master Index lifecycle metadata, Testing Architecture controls, new-build decision wording, cross-document audit status, and the current progress snapshot were corrected. Automated structural checks pass; semantic owner review and remaining owner inputs are still open.

Each theme needs an owner, acceptance criteria, dependency list, and test evidence before being marked done.

**Current priority reconciliation — 2026-11-18:** Documentation Phase 1 is the active workstream. Historical source-gate and zero-source inventory statements remain dated history; current status is DEC-BBE-002 resolved and a static frontend shell present. No further product coding is authorized by this roadmap until the documentation gate is accepted.

**Security architecture review — 2026-11-18:** Specification 15 now maps reusable security controls to the current static website and marks forms, accounts, booking, payments, backend/API/database, AI/plugins, mobile, and hardware as conditional/not approved/not implemented. The data/privacy approval gate and minimum public-release security evidence are defined in Specification 15 Section 89. Owner acceptance and implementation evidence remain outstanding; documentation review continues before product coding.

**DevOps/release review — 2026-11-18:** Specifications 16 and 29 now distinguish the present static website baseline from conditional infrastructure and future workflows, separate documentation commits from software releases, and define evidence required for the first public website release, recovery, and operational ownership. Hosting, domain, CI provider, deployment, and production remain unapproved/unimplemented.


**AI/data extensibility scope review — 2026-11-18:** Specifications 11–14 and 19 now explicitly distinguish BI-BUGS product requirements from reusable AI, knowledge-graph, plugin, and microservices patterns. AI, graph storage, plugins, and microservices remain unapproved for the first website release; project memory is not a customer/employee data store. Adoption requires a specific business requirement, security/data controls, registry traceability, tests, and owner approval. Documentation Phase 1 remains active.

## Current execution snapshot — 2026-11-19

Documentation Phase 1 remains active at 70% provisional. The specification-by-specification and supporting-document semantic reviews are recorded as complete; the remaining cross-document traceability, owner-input, final verification, and acceptance gates are listed in the Documentation Completion Matrix. The source decision is resolved, but business content and first-release workflow are not. Keep phase percentages provisional and do not mark the phase complete until the matrix's acceptance checklist and owner approval are satisfied.


**Consistency reconciliation — 2026-11-20:** The internal documentation package is ready for owner review, not owner-accepted. OI-01–OI-11 remain open. Approved decisions alone may become `WREQ-*` records; no speculative registry population is allowed. Milestone 67 updates the canonical audit and revision history.

**Owner-input reconciliation — 2026-11-21:** OI-01 is partially resolved for the legal/business identity fact only: `BI-BUGS Pest Control Services Pvt Ltd` is recorded in WREQ-C-001. Public display wording and brand assets remain owner approval items. OI-02 is partially resolved for catalogue breadth: owner directed a comprehensive 71-entry candidate taxonomy in Specification 32 Section 4. Individual BI-BUGS service availability, delivery capability, partner/referral status, exclusions, coverage, permissions, treatment details and claims remain unverified. OI-03–OI-11 remain open. Documentation remains 70% provisional.


**Comprehensive service catalogue — 2026-11-21:** Owner requested inclusion of the full range of pest-control services. Specification 32 now contains 71 grouped candidate entries, with allied cleaning/hygiene/weed services explicitly separated from core pest control. Only individually verified and owner-approved services may be published as available. Milestone 70 records the catalogue capture; documentation progress remains 70% because service capability/claims and other owner acceptance gates are still open.


**Service approval control gate — 2026-11-23:** All 71 WDS candidate entries now carry explicit provider/delivery, evidence, coverage, compliance/safety, owner approval, content approval, and publication status fields. They default to blocked. The strict service-catalogue validator and unit tests prevent publication unless all required gates are satisfied. This completes the internal approval-control design, not the owner verification of the services themselves.
