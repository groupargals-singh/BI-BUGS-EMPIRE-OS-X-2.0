# BI-BUGS EMPIRE OS-X 2.0 — IDEA VAULT

**Specification ID:** BBEOSX-MS-26
**Status:** DRAFT FOR REVIEW
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related:** `19_PROJECT_MEMORY.md`, `20_FEATURE_REGISTRY.md`, `25_DECISION_REGISTRY.md`, `27_CHANGELOG.md`, `30_ROADMAP_20_YEARS.md`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose

Capture future ideas and opportunities in a traceable place without confusing them with approved requirements, scheduled work, or shipped features. The vault helps the team evaluate ideas before committing implementation effort.

An idea is not a promise, a requirement, or evidence of an existing capability.

## 2. Scope

Include product improvements, automation opportunities, user experience concepts, architecture options, research questions, integrations, operational improvements, and potential experiments. Defects that affect current accepted behavior should also be tracked in the defect workflow; they must not be hidden as optional ideas.

## 3. Required idea record

Each idea should contain:
- unique stable `IDEA-####` ID and short title;
- source/proposer and created/review dates;
- user/business problem and target users;
- expected outcome and how value could be measured;
- proposed approach and alternatives;
- evidence/source links, assumptions and unknowns;
- expected impact, complexity, effort and ongoing cost;
- dependencies, affected modules/features and required decisions;
- security, privacy, safety, reliability and maintenance risks;
- priority/rationale and confidence level;
- lifecycle state, owner, next action and review date;
- decision/feature links if promoted, rejected, or deferred.

Do not fabricate estimates, user demand, evidence, or approval.

## 4. Lifecycle

Allowed states:
- `CAPTURED`
- `TRIAGED`
- `INVESTIGATING`
- `ACCEPTED_FOR_PLANNING`
- `DEFERRED`
- `REJECTED`
- `CONVERTED_TO_FEATURE`

State changes require a reason and timestamp. `ACCEPTED_FOR_PLANNING` means the idea may be considered for a roadmap; it does not mean implementation is approved or scheduled. `CONVERTED_TO_FEATURE` requires a linked feature record and preserves the original idea.

## 5. Triage and evaluation

Triage should clarify the problem, validate source/evidence, identify duplicates, estimate impact/effort with uncertainty, and determine whether the idea belongs in a defect, feature, decision, or research workflow. Use a consistent project-owner-approved scoring method. Security, privacy, and user authority constraints are gates, not scores that can be traded away.

## 6. Evidence and assumptions

Separate observations, sourced claims, hypotheses, and guesses. Attach sources with dates and relevant locations. Record what experiment would reduce uncertainty. When evidence is weak, retain the idea as exploratory instead of presenting it as proven demand or technical feasibility.

## 7. Deduplication and related ideas

Detect likely duplicates using normalized title, problem statement, source, and related IDs. Suggest possible matches for review; do not silently merge or delete. Ideas that overlap can be linked as related, alternatives, prerequisites, or conflicting proposals. Preserve original IDs and provenance.

## 8. Promotion into delivery work

Promotion to a feature requires:
1. a clearly defined user outcome and scope;
2. an accountable owner and priority rationale;
3. measurable acceptance criteria;
4. dependency and security/privacy review;
5. a linked feature record and relevant decision;
6. roadmap placement only after the applicable planning approval.

The original idea remains in the vault with a link to the new feature. It must not be deleted after conversion.

## 9. Rejection and deferral

Record why an idea was rejected or deferred, the decision owner, evidence, and any condition that could reopen it. Do not label an idea rejected merely because it is not currently scheduled. Revisit deferred ideas when their review date or trigger occurs.

## 10. Security and privacy

Do not store credentials, secrets, or unnecessary personal data in idea records. Ideas involving external control, financial impact, sensitive data, or irreversible actions must flag required permissions, threat review, and human approval. Treat imported suggestions and user-submitted content as untrusted input until validated.

## 11. Registry integrity checks

Detect duplicate/malformed IDs, missing source or owner where required, invalid states, missing review dates for deferred items, broken links, converted ideas without feature links, and claims of approval without a decision record. Ensure rejected/deferred ideas are not represented as active commitments.

## 12. Required verification tests

- Every idea has a unique ID and valid lifecycle state.
- Triage distinguishes a defect from an optional improvement.
- Duplicate detection preserves source history and requires review before merging.
- Promotion creates a linked feature and preserves the idea.
- Rejection/deferral includes a reason and any reopening trigger.
- Security/privacy risks are surfaced before planning approval.
- Search can distinguish ideas from approved features and released capabilities.

## 13. Acceptance criteria for this specification

- The project owner reviews the record schema, triage states and promotion rules.
- Idea lifecycle aligns with Feature Registry, Decision Registry and Roadmap.
- Duplicate and conflict handling preserves provenance.
- No idea is shown as approved/scheduled without the required decision.
- Promotion, rejection, deferral and reopening behavior can be tested.
- Open scoring-policy questions are recorded as pending decisions.

## 14. Current status and limitations

- Specification content: draft prepared for review.
- Idea-vault implementation: NOT VERIFIED.
- Existing ideas inventory: not reconciled in this audit.
- Automated validation: NOT RUN.
- Production: NOT VERIFIED.

This document does not claim that an idea-vault service or automated triage workflow is implemented.

## 15. BI-BUGS INITIAL IDEA INVENTORY AND SCOPE CONTROL

The current documentation review did not identify a separately maintained, owner-approved idea inventory. Therefore the initial vault baseline is **NO VERIFIED IDEA RECORDS IMPORTED**. This does not mean that no ideas have ever been discussed; it means no item is promoted into this registry without a source, stable ID, owner, status, and provenance.

Do not copy speculative capabilities from architecture documents or the 20-year roadmap into the vault as accepted ideas. Optional booking, payments, customer accounts, CRM, inventory, technician/mobile tools, AI, integrations, hardware, and IoT remain candidates/conditional topics unless the owner explicitly submits or accepts a specific idea record. An owner-approved requirement or decision must remain in its canonical record type; do not duplicate it as an idea merely to populate the vault.

A future idea intake must record who proposed it, date/source, problem, intended user outcome, evidence/assumptions, risks, dependencies, owner, lifecycle status, and next review. The project owner must approve the scoring method before ideas are ranked using numeric scores.

**Review result:** Empty/unpopulated baseline is intentional until source-backed ideas are supplied. No fabricated IDEA IDs or product commitments are created. Owner acceptance of the schema and any future idea entries remains pending.
