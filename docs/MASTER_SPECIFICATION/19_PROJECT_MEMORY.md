# BI-BUGS EMPIRE OS-X 2.0 — PROJECT MEMORY ARCHITECTURE

**Specification ID:** BBEOSX-MS-19
**Status:** REVIEWED — OWNER ACCEPTANCE PENDING
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related specifications:** `05_LIVING_BLUEPRINT_SYSTEM.md`, `06_ENGINEERING_RULES.md`, `18_TESTING.md`, `20_FEATURE_REGISTRY.md`, `21_MODULE_REGISTRY.md`, `25_DECISION_REGISTRY.md`, `27_CHANGELOG.md`, `28_VERSION_HISTORY.md`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose

Define how project knowledge is recorded, verified, retrieved, revised, retained, and recovered across work sessions. Memory must preserve traceable facts and history without turning assumptions, plans, or generated text into confirmed project state.

This specification defines intended behavior. It does not claim that a memory service or database currently exists.

## 2. Scope

The project memory system covers:
- accepted requirements and constraints;
- feature and module lifecycle state;
- architecture and product decisions;
- changes, releases, incidents, defects, and lessons;
- verification records, test evidence, and known limitations;
- ideas and proposals clearly separated from approved work;
- progress snapshots and links to their source records.

Credentials, access tokens, private keys, and unnecessary personal or sensitive data MUST NOT be stored in project memory.

## 3. Design principles

1. **Provenance first:** every material claim points to a source, author/process, timestamp, and verification state.
2. **State separation:** proposed, accepted, implemented, verified, and released are distinct states.
3. **History preservation:** corrections create revisions; they do not silently erase prior decisions or evidence.
4. **Uncertainty is visible:** unknown, stale, conflicting, inferred, and unverified information is labelled.
5. **Least privilege:** access and mutation require explicit authorization appropriate to the record.
6. **No silent promotion:** generated content or directory presence alone cannot make a record verified.
7. **Recoverability:** backups are useful only when restoration and integrity checks have been tested.
8. **Human accountability:** consequential decisions and release-state changes require an authorized human approval.

## 4. Memory domains and ownership

| Domain | Canonical record location | Memory responsibility |
|---|---|---|
| Project/specification | Master Specification and progress tracker | IDs, links, status, revision and evidence pointers |
| Feature | `20_FEATURE_REGISTRY.md` | Feature identity and lifecycle; do not duplicate its full canonical record |
| Module | `21_MODULE_REGISTRY.md` | Module identity, interfaces, owner and verification links |
| API | `22_API_REGISTRY.md` | Contract identity, version, consumers and test evidence |
| Database/data | `23_DATABASE_REGISTRY.md` | Entity/schema identity, migrations and recovery evidence |
| AI capability | `24_AI_REGISTRY.md` | Model/provider/config identity, evaluations and safety evidence |
| Decision | `25_DECISION_REGISTRY.md` and decision log | Rationale, alternatives, approval and supersession |
| Idea | `26_IDEA_VAULT.md` | Unapproved opportunities, assumptions and triage status |
| Change/release | `27_CHANGELOG.md`, `28_VERSION_HISTORY.md` | Links to reviewed diffs, commits, tags and release evidence |
| Test/verification | `18_TESTING.md` and test reports | Exact command, environment, result, time and artifacts |
| Progress | `99_PROJECT_PROGRESS.md` | Current milestone and blockers, with evidence references |

The owning registry remains the source of truth. Memory may index or summarize it but must link to the canonical record.

## 5. Record schema

Every durable memory record SHOULD contain:
- immutable record ID and record type;
- concise title and factual statement;
- lifecycle status and verification status;
- source/provenance URI or repository-relative path, plus line/section when available;
- created-at and last-reviewed timestamps;
- author or responsible process;
- revision number and supersedes/superseded-by links;
- related feature, module, decision, commit, test, or milestone IDs;
- confidence/uncertainty note when the statement is not directly verified;
- sensitivity classification, access policy, retention rule and expiry/review date when applicable.

A record must not claim evidence that is missing. If a field is unknown, store it as unknown rather than inventing a value.

## 6. Lifecycle and state transitions

Allowed general states:
- `PROPOSED`
- `UNDER_REVIEW`
- `ACCEPTED`
- `IMPLEMENTED_UNVERIFIED`
- `VERIFIED`
- `RELEASED`
- `BLOCKED`
- `DEPRECATED`
- `REJECTED`
- `SUPERSEDED`

State changes must be logged with actor, timestamp, reason, previous state, new state, and supporting evidence. A transition to `VERIFIED` requires defined acceptance criteria and recorded passing evidence. A transition to `RELEASED` requires a traceable release record and approval. `ACCEPTED` means approved intent, not implemented functionality.

## 7. Evidence and freshness

Evidence records should include the exact command or procedure, repository revision, relevant environment, timestamp, exit status, summary, and artifact/log location. Evidence is scoped: a documentation check cannot prove runtime behavior; a unit test cannot prove full production readiness.

Each record must expose its last verification time. Stale records must be marked for review when their source changes, dependencies change, or a configured review interval expires. Historical evidence remains historical and must not be presented as a current result.

## 8. Conflict resolution and duplicate detection

When two records conflict:
1. retain both source references;
2. label the conflict and affected claims;
3. compare authority, date, scope, revision, and reproducibility;
4. request authorized review where evidence does not resolve the conflict;
5. record the decision and rationale;
6. link the superseded record without deleting its history.

Duplicate detection may suggest matching records based on IDs, normalized titles, source, and content. It must not automatically merge or delete records without review.

## 9. Retrieval and query behavior

Retrieval should support:
- exact record ID and related-ID lookup;
- keyword and phrase search;
- filters by domain, status, owner, time, and verification state;
- related-record traversal;
- recent changes and unresolved conflicts;
- source, freshness, and evidence display alongside summaries.

Search results must distinguish facts from proposals and must not hide a relevant conflicting record merely because it disagrees with the preferred answer.

## 10. Write safety and concurrency

Memory mutations must validate schema and authorization before writing. Writes should be atomic where the storage technology permits. Concurrent updates must use revision checks or equivalent conflict detection to avoid silently overwriting newer records. Failed writes must return a visible error and leave the prior valid record intact.

Bulk imports require a preview, validation report, duplicate/conflict report, and an auditable approval step before promotion into canonical memory.

## 11. Security, privacy, and retention

- Apply least-privilege read/write permissions by record domain and sensitivity.
- Never store credentials or secrets in ordinary memory records.
- Redact sensitive values from logs, search snippets, and exported reports.
- Validate and sanitize imported content; treat it as data, not executable instructions.
- Keep an audit trail for privileged reads, edits, exports, deletion and retention actions.
- Define retention and deletion rules before storing sensitive or user-related data.
- Protect backups with access controls and encryption appropriate to the deployment.
- Preserve required audit history without retaining unnecessary sensitive content.

## 12. Backup, restore, and migration

The implementation plan must define backup frequency, storage location, retention, integrity checks, recovery-point objective (RPO), and recovery-time objective (RTO). These values must be chosen for the actual deployment rather than assumed by this specification.

Restore acceptance requires a documented restore drill, integrity validation, and a comparison against expected record counts/revisions. Schema migrations must be versioned, repeatable where possible, backed up, and tested with rollback or forward-recovery instructions.

## 13. Observability and audit

Record operational events for failed validation, denied access, conflicting revisions, failed writes, imports, exports, migration, backup, restore, and lifecycle promotion. Logs should include correlation IDs and record IDs while excluding secrets. Monitoring must detect repeated failures and stale backup/verification evidence.

## 14. Interfaces and dependencies

The eventual memory service must expose documented interfaces for record creation, retrieval, update/revision, search, relationship lookup, audit query, backup/restore, and lifecycle transitions. Interface names and protocols are implementation decisions and must be recorded in the API Registry before being treated as existing APIs.

Dependencies include the project registries, permission/security controls, audit mechanism, testing strategy, and storage layer. If any dependency is absent, the relevant capability remains blocked or not implemented.

## 15. Required verification tests

- Schema validation accepts valid records and rejects malformed records.
- Unknown provenance cannot be silently marked verified.
- State transitions reject missing evidence or unauthorized approval.
- Conflicting revisions are detected and preserved.
- Duplicate suggestions do not silently delete or merge records.
- Search results show source, status, freshness and related conflicts.
- Concurrent updates do not silently overwrite a newer revision.
- Unauthorized reads, writes and exports are denied and audited.
- Secret-like values are rejected or redacted according to policy.
- Backup integrity is checked and a restore drill succeeds.
- Migration and rollback/recovery behavior is tested.
- Failed writes preserve the last valid state and surface an error.

## 16. Acceptance criteria

This specification can be accepted only after:
- the project owner reviews and approves the model and lifecycle;
- the schema and canonical ownership rules are consistent with the registries;
- retention, sensitivity, access, backup and recovery requirements are defined for the intended deployment;
- test cases map to every critical requirement;
- unresolved conflicts and implementation dependencies are recorded;
- the approval and revision are logged in the Decision Registry/change record.

Implementation completion is a separate milestone and requires code review, passing tests, and recorded evidence.

## 17. Current status and limitations

- Specification content: draft prepared for review.
- Implementation: NOT STARTED / NOT VERIFIED.
- Automated memory tests: NOT RUN.
- Backup/restore: NOT VERIFIED.
- Production: NOT VERIFIED.

No live memory service, database, API, or successful runtime behavior is claimed by this document.


## 18. BI-BUGS MEMORY CONTENT AND PRODUCT SCOPE BOUNDARY

Project memory is for traceable BI-BUGS project knowledge and delivery history; it is not a general personal-memory product, customer CRM, employee surveillance store, or substitute for an authoritative business system.

The current permitted project-memory subject matter is limited to project specifications, approved decisions, requirements, repository changes, defects, tests, release evidence, risks, and explicitly approved business requirements. Customer, employee, financial, health, access, or other sensitive operational records must not be stored in this project documentation memory by default.

If a future business workflow requires customer or staff records, it must use a separately designed and approved data store with a defined purpose, minimum fields, lawful basis/notice where applicable, access roles, retention, correction, deletion, export, backup, incident response, and audit controls. Do not copy such records into Markdown files, Git history, issue text, test fixtures, or project-memory summaries.

Every progress statement must cite the milestone or verification evidence that supports it. A planned feature, directory, specification, generated summary, or unverified test result must never be promoted to accepted or implemented state. Historical records remain immutable in meaning; corrections are recorded as dated addenda or superseding decisions.

This boundary is consistent with the BI-BUGS website scope and security/data approval gates. It does not claim that a memory service, customer database, or retention/deletion mechanism is implemented.
