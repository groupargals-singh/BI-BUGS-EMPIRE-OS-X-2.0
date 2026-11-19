# BI-BUGS EMPIRE OS-X 2.0 — DATABASE REGISTRY

**Specification ID:** BBEOSX-MS-23
**Status:** DRAFT FOR REVIEW
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related:** `09_DATABASE_ARCHITECTURE.md`, `15_SECURITY.md`, `18_TESTING.md`, `19_PROJECT_MEMORY.md`, `20_FEATURE_REGISTRY.md`, `21_MODULE_REGISTRY.md`, `22_API_REGISTRY.md`, `25_DECISION_REGISTRY.md`, `29_RELEASE_PROCESS.md`

---

## 1. Purpose

Maintain a canonical inventory of persistent data entities, tables, collections, indexes, schemas, migrations, data flows, and recovery obligations. The registry identifies who owns data and how integrity, access, retention, and restoration are verified.

This document defines requirements, not an existing database deployment.

## 2. Scope

Include relational and non-relational stores, files used as durable records, object/blob storage, caches when they affect correctness, search indexes, event stores, and migration/backup artifacts. Mark transient caches separately from authoritative data.

## 3. Required data record

Each record must include:
- stable `DATA-####` ID and canonical entity/table/collection name;
- purpose, lifecycle and verification status;
- owning module and accountable owner;
- schema fields, types, nullability, defaults and validation;
- primary/unique/foreign keys and integrity constraints;
- indexes, query patterns and performance assumptions;
- authoritative/source-of-truth status and downstream consumers;
- sensitivity classification, purpose, minimization and retention;
- access policy, encryption expectations and audit requirements;
- migration/version history and compatibility notes;
- deletion, correction, archival and legal/operational hold behavior;
- backup policy, recovery-point/time objectives and restore evidence;
- related APIs, features, decisions, tests and source paths;
- latest verification result, revision, review date and blocker.
Unknown schema or deployment details must be marked pending.

## 4. Data ownership and source of truth

Every authoritative entity has one owner. Replicas, caches, search indexes, and materialized views must identify their source and reconciliation strategy. Cross-module writes must go through approved contracts. Do not maintain competing sources of truth without a documented decision, conflict-resolution rule, and repair procedure.

## 5. Schema and integrity

Define types, nullability, defaults, constraints, referential integrity, uniqueness, ordering, timestamps, timezone semantics, and version fields. Validate input before persistence and enforce critical constraints at the storage boundary where possible. Define how partial writes and multi-record transactions behave.

## 6. Identifiers and time

Document ID format, uniqueness scope, generation method, collision handling, timestamp source, timezone, and ordering guarantees. Do not use local wall-clock timestamps as a unique identifier. For distributed operations, record enough metadata to order or reconcile events without assuming perfectly synchronized clocks.

## 7. Migrations and compatibility

Every schema migration needs a unique version, purpose, preconditions, expected changes, compatibility window, data transformation, validation, backup requirement, rollback or forward-recovery procedure, and test evidence. Test migrations on representative data before release. Avoid destructive changes until data backup and recovery are proven.

## 8. Privacy and security

Classify each field or entity. Collect only data needed for an approved purpose. Define read/write permissions, masking, encryption in transit/at rest where supported, key management, audit events, retention, deletion, and export restrictions. Credentials and secrets must not be stored in ordinary application records. Logs and backups require protection consistent with the data they contain.

## 9. Retention and deletion

Define retention duration or trigger, archival rules, deletion behavior, and treatment of replicas/backups/search indexes. Deletion must be auditable and must not be falsely reported complete when protected backups or downstream copies remain. Document any legally or operationally required holds and their approval process.

## 10. Transactions and concurrency

Specify transaction boundaries, isolation expectations, locking/version checks, optimistic concurrency, duplicate submission behavior, idempotency, and conflict responses. For distributed workflows, document consistency guarantees, outbox/inbox or equivalent patterns where needed, retries, and compensation for partial completion.

## 11. Indexes and performance

Link indexes to observed query patterns and expected scale. Measure query plans and latency with representative data before tuning. Avoid indexes that add unnecessary write cost. Define pagination, query limits, connection pools, timeouts, and resource ceilings for high-impact data paths.

## 12. Backup and recovery

Define backup frequency, protected destination, retention, encryption/access control, integrity checks, recovery-point objective (RPO), and recovery-time objective (RTO) for each critical dataset. These values must be approved for the real deployment, not invented in this specification. A backup is not verified until a restore drill succeeds and data integrity is checked.

## 13. Testing requirements

Test schema validation, constraints, duplicate records, malformed values, boundary values, concurrent updates, transaction rollback, migration/upgrade, backup/restore, retention/deletion, access denial, sensitive-data redaction, and recovery after dependency failure. Test with synthetic or approved representative data; do not expose production sensitive data in test logs.

## 14. Registry integrity checks

Detect duplicate IDs, missing owners, incomplete schema definitions, unresolved module/API links, undocumented sensitive fields, missing retention/access rules, migration gaps, conflicting source-of-truth declarations, and verified/released records without evidence. Distinguish an intended schema from a schema confirmed in a running database.

## 15. Repository baseline

The inspected repository currently has a `database/` directory containing only a `.gitkeep` placeholder and no tracked database implementation files. Therefore no live database, schema, migration, backup, or restore capability has been confirmed. Future entries must be reconciled against actual migrations and runtime configuration.

## 16. Required verification tests

- IDs and schema versions are unique and traceable.
- Required fields, constraints, and referential integrity behave as specified.
- Unauthorized access and prohibited cross-module writes are denied.
- Duplicate/concurrent writes have deterministic documented behavior.
- Migrations pass on representative data and recovery steps are tested.
- Backup integrity checks and restore drills pass.
- Retention/deletion behavior includes downstream copies as specified.
- Sensitive values are excluded or redacted from logs.
- `VERIFIED` or `RELEASED` requires current evidence and release references.

## 17. Acceptance criteria for this specification

- The project owner reviews ownership, classification, retention, and recovery policies.
- Rules align with Database Architecture, Security, Testing, API, and Release specifications.
- Every approved data entity has an owner and a declared source of truth.
- Critical datasets have approved recovery objectives and restore-test requirements.
- Migration and deletion behavior is defined before implementation is marked ready.
- Unknown deployment decisions remain explicitly pending.

## 18. Current status and limitations

- Specification content: draft prepared for review.
- Database/schema implementation: NOT VERIFIED.
- Migration tests: NOT RUN.
- Backup/restore: NOT VERIFIED.
- Production: NOT VERIFIED.

This document does not claim that a database or data registry service is implemented or verified.

## 19. BI-BUGS initial data inventory and population gate

**Initial verified application database inventory: NO DATABASE ENTITY OR SCHEMA RECORDS POPULATED.** No product database, schema, migration, or persistent customer/staff record store is verified in the current repository. Git-tracked project documentation and project-control records are not the application database.

Do not create data-entity IDs or define customer fields before the business purpose, collection channel, minimum necessary fields, privacy notice/consent where applicable, access roles, retention, correction/deletion, export, audit, backup, and recovery requirements are approved. A future schema record must link to the accepted requirement and data-flow/security review. Use synthetic test data unless a separately approved test-data process permits otherwise.

**Review result:** Registry schema and privacy-first population gate reviewed. Empty initial application-data inventory is intentional; owner approval and approved workflow requirements remain pending.
