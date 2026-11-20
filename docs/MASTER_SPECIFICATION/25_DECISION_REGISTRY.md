# BI-BUGS EMPIRE OS-X 2.0 — DECISION REGISTRY

**Specification ID:** BBEOSX-MS-25
**Status:** REVIEWED — OWNER ACCEPTANCE PENDING
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related:** `02_ENGINEERING_CONSTITUTION.md`, `06_ENGINEERING_RULES.md`, `19_PROJECT_MEMORY.md`, `20_FEATURE_REGISTRY.md`, `21_MODULE_REGISTRY.md`, `26_IDEA_VAULT.md`, `27_CHANGELOG.md`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose

Maintain an auditable record of material product, architecture, engineering, security, data, and delivery decisions. The registry explains what was decided, why, by whom, based on which evidence, and what the decision affects.

A proposal is not binding until accepted by an authorized decision owner. Recording a decision does not prove that it has been implemented.

## 2. Scope

Record decisions that affect project direction, architecture boundaries, interfaces, data ownership, security, privacy, dependencies, technology selection, migration, release policy, significant scope, or material risk. Routine reversible implementation details may be recorded in code review unless they affect a canonical contract or future compatibility.

## 3. Required decision record

Each record must include:
- unique stable `DEC-####` ID and concise title;
- lifecycle status and decision date;
- decision owner, required approver and actual approval record;
- context, problem statement and desired outcome;
- constraints, non-goals, assumptions and unknowns;
- options considered, including doing nothing where relevant;
- evidence, sources, experiments and confidence/limitations;
- selected option and explicit rationale;
- consequences, benefits, trade-offs and residual risks;
- affected specifications, features, modules, APIs, data and releases;
- security/privacy/safety and operational impact;
- implementation steps, migration and rollback/recovery plan;
- validation/test plan and success criteria;
- review trigger/date and superseding/superseded-by links;
- change/commit references when implementation occurs.

Unknown information must be labelled pending rather than fabricated.

## 4. Lifecycle

Allowed states:
- `PROPOSED`
- `UNDER_REVIEW`
- `ACCEPTED`
- `REJECTED`
- `SUPERSEDED`
- `WITHDRAWN`

Only the authorized owner/approver can accept a decision. Every transition records actor, timestamp, reason and supporting record. An accepted decision can later be superseded; its original history must remain readable.

## 5. Decision quality

A decision should state the problem rather than start with a preferred solution. Compare meaningful alternatives using relevant criteria such as user value, security, privacy, reliability, maintainability, compatibility, cost, complexity, reversibility, and evidence quality. Explain why the chosen option is preferable under the stated constraints and what would change the conclusion.

## 6. Evidence and assumptions

Separate measured results, authoritative requirements, expert judgement, estimates, and unverified assumptions. Link sources with dates and relevant locations. Record uncertainty and known evidence gaps. Do not present generated text, undocumented verbal claims, or a single unverified test as conclusive evidence.

## 7. Authority and approvals

The project constitution and user authority take precedence over lower-level decisions. Decisions cannot grant permission to bypass security controls, erase required audit history, or modify governing rules without the authorized process. High-impact, financial, destructive, external-control, privacy-sensitive, or production-impacting decisions require explicit authorized approval and risk review.

## 8. Implementation traceability

When a decision is implemented, link the relevant code/configuration changes, pull request or review, tests, release and rollback reference. Mark implementation separately from acceptance. If implementation diverges from the accepted decision, record a new decision or approved amendment rather than silently changing the original.

## 9. Review and reversal

Review a decision when its assumptions fail, dependencies change, security risk changes, acceptance criteria fail, cost/latency exceeds approved bounds, or a replacement becomes available. Reversal requires impact analysis, migration/rollback plan, and a new linked decision. Preserve the old decision as superseded, not deleted.

## 10. Conflicts and precedence

When decisions conflict:
1. identify the affected requirements and records;
2. compare authority, date, scope, evidence and explicit supersession;
3. apply the governing constitution and approved hierarchy;
4. escalate unresolved conflicts to the authorized owner;
5. record the resolution and update affected specifications/registries.

Do not infer precedence solely from which file was edited most recently.

## 11. Links to other registries

- Feature Registry: decisions that approve, reject, or change feature scope.
- Module Registry: ownership, boundaries and dependency decisions.
- API Registry: contract, versioning and compatibility decisions.
- Database Registry: source of truth, schema, retention and migration decisions.
- AI Registry: model/provider, permissions, evaluation and data-exposure decisions.
- Idea Vault: ideas promoted to formal consideration.
- Changelog/Version History: implemented and released changes.
- Project Progress: milestone impact and unresolved blockers.

Each linked record remains canonical in its owning registry.

## 12. Registry integrity checks

Detect duplicate IDs, missing approver for accepted decisions, missing rationale/options, unsupported evidence claims, unresolved conflicts, missing affected-record links, accepted decisions without review triggers when risk warrants them, and implemented/released claims without traceability. Ensure supersession links are reciprocal and IDs are never recycled.

## 13. Required verification tests

- IDs and lifecycle values are unique and valid.
- Acceptance is blocked when required approval or rationale is missing.
- Every accepted decision has context, options, evidence/assumptions and consequences.
- Material security/data/compatibility impact is recorded.
- Superseded decisions retain their history and links.
- Conflicts are flagged rather than silently overwritten.
- Implementation status requires code/test/release references.
- Access to sensitive decision records is permission-checked and audited.

## 14. Acceptance criteria for this specification

- The project owner approves the record schema, authority rules and lifecycle.
- Decision authority aligns with the Engineering Constitution and Security Rules.
- Registry links match the Feature, Module, API, Database, AI, Idea and Change registries.
- Approval and supersession workflows are testable.
- High-impact decisions require explicit evidence and approval.
- Unresolved policy choices are documented as pending decisions.

## 15. Current status and limitations

- Specification content: draft prepared for review.
- Registry implementation: NOT VERIFIED.
- Automated validation: NOT RUN.
- Existing decisions: must be inventoried from the canonical decision log and reviewed.
- Production: NOT VERIFIED.

This document does not claim that a decision-registry service or automated approval workflow is implemented.

## 16. BI-BUGS DECISION LOG BASELINE AND CURRENT RECORDS

`docs/DECISIONS/DECISION_LOG.md` is the current canonical record store for project decisions; this specification defines the registry schema and governance. Do not create duplicate records in a second file or treat a schema example as a real decision. Stable IDs remain unique and are never recycled.

| Decision ID | Title | Status | Evidence location | Scope boundary |
|---|---|---|---|---|
| DEC-BBE-001 | BI-BUGS Pest Control website is the primary project scope | ACCEPTED | `../DECISIONS/DECISION_LOG.md` | Controls project purpose; detailed requirements remain open |
| DEC-BBE-002 | Build a new official BI-BUGS website from scratch | ACCEPTED | `../DECISIONS/DECISION_LOG.md` | Approves new-build route only; not domain, hosting, content, workflow, payment, or production release |

These two records are the only accepted project decisions identified in the current decision-log baseline. This is a bounded repository inventory, not a claim that no verbal or external business decisions exist. Any additional owner decision must be captured in the canonical log with the complete schema before it is treated as binding.

**Review result:** Schema and canonical decision-log linkage reviewed. No additional decision records have been invented. Automated registry validation and owner acceptance of the schema remain pending.
