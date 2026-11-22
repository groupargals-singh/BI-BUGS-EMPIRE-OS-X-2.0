# BI-BUGS EMPIRE OS-X 2.0 — VERSION HISTORY

**Specification ID:** BBEOSX-MS-28
**Status:** REVIEWED — OWNER ACCEPTANCE PENDING
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related:** `19_PROJECT_MEMORY.md`, `25_DECISION_REGISTRY.md`, `27_CHANGELOG.md`, `29_RELEASE_PROCESS.md`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose

Maintain an authoritative history of software release identities and their status, scope, compatibility, verification, approval, deployment and rollback evidence. This record distinguishes source-control commits from software versions and deployed artifacts.

A commit is not automatically a release. A tag or version label is not proof of deployment or successful operation.

## 2. Required version record

Each release record should include:
- semantic version or explicitly identified pre-release version;
- lifecycle status and release date;
- source commit and signed/approved tag where supported;
- artifact identity, checksum/provenance and build environment;
- scope and linked changelog entries;
- compatibility, API/schema changes and migration requirements;
- security/dependency notes and known issues;
- test suite/revision, commands, results and evidence links;
- release owner, approval and release process record;
- deployment environment/status and health verification when deployed;
- rollback or forward-recovery procedure and evidence;
- predecessor/successor and support/deprecation status.

Unknown fields must remain pending; do not infer deployment from a commit.

## 3. Versioning policy

Use Semantic Versioning where applicable:
- **MAJOR:** incompatible public contract changes;
- **MINOR:** backward-compatible functionality;
- **PATCH:** backward-compatible fixes;
- **Pre-release:** a clearly labelled candidate or preview that is not equivalent to a final release.

The project owner must approve the actual versioning policy and compatibility promises. Documentation-only commits do not automatically increment the software version.

## 4. Lifecycle

Suggested states:
- `PLANNED`
- `CANDIDATE`
- `VERIFIED`
- `APPROVED`
- `RELEASED`
- `DEPLOYED`
- `ROLLED_BACK`
- `WITHDRAWN`
- `UNSUPPORTED`

Transitions require a timestamp, actor, reason, source revision and evidence. `RELEASED` means an approved artifact was published. `DEPLOYED` means that artifact was installed in a named environment and deployment/health checks were recorded. Do not combine these states.

## 5. Source and artifact provenance

Record the exact source commit, build command/environment, dependency lock state where applicable, artifact filename/identifier, checksum, and build logs. Where reproducible builds or signed provenance are available, retain the verification result. Never replace a released artifact silently while retaining the same identity.

## 6. Verification and release gates

A candidate should pass required unit, component, integration, end-to-end, security, accessibility, performance, migration and recovery tests according to scope/risk. Record skipped tests and reasons. A release gate must fail closed when required evidence or approval is missing. A green build alone is not a complete release gate.

## 7. Deployment and rollback

Record deployment environment, configuration revision, migration status, health checks, monitoring, and post-deployment validation. Define rollback/forward-recovery prerequisites, data compatibility, and responsible owner. Rollback success requires evidence; a documented plan alone is not proof that rollback works.

## 8. Support and deprecation

For each released version, record supported status, maintenance window when approved, security update policy, known issues, upgrade path and end-of-support date when known. Deprecation requires a notice, migration guidance, and replacement or end-of-life decision.

## 9. Incident and withdrawal handling

If a release is withdrawn or rolled back, preserve its record and document the reason, affected environments, impact, remediation, and follow-up tests. Do not delete release history. Security incidents must follow the approved disclosure and access-control process.

## 10. Reconciliation with changelog and Git

Version History, Changelog, tags, source commits, build artifacts and deployment records must agree on version identity and status. Mark a commit as documentation-only when relevant. If the repository lacks artifact or deployment evidence, state that release/deployment status is not verified.

## 11. Integrity checks

Detect duplicate versions, missing source commit/artifact identity, invalid lifecycle transitions, release entries without changelog links, deployment claims without environment evidence, missing test/approval evidence, and rollback claims without test records.

## 12. Required verification tests

- Version identifiers are unique and follow the approved scheme.
- Every release maps to a source revision and identifiable artifact.
- Candidate/release/deployment states are distinct.
- Required release gates block missing tests or approval.
- Changelog, Git tags and Version History agree.
- Deployment status includes environment and health evidence.
- Rollback/forward recovery is tested for releases that require it.
- Withdrawn versions retain their history and incident links.

## 13. Initial repository baseline

The inspected Git history includes documentation commits such as `4a63ff3` (“Add testing architecture specification”). This is a repository commit, not evidence of a software release. No application build artifact or deployment record was found in the tracked-file inventory for this audit.

## 14. Acceptance criteria for this specification

- The project owner approves the versioning and lifecycle rules.
- Changelog and Release Process requirements are consistent.
- Artifact, test, approval, deployment and rollback evidence are defined.
- Documentation changes cannot be misreported as shipped software.
- Existing tags/releases are reconciled before declaring a complete version history.

## 15. Current status and limitations

- Specification content: draft prepared for review.
- Complete software version inventory: NOT VERIFIED.
- Build artifact history: NOT VERIFIED.
- Deployment history: NOT VERIFIED.
- Production: NOT VERIFIED.

This document does not claim that a software release or deployment has occurred.

## 16. Verified repository baseline — 2026-11-19

This is a source-control baseline record, not a software release:

- Branch: `main`
- Latest inspected commit: `d500146ef4234862f11fc49d13b7eae4115aa33d` — `Review BI-BUGS blueprint and structure specifications`
- Earlier documentation/control commits in this reviewed sequence: `98949c3` and `f9550bb`.
- Local Git tag inventory at review time: no tags listed.
- Tracked release/build artifact inventory: no application release artifact identified; `deployment/.gitkeep` is a placeholder, not a deployment artifact.
- Production deployment: NOT VERIFIED.

A complete remote release/tag inventory and any releases/deployments performed outside this repository require owner confirmation. Do not infer that none exist outside the inspected repository. Do not assign a semantic software version to documentation commits. A future release record must identify an approved artifact, source revision, tests, approval, target environment, deployment health evidence, and rollback/recovery evidence where applicable.

**Review result:** Repository source-control baseline is recorded with evidence boundaries. No software release is declared.


## 17. Documentation-only source-control revisions after initial baseline

The following verified `main` revisions extend the source-control history recorded in Section 16. They are documentation/project-control commits, not semantic software versions, release artifacts, or deployments:

- `c2fe0c6` — BI-BUGS UX, testing, and governance record review.
- `d103fe3` — BI-BUGS registry population gates.
- `f5f247b` — BI-BUGS governance and website requirements review.
- `a84c4a0` — supporting documentation and roadmap reconciliation.

No software release is declared by these commits. Recheck Git history, remote tags, artifacts, and owner-provided external release records before preparing any actual software release entry.


## 18. Documentation-only source-control revisions — 2026-11-20

- `0f2b457` — reconciled BI-BUGS documentation acceptance gates, lifecycle headers, owner-input conversion rules, and roadmap status.
- Classification: documentation/project-control only; not a semantic software version, release artifact, or deployment.
- Remote `main` was verified at `0f2b4570d79394b053516cbdc5d191f99efa3ac8`.
- Evidence boundary: internal documentation package can be presented for owner review; OI-01–OI-11 and explicit owner acceptance remain open.

## 19. Earlier documentation-only source-control revision — 2026-11-19

- `06c0077` — finalized BI-BUGS documentation review and owner-input gates.
- Classification: documentation/project-control only; not a semantic software version, release artifact, or deployment.
- Evidence boundary: internal documentation package can be presented for owner review; OI-01–OI-11 and explicit owner acceptance remain open.

## 20. Lifecycle review status reconciliation — 2026-11-21

- `60e6bec` — reconciled lifecycle status headers for Specifications 01–30 with the evidence-based semantic-review matrix; refreshed current progress and audit records.
- Classification: documentation/project-control only; not a semantic software version, release artifact, or deployment.
- Remote `main` verified at `60e6bece392a6f7bcaf2ceb1249cd603c59ac06b`.
- Evidence boundary: owner inputs OI-01–OI-11, approved requirements, requirement-level traceability, and explicit owner acceptance remain open.

## 21. Source-backed company identity reconciliation — 2026-11-21

- Documentation-only update: Specification 32 now records the legal/business identity from WREQ-C-001 as source-confirmed while retaining public display and brand approval as pending. Specification 31 and the completion matrix clarify this boundary.
- Classification: documentation/project-control only; not a semantic software version, release artifact, or deployment.
- Repository revision: `34e92812ec7758c43313c612899eef41da4e72f9`, pushed to and verified on remote `main`.


## 22. Comprehensive candidate pest-control catalogue — 2026-11-21

- Documentation-only change: recorded the owner's direction to include a comprehensive pest-control service catalogue; Specification 32 Section 4 contains 71 candidate entries and Specification 31 records the approval boundary.
- OI-02 is partially resolved for catalogue breadth only; individual service availability, capability, permissions, safety and public claims remain pending.
- Classification: documentation/project-control only; not a software version, service launch, release artifact, or deployment.
- Git revision and remote status: to be recorded after verification and push.


## 23. Per-service catalogue approval controls — 2026-11-23

- Added per-service delivery model, evidence, coverage, compliance/safety, owner approval, public-content approval and publication status fields to all 71 candidate entries.
- Added strict read-only validator `scripts/validate_service_catalogue.py` and unit tests `testing/test_validate_service_catalogue.py`.
- All entries remain blocked by default; validation does not establish actual service availability or approve claims.
- Documentation/project-control change only; not a software release or deployment. Git revision to be recorded after push.


## 24. Geographic selector scope decision — 2026-11-23

- Documentation-only change: owner approved all-India States/UTs and city selection plus a separate International/World country selector; recorded as DEC-BBE-003 / WREQ-GEO-001.
- OI-03 is partially resolved for selection scope only. Actual service coverage and public contact details remain open.
- No application feature, software release, nationwide service claim or international operation is declared. Commit `95eb1c9c3e3258648227a14b873140c444ac5117` (`Record India and international location selector scope`) pushed to `origin/main`; exact remote `main` hash verified after fetch. This is a documentation-only revision.


## 25. Initial active-area and contact owner inputs — 2026-11-23

- Captured owner-declared active areas, inactive default for all other India/world locations, Morena head-office city, and public phone/email details.
- `Sambhav`, `Bolpur`, Chambal boundary and exact Morena address remain pending clarification. Per-service publication approvals remain mandatory.
- Documentation-only change; website implementation not started. Commit `2630bffe2f253e15e8b482cf14bb16a4806013e0` (`Record initial BI-BUGS active areas and contacts`) pushed to `origin/main`; exact remote hash verified after fetch.


## 26. Owner-confirmed division and district selections — 2026-11-23

- Documentation-only update: recorded all districts under the owner-selected Madhya Pradesh divisions Chambal, Gwalior, Bhopal and Indore (21 districts), plus Rajasthan Dholpur; prior Jaipur, Jaisalmer and Agra selections remain.
- Added decision `DEC-BBE-005`, updated OI-03, requirements, progress and roadmap. Official administrative references are linked in Specification 31 Section 23.
- Classification: documentation/project-control only; no frontend implementation, service availability, software release or deployment is claimed.
- Git revision: `8c61424fd1f82329f899d8366b0b2a3b60864c97` (`Record selected MP divisions and Dholpur district`) pushed to `origin/main`; exact local/remote `main` hash verified. This is a documentation-only revision.


## 27. Owner-provided Morena head-office address — 2026-11-23

- Documentation-only update: captured owner-supplied head-office address text, “Near Railway Station, Manohar Nagar, Tussi Pura, Morena, Madhya Pradesh 476001”, under `DEC-BBE-006`.
- Map pin/coordinates remain unknown; no geolocation or map integration is claimed.
- Classification: documentation/project-control only; no frontend implementation, software release or deployment.
- Git revision: `cbad6a7` (`Record Morena head office address input`) pushed to `origin/main`; exact local/remote `main` hash verified. This is a documentation-only revision.


## 28. Location catalogue governance and validation — 2026-11-23

- Added Specification 35, canonical owner-area JSON register, strict location-register validator and unit tests.
- Expanded lifecycle metadata audit scope from Specifications 01–34 to 01–35.
- Classification: documentation/project-control only; no full India/world selector dataset, frontend implementation, service availability, software release or deployment is claimed.
- Git revision: `4cf0b97cf8401d9dd376a5ad5b07eee9c3c3d663` (`Add governed location register and validation`) pushed to `origin/main`; exact local/remote `main` hash verified. This is a documentation/project-control revision, not a software release.


## 29. India and International location reference-data snapshot — 2026-11-23

- Added LGD State/UT/district snapshot (36 States/UTs; 770 districts), UN M49 country/area catalogue (248 entries; 247 International), and GeoNames India populated-place index (549,031 records).
- Added manifest, source attribution/license/limitations, reproducible importer, strict validator and tests; reconciled Specification 35, progress, roadmap and matrix.
- Classification: documentation/reference-data only; GeoNames is not a city-only official municipal list. LGD ULB cross-check, owner selector approval, service coverage, frontend implementation, software release and deployment remain unapproved/not implemented.
- Git revision: `03cd4a93fd7dcad1c00e628250176f5c2c33478a` (`Import validated India and international location data`) pushed to `origin/main`; exact local/remote `main` hash verified. This is a documentation/reference-data revision, not a software release.
