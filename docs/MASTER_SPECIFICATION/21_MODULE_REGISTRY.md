# BI-BUGS EMPIRE OS-X 2.0 — MODULE REGISTRY

**Specification ID:** BBEOSX-MS-21
**Status:** REVIEWED — OWNER ACCEPTANCE PENDING
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related specifications:** `03_MASTER_BLUEPRINT.md`, `06_ENGINEERING_RULES.md`, `07_PROJECT_STRUCTURE.md`, `08_FOLDER_ARCHITECTURE.md`, `18_TESTING.md`, `19_PROJECT_MEMORY.md`, `20_FEATURE_REGISTRY.md`, `22_API_REGISTRY.md`, `23_DATABASE_REGISTRY.md`, `24_AI_REGISTRY.md`, `25_DECISION_REGISTRY.md`

---

## 1. Purpose

Define a canonical inventory of logical software modules, their responsibilities, ownership, boundaries, interfaces, dependencies, data ownership, lifecycle, and verification evidence.

A directory is not automatically a functioning module. A module is considered implemented only when its code and required configuration exist; it is verified only when defined tests pass on an identified revision.

## 2. Scope

The registry covers application modules, infrastructure adapters, shared libraries, AI components, background workers, integration adapters, security controls, observability, and deployment components. It records links to canonical design documents and code rather than duplicating their full contents.

## 3. Required module record

Every module record MUST contain:
- unique stable `MOD-####` ID, name, purpose, and user/system outcome;
- lifecycle and verification status;
- owner and responsible team/person;
- canonical repository path and public entry points;
- responsibilities, explicit exclusions, and trust boundary;
- public interfaces, events, APIs, and contracts;
- upstream dependencies and downstream consumers;
- data ownership, persistence, retention, and classification;
- configuration, secret references, and permission requirements;
- expected failure modes, timeouts, retry behavior, and recovery;
- logging, metrics, tracing, and audit requirements;
- unit/component/integration test paths and acceptance evidence;
- related features, decisions, specifications, and change records;
- version/commit, last review, blockers, and next action.

Unknown values must be marked unknown or pending rather than invented.

## 4. Identifier and ownership rules

- Assign IDs centrally and never recycle them.
- Every module has one accountable owner, even if several teams contribute.
- Shared modules require a documented support and change policy.
- File paths may change; the stable module ID remains unchanged.
- Splits, merges, renames, and replacements must preserve predecessor/successor links.

## 5. Lifecycle

Allowed states:
- `PROPOSED`
- `DESIGNED`
- `READY`
- `IN_PROGRESS`
- `IMPLEMENTED_UNVERIFIED`
- `VERIFIED`
- `RELEASED`
- `BLOCKED`
- `DEPRECATED`
- `RETIRED`

A state change must record actor, time, reason, previous/new status, and evidence. `VERIFIED` requires module-specific passing tests. `RELEASED` requires a traceable release. A design document alone cannot promote a module to implemented or verified.

## 6. Module boundary contract

Each module must declare:
- what it owns and what it does not own;
- the only supported ways other modules may call it;
- the data it may read or mutate;
- the permissions required for privileged operations;
- error formats and failure behavior;
- version and compatibility expectations;
- how it can be tested in isolation;
- what happens when a dependency is unavailable.

Consumers must not bypass a module's public interface to write directly to its internal data or state unless an approved architecture decision explicitly permits it.

## 7. Dependency rules

- Dependencies must be explicit, justified, and versioned where applicable.
- Avoid cyclic dependencies; any exception requires a documented decision and mitigation.
- Keep dependency direction consistent with the Master Blueprint and Engineering Rules.
- External services need timeouts, bounded retries, error mapping, and fallback/abort behavior.
- Optional dependencies must fail safely when absent.
- A dependency graph should identify critical paths and single points of failure.

## 8. Data and transaction ownership

Each module must name its canonical data owner. Cross-module data changes must use an approved interface or event/transaction pattern. Define consistency, idempotency, concurrency, validation, and compensation behavior for multi-step operations. Do not duplicate authoritative state without a reconciliation strategy.

## 9. Security and trust boundaries

Module records must identify untrusted inputs, external calls, privilege boundaries, secrets, sensitive data, and audit obligations. Enforce permissions in application code and infrastructure; documentation or AI prompts alone are not a security boundary. Validate input at trust boundaries, use least privilege, and redact secrets from errors/logs.

## 10. Configuration and secrets

Configuration must be schema-validated and environment-specific values separated from code. Secret records must contain references to an approved secret store, not the secret value itself. Document safe defaults, missing/invalid configuration behavior, rotation requirements, and startup checks.

## 11. Reliability and observability

Define health/readiness behavior, timeouts, cancellation, retries with limits, backoff, idempotency, graceful shutdown, resource limits, and recovery. Logs and metrics must make failures diagnosable without leaking sensitive data. Background workers must define queue semantics, retry/dead-letter behavior, and duplicate-work handling where applicable.

## 12. Testing strategy

Each module should have:
- unit tests for core logic and edge cases;
- component tests for its public contract;
- integration tests for real dependency boundaries;
- authorization and invalid-input tests;
- failure/retry/recovery tests where applicable;
- performance/resource tests for critical or high-load modules;
- regression tests for previously fixed defects.

Test evidence records revision, command, environment, time, result, and artifact location.

## 13. Repository baseline

Historical baseline: during the original audit these directories contained only `.gitkeep` placeholders. Current inventory (2026-11-19) contains a static frontend shell plus documentation validators and tests. These are limited website-foundation/project-control files, not completed business modules. `backend/`, `database/`, `cloud/`, `ai-core/`, `mobile/`, `hardware/`, and `deployment/` still have no verified product implementation. Registry records must be based on approved design and actual implementation.

## 14. Registry integrity checks

Checks should detect:
- duplicate/malformed module IDs;
- missing owner, purpose, status, or canonical path;
- non-existent code/test references;
- unrecorded or cyclic dependencies;
- undocumented public interfaces;
- modules with multiple conflicting data owners;
- missing permission/trust-boundary declarations;
- `VERIFIED` modules without passing test evidence;
- `RELEASED` modules without release references;
- stale ownership or verification records.

A path that exists but contains only a placeholder must be reported as a placeholder, not as an implemented module.

## 15. Change and deprecation policy

Changes to module responsibility, interface, data ownership, dependencies, security boundary, or lifecycle require impact analysis and a linked decision/change record. Update consumers, contracts, tests, and documentation together. Deprecation requires a replacement or explicit end-of-life plan, migration guidance, support window where applicable, and removal criteria.

## 16. Required verification tests

- IDs and lifecycle values are unique and valid.
- Module ownership and boundaries are explicit.
- Dependency references resolve or are clearly marked external/pending.
- Cycles and undeclared dependencies are detected.
- A module cannot become verified without passing evidence.
- Placeholder directories are not counted as implemented modules.
- Unauthorized access and cross-module writes are rejected by the implemented system.
- Failures, retries, timeouts, and recovery follow the module contract.
- Deprecation and migration links remain traceable.

## 17. Acceptance criteria for this specification

- The project owner reviews the record schema, lifecycle, and boundary rules.
- Module lifecycle is consistent with the Feature, API, Database, AI, Testing, and Release specifications.
- Repository inventory is reconciled with each proposed module record.
- No planned module is described as implemented without code evidence.
- Critical modules have explicit owner, dependency, security, and test requirements.
- Open architecture decisions and blockers are linked to the Decision Registry.

## 18. Current status and limitations

- Specification content: draft prepared for review.
- Implementation: NOT STARTED / NOT VERIFIED.
- Automated registry validation: NOT RUN.
- Production: NOT VERIFIED.

This document does not claim that a module registry service or any application module is implemented or verified.

## 19. BI-BUGS initial module inventory and population gate

**Initial verified product-module inventory: NO PRODUCT MODULE RECORDS POPULATED.** Repository folders such as `frontend/`, `backend/`, `database/`, `ai-core/`, `cloud/`, `deployment/`, `mobile/`, and `hardware/` are organizational boundaries, not proof of functioning modules. The current frontend shell has not yet been decomposed into owner-approved product modules or domain ownership boundaries.

Do not create module IDs solely to mirror directory names. A module record requires a defined BI-BUGS responsibility, approved requirement(s), accountable owner, public/internal interfaces, dependency direction, data ownership, security boundary, lifecycle, test evidence, and change/deprecation policy. A module may be recorded as planned only when its need and scope are accepted; it must not be described as implemented without code evidence.

**Review result:** Registry schema and directory-versus-module distinction reviewed. Empty baseline is intentional until requirements and architecture select actual modules; owner acceptance remains pending.
