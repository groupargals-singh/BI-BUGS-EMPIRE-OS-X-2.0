# BI-BUGS EMPIRE OS-X 2.0 — FEATURE REGISTRY

**Specification ID:** BBEOSX-MS-20
**Status:** DRAFT FOR REVIEW
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related specifications:** `03_MASTER_BLUEPRINT.md`, `06_ENGINEERING_RULES.md`, `18_TESTING.md`, `19_PROJECT_MEMORY.md`, `21_MODULE_REGISTRY.md`, `22_API_REGISTRY.md`, `25_DECISION_REGISTRY.md`, `27_CHANGELOG.md`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose

Define the authoritative catalogue of user-facing capabilities and system features, including their ownership, scope, dependencies, lifecycle, acceptance criteria, implementation references, and verification evidence.

A feature record describes intended or observed capability. A feature name, folder, design document, or roadmap entry is not proof that the feature works.

## 2. Scope

The registry covers product capabilities, operational capabilities, security controls, AI capabilities, integrations, administrative functions, and cross-cutting platform behavior. It links to detailed specifications rather than copying their full content.

## 3. Required feature record

Every feature MUST have:
- unique, stable `FEAT-####` identifier;
- canonical name and concise user outcome;
- problem statement and target users/actors;
- scope, explicit exclusions, and assumptions;
- priority and business/security impact;
- lifecycle status and status-change history;
- owning module and accountable owner;
- dependencies, consumers, APIs, data entities and related features;
- functional and non-functional requirements;
- measurable acceptance criteria and failure behavior;
- security, privacy, accessibility and operational considerations;
- source paths, related specification IDs and decision IDs;
- implementation references and version/commit when available;
- test paths, commands, latest result and evidence references;
- blocker, next action, review date and release reference when applicable.

Unknown fields must be marked unknown or pending; they must not be fabricated.

## 4. Identifier and naming rules

- Allocate identifiers centrally and never reuse an ID, including after rejection or deprecation.
- Keep names stable and human-readable; rename through a recorded change.
- Maintain aliases only when needed for backward compatibility or search.
- Do not use a file path as the feature's sole identity because paths can change.
- Link split or merged features to their predecessor/successor records.

## 5. Lifecycle

Permitted lifecycle values:
- `PROPOSED`
- `UNDER_REVIEW`
- `APPROVED`
- `IN_DESIGN`
- `READY`
- `IN_PROGRESS`
- `IMPLEMENTED_UNVERIFIED`
- `VERIFIED`
- `RELEASED`
- `BLOCKED`
- `DEPRECATED`
- `REJECTED`

Status definitions:
- **PROPOSED:** idea exists but has not been approved.
- **APPROVED:** authorized scope and value are accepted.
- **IN_DESIGN / READY:** design or acceptance requirements are being completed / are actionable.
- **IN_PROGRESS:** implementation work has started.
- **IMPLEMENTED_UNVERIFIED:** code exists, but acceptance evidence is incomplete.
- **VERIFIED:** defined acceptance criteria have passing, current evidence.
- **RELEASED:** verified capability is included in a traceable approved release.
- **BLOCKED:** a named dependency or issue prevents progress.
- **DEPRECATED / REJECTED:** not intended for new use / not accepted.

## 6. Transition controls

Every material transition records the previous state, new state, actor, timestamp, reason, and evidence. `VERIFIED` requires passing acceptance tests on an identified revision. `RELEASED` requires a release record and approval. A failure returns the feature to an appropriate unverified or blocked state without deleting history.

## 7. Priority and risk

The project owner must define the priority scale and apply it consistently. Each feature should include impact, urgency, confidence, implementation effort, and risk. Security, privacy, data integrity, user authority, and recovery requirements cannot be waived merely to raise delivery priority.

## 8. Dependencies and traceability

Record upstream dependencies, downstream consumers, interfaces, data ownership, configuration, and failure behavior. Dependencies must link to canonical module/API/database/AI records. Cycles and undocumented cross-module writes must be flagged for architecture review.

Traceability should connect:
requirement → feature → module/API/data → decision → implementation change → test/evidence → release.

## 9. Acceptance criteria

Acceptance criteria must be specific, observable, testable, and linked to the user's intended outcome. Include positive behavior, invalid input, permission denial, failure/retry behavior, relevant boundary cases, and recovery behavior where applicable. Avoid vague criteria such as “works correctly” without a measurable condition.

## 10. Implementation and verification evidence

For implemented features record repository-relative paths and relevant symbols, commit/revision, test command, test environment, timestamp, result, and report/artifact location. Evidence must be reproducible where practical.

Do not infer implementation from a directory existing. Do not infer correctness from compilation alone. Do not infer production deployment from a local test. If evidence is missing, mark the feature `IMPLEMENTED_UNVERIFIED`, `BLOCKED`, or `NOT VERIFIED` as appropriate.

## 11. Change management

Scope, behavior, dependency, data, API, security, or acceptance changes require:
1. impact analysis;
2. linked decision/change record where material;
3. updated canonical specification and registry;
4. updated tests and migration notes when needed;
5. review and verification before status promotion.

Preserve the previous record revision and reason for change.

## 12. Reporting and stale records

The registry should support filtering by lifecycle, owner, priority, module, blocker, verification result, and release. Reports should identify:
- approved but not started features;
- work in progress and blockers;
- implemented but unverified features;
- verified but unreleased features;
- released features with stale or missing evidence;
- deprecated/rejected features and their replacements.

Recheck records when source files, dependencies, acceptance criteria, or releases change. Clearly display the last review/verification date.

## 13. Security and privacy

Feature records must identify trust boundaries, required permissions, data sensitivity, external data sharing, audit needs, abuse cases, and sensitive failure modes. Never store credentials in registry records. High-impact features require security review and explicit authorization rules in implementation, not only prompt instructions.

## 14. Registry integrity checks

Automated or manual checks should detect:
- duplicate or malformed feature IDs;
- missing required fields;
- invalid lifecycle values or transitions;
- broken specification/source/test references;
- missing acceptance criteria for approved features;
- a `VERIFIED` state without evidence;
- a `RELEASED` state without release reference;
- unresolved blockers on features marked ready;
- orphaned features and dependency cycles;
- stale records and conflicting status claims.

## 15. Required verification tests

- Every record has a unique stable ID and valid status.
- Status promotion is rejected if required evidence is absent.
- Every approved feature has a defined scope and testable acceptance criteria.
- Source/test references resolve or are explicitly marked pending.
- Dependency links point to known records or documented external dependencies.
- Duplicate IDs and invalid lifecycle values are reported.
- Released features link to an approved release record.
- Historical revisions remain traceable after changes.

## 16. Initial repository baseline

Historical baseline: at the time of the original draft review, the implementation directories contained only `.gitkeep` placeholders. Current inventory (2026-11-19) now includes a limited static website shell in `frontend/`, two documentation validators in `scripts/`, and their project-control tests in `testing/`. These are not business features or production workflows. No backend, API, database, AI, booking, payment, or deployed feature is verified. The feature catalogue must be populated from owner-approved requirements and reconciled against actual code as implementation proceeds.

## 17. Acceptance criteria for the specification

- The project owner reviews the schema, lifecycle, and priority policy.
- Feature IDs and lifecycle values are consistent with the Module, API, Database, AI, Decision, and Progress registries.
- Verification and release status definitions are consistent with the Testing and Release specifications.
- Initial feature records are sourced from approved requirements, not invented functionality.
- Unresolved decisions and blockers are explicitly recorded.

## 18. Current status and limitations

- Specification content: draft prepared for review.
- Implementation: NOT STARTED / NOT VERIFIED.
- Registry automation: NOT RUN.
- Production: NOT VERIFIED.

No live feature catalogue or functioning registry service is claimed by this document.
