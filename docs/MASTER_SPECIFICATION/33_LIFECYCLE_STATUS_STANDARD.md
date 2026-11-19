# BI-BUGS EMPIRE OS-X 2.0
# MASTER SPECIFICATION — 33
# LIFECYCLE STATUS AND BACKWARD-COMPATIBILITY STANDARD

**Specification ID:** BBEOSX-MS-33
**Specification status:** DRAFT FOR REVIEW — ENGINEERING STANDARD; OWNER ACCEPTANCE PENDING
**Implementation status:** PARTIAL — AUDIT SCRIPT AND UNIT TESTS ADDED
**Testing status:** UNIT TESTS EXECUTED — SEE PROGRESS TRACKER
**Production status:** NOT APPLICABLE — DOCUMENTATION/DEVELOPMENT TOOLING ONLY
**Authority:** `00_MASTER_INDEX.md` and `02_ENGINEERING_CONSTITUTION.md`
**Related:** `06_ENGINEERING_RULES.md`, `07_PROJECT_STRUCTURE.md`, `18_TESTING.md`, `19_PROJECT_MEMORY.md`, `20_FEATURE_REGISTRY.md`, `21_MODULE_REGISTRY.md`, `29_RELEASE_PROCESS.md`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose

Define one unambiguous interpretation for lifecycle metadata across the numbered specifications while preserving existing documents and their history. This standard makes status reporting machine-checkable without treating a document label as proof of implementation, test execution, owner approval, release, or production readiness.

## 2. Canonical lifecycle dimensions

Every specification should expose these four independent dimensions in its header:

| Canonical field | What it describes | It does not prove |
|---|---|---|
| `Specification status` | Maturity and review/approval state of the written specification | Implementation or deployment |
| `Implementation status` | State of executable product capability | Test success or production use |
| `Testing status` | State of test execution and retained evidence | Owner acceptance or release |
| `Production status` | State of approved production deployment/operation | That a document is merely present |

Recommended header labels are exactly `Specification status`, `Implementation status`, `Testing status`, and `Production status`. Each field must be explicit. Use `NOT DECLARED` in reports when the source header does not state a dimension; do not silently fill it in.

## 3. Backward-compatible aliases

The audit tool recognizes these historical header labels as aliases without editing the source document:

| Canonical dimension | Recognized historical labels |
|---|---|
| Specification status | `Specification status`, `Status` |
| Implementation status | `Implementation status`, `Implementation` |
| Testing status | `Testing status`, `Testing` |
| Production status | `Production status`, `Production` |

The alias is recognized only when it appears as a metadata field in the document header. A mention in body text does not count. If more than one alias for the same dimension appears in a header, the report flags it as `AMBIGUOUS`; a human must resolve the conflict.

## 4. Interpretation safeguards

- `ACTIVE` is a legacy document/workstream label only. It is not equivalent to `APPROVED`, `IMPLEMENTED`, `TESTED`, `RELEASED`, or `PRODUCTION VERIFIED`.
- `DONE` or `COMPLETE` in a historical document does not independently prove current implementation, test, or production state.
- A missing field is `NOT DECLARED`, not an inferred success or failure.
- `NOT STARTED`, `NOT RUN`, `NOT VERIFIED`, `DRAFT`, `PENDING`, and `UNKNOWN` retain their literal meaning; do not normalize distinct states into one another.
- Approval requires an attributable owner/reviewer decision and evidence in the designated decision record. The status tool does not approve documents.
- Implementation, testing, release, and production claims require separate evidence and must never be inferred from the specification-status field.

## 5. Migration policy

1. New specifications use all four canonical labels.
2. Existing documents may retain recognized aliases until a separately reviewed migration is scheduled.
3. Migration must preserve the original value and meaning; do not convert `ACTIVE` to `APPROVED` or `DONE` to a software delivery state.
4. Before rewriting a header, record the old label/value, the proposed canonical label/value, the evidence for the mapping, and the reviewer decision.
5. Do not perform bulk metadata rewrites based only on pattern matching.
6. Update the Master Index and progress tracker when a migration is completed and verified.

## 6. Automated audit

Run the read-only audit from the repository root:

```bash
python scripts/validate_spec_lifecycle.py
```

The command scans numbered specifications 01–34, recognizes the aliases above, reports missing/ambiguous dimensions, and does not modify files. To make undeclared or ambiguous dimensions fail the command, run:

```bash
python scripts/validate_spec_lifecycle.py --strict
```

Strict mode is an audit gate for header completeness, not an approval gate. A clean report does not prove semantic correctness, owner acceptance, working software, executed product tests, release, or production readiness.

## 7. Acceptance criteria

- Alias mapping is documented and deterministic.
- Header parsing is limited to the document header, not body mentions.
- Missing and duplicate/ambiguous metadata are reported explicitly.
- The audit is read-only and does not rewrite source documents.
- Unit tests cover canonical labels, legacy aliases, missing fields, ambiguous aliases, and body-text exclusion.
- Status output preserves literal values and never upgrades a state.

## 8. Current implementation boundary

The audit utility and its unit tests are development tooling. They do not implement BI-BUGS customer-facing website, backend, database, AI, or business workflows. Their own test results are recorded in `99_PROJECT_PROGRESS.md`.
