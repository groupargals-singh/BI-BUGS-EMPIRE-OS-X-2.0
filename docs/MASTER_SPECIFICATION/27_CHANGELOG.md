# BI-BUGS EMPIRE OS-X 2.0 — CHANGELOG

**Specification ID:** BBEOSX-MS-27
**Status:** REVIEWED — OWNER ACCEPTANCE PENDING
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related:** `19_PROJECT_MEMORY.md`, `20_FEATURE_REGISTRY.md`, `25_DECISION_REGISTRY.md`, `28_VERSION_HISTORY.md`, `29_RELEASE_PROCESS.md`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose

Provide a human-readable, traceable record of meaningful project changes so maintainers and users can understand what changed, why it changed, and what verification supports the change.

The changelog records actual changes. It must not imply that planned work has shipped.

## 2. Scope

Record user-visible changes, architecture and contract changes, bug fixes, security changes, deprecations, removals, migrations, operational changes, and known limitations. Tiny formatting-only changes may be grouped unless they materially affect traceability.

## 3. Entry format

Each release or unreleased group should include:
- version or clearly labelled `Unreleased`;
- date or explicit pending date;
- Added, Changed, Fixed, Security, Deprecated, Removed, Migration/Operations, and Known Issues subsections as applicable;
- concise impact and affected areas;
- compatibility/migration notes for breaking changes;
- linked decision, feature, issue/defect, commit/tag and test evidence when available;
- approval/release reference for released entries.

Do not invent version numbers, dates, test results, or release links.

## 4. Change categories

- **Added:** newly available and verified capability.
- **Changed:** behavior or contract changes.
- **Fixed:** confirmed defect corrections, including the observable symptom.
- **Security:** security-relevant changes, with responsible disclosure where required.
- **Deprecated:** functionality still present but scheduled for removal.
- **Removed:** capability actually removed from the released artifact.
- **Migration/Operations:** data, configuration, deployment, or recovery actions required.
- **Known Issues:** important limitations and unresolved defects.

Documentation-only changes must be identified as such when they could otherwise be mistaken for software functionality.

## 5. Unreleased versus released

Keep unreleased changes separate from published releases. A change may move to a released section only after the release process has been followed and the release record identifies the artifact/version. Do not rewrite published history to conceal a defect; add a correction entry with links.

## 6. Accuracy and evidence

Each statement must match the scope of the evidence. A code change does not prove the feature passes tests; a passing test does not prove production deployment. Link exact revision, test report, and release artifact where applicable. Label missing evidence and known limitations.

## 7. Security-sensitive entries

Avoid publishing exploitable details, secrets, tokens, personal data, or sensitive incident information. Follow the approved disclosure process. Public notes should communicate impact and remediation safely; detailed incident evidence belongs in access-controlled records.

## 8. Compatibility and migration notes

For breaking changes, state affected consumers, prerequisites, migration steps, compatibility window, data/schema effects, rollback or forward-recovery guidance, and support status. Link the relevant API/database/decision records.

## 9. Review workflow

1. Collect change records from reviewed work.
2. Check each claim against code, tests, and release evidence.
3. Link feature/decision IDs and the source revision.
4. Check security/privacy disclosure.
5. Obtain release-owner review.
6. Publish only with the corresponding approved release.

## 10. Integrity checks

Detect duplicate release headings, missing dates/status, references to unknown versions or commits, unreleased entries marked shipped, claims of fixes without evidence, missing migration notes for breaking changes, and mismatched changelog/version-history records.

## 11. Repository baseline

The repository contains a documentation changelog draft and a Git history, but this specification does not treat documentation commits as software releases. Each actual release must be established by its approved version and artifact evidence.

## 12. Required verification tests

- Entries follow the agreed format and newest-first order.
- Unreleased work is not described as shipped.
- Each released entry links to a valid release record.
- Claims are supported by change/test evidence.
- Breaking changes include migration/compatibility notes.
- Security notes do not disclose secrets or restricted details.
- Changelog and Version History agree on release identity and status.

## 13. Acceptance criteria for this specification

- The project owner approves the categories and release-promotion rules.
- The format aligns with Version History and Release Process.
- Documentation-only work is distinguishable from software delivery.
- The current unreleased section is reconciled with reviewed changes.
- Integrity checks and evidence requirements are defined.

## 14. Current status and limitations

- Specification content: draft prepared for review.
- Changelog process automation: NOT VERIFIED.
- Software release status: NOT VERIFIED by this document.
- Production: NOT VERIFIED.

This document does not claim that a release has occurred merely because changelog text exists.

## 15. Unreleased documentation and project-control change record

### Unreleased — documentation and project-control changes only

- 2026-11-23: Added per-service capability/evidence/coverage/compliance/owner/content/publish controls for all 71 candidate catalogue entries, plus a strict read-only validator and unit tests. All entries remain blocked pending real owner evidence. Documentation-only; no service launch is claimed.

- 2026-11-21: Added owner-directed 71-entry comprehensive candidate pest-control catalogue; separated allied services and retained capability, legal, safety, and publication verification gates. Updated OI-02 and requirements/matrix/roadmap records. Documentation-only; no service availability or software release is claimed.

The following verified repository revisions are documentation/control changes, not software releases (newest first):

- `34e9281` — reconciled the source-confirmed legal/business identity (`WREQ-C-001`) with the OI-01 public-brand approval boundary; see Milestone 69.
- `60e6bec` — reconciled lifecycle status headers for Specifications 01–30 with the semantic-review matrix and refreshed the current progress snapshot.
- `a30749d` — recorded the final documentation verification revision and owner-acceptance boundary.
- `0f2b457` — reconciled BI-BUGS documentation acceptance gates, stale lifecycle-header wording, owner-input conversion rules, and roadmap status.

- `06c0077` — finalized the document review baseline, owner-input register, requirement-record schema, and internal package/owner-acceptance distinction.

- `a84c4a0` — reconciled supporting documentation, legacy architecture summaries, roadmap views, and the auxiliary completion matrix.
- `f5f247b` — reviewed the Master Index, Constitution, Digital DNA, website requirements, and lifecycle standard.
- `d103fe3` — defined evidence-based population gates for feature, module, API, database, and AI registries.
- `c2fe0c6` — reviewed UI/UX, testing, decision, idea, changelog, version-history, and long-range roadmap controls.
- `d500146` — reviewed and clarified Living Blueprint, Engineering Rules, Project Structure, and Folder Architecture for BI-BUGS scope and repository evidence.
- `98949c3` — added the Documentation Completion Matrix and semantic-review backlog.
- `f9550bb` — synchronized verified BI-BUGS documentation and the limited static website foundation; included documentation, validators, tests, and frontend shell.

These entries describe source-control changes only. They do not claim a released application artifact, production website, backend, database, or deployed business workflow. The changelog must be updated from verified commits and approved release records; do not move an entry from Unreleased to a versioned release section until the release process has produced an identifiable approved artifact.

**Current baseline:** No software release version or release artifact is established by the above commits. The inspected local Git tag inventory contained no tags at the time of review; confirm remote tags and any external releases separately before a future release declaration.


## Unreleased — 2026-11-23 — Geographic selector requirement (documentation only)

- Added owner-approved requirement `WREQ-GEO-001` for all-India States/UTs and city selection plus a separate International/World country selector.
- Recorded decision `DEC-BBE-003` and partially resolved OI-03 for selector scope only.
- Actual BI-BUGS service coverage, exclusions and public contact details remain unconfirmed; no nationwide/worldwide availability claim or website feature implementation is implied.


## Unreleased — 2026-11-23 — Initial owner-declared active areas and contact inputs

- Recorded initial active-area declarations for Chambal region, Gwalior, Bhopal, Indore, Jaipur, Jaisalmer and Agra; two ambiguous names retained verbatim pending clarification.
- Recorded Morena as head-office city only and owner-provided public phone/email details. Other India and international locations remain inactive pending future owner activation.
- Per-service availability gate remains mandatory; no website code or precise address was implemented.


## Unreleased — 2026-11-23 — Owner-confirmed active division/district selections

- Added owner-selected Madhya Pradesh divisions Chambal, Gwalior, Bhopal and Indore and all 21 districts within them; added Rajasthan Dholpur while retaining prior Jaipur, Jaisalmer and Agra selections.
- Recorded DEC-BBE-005 and Specification 31 Section 23, using official government administrative listings for district mapping.
- Other India and international locations remain inactive by default; per-service availability approvals remain separate. Documentation-only; no website UI or service coverage claim is implemented.


## Unreleased — 2026-11-23 — Owner-provided Morena head-office address

- Captured the owner-supplied address text: Near Railway Station, Manohar Nagar, Tussi Pura, Morena, Madhya Pradesh 476001.
- Recorded decision `DEC-BBE-006` and updated website requirements, discovery workbook, progress, completion matrix and roadmap.
- No map pin/coordinates or geocoded location inferred. Documentation-only; no frontend or map integration implemented.


## Unreleased — 2026-11-23 — Location catalogue governance and validation

- Added Specification 35 and canonical `LOCATION_AREA_REGISTER.json` for 25 owner-selected districts, with separate India/International selector scope and inactive-by-default controls.
- Added strict read-only `scripts/validate_location_register.py` and unit tests; expanded lifecycle audit scope to numbered Specifications 01–35.
- Full authoritative India/world datasets, per-service coverage evidence, owner acceptance and frontend implementation remain open. Documentation/project-control change only.


## Unreleased — 2026-11-23 — India and International location reference datasets

- Imported official LGD hierarchy for 36 States/UTs and 770 districts; imported UN M49 248 country-or-area entries (247 International); imported GeoNames India 549,031 active populated-place records.
- Added source manifest/checksums, attribution/license boundaries, explicit crosswalk limitations, reproducible importer and strict catalogue validator/tests.
- Official LGD ULB/city-only cross-check, final owner selector approval, service coverage and frontend implementation remain open. Documentation/data import only; no public website release or service availability claim.
