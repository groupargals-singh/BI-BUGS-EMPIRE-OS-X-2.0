# BI-BUGS EMPIRE OS-X 2.0 — Master Specification

**Document status:** DRAFT FOR REVIEW

## Source of truth

- [00_MASTER_INDEX.md](00_MASTER_INDEX.md) — specification catalogue and navigation.
- [99_PROJECT_PROGRESS.md](99_PROJECT_PROGRESS.md) — milestone status and verification evidence.
- [32_WEBSITE_DISCOVERY_WORKBOOK.md](32_WEBSITE_DISCOVERY_WORKBOOK.md) — owner-input checklist for website identity, content, customer journey, and operations.
- [33_LIFECYCLE_STATUS_STANDARD.md](33_LIFECYCLE_STATUS_STANDARD.md) — canonical lifecycle dimensions, backward-compatible aliases, and audit policy.
- [34_CROSS_DOCUMENT_TRACEABILITY_AUDIT.md](34_CROSS_DOCUMENT_TRACEABILITY_AUDIT.md) — semantic consistency findings, registry/traceability gaps, and remaining delivery gates.
- [35_LOCATION_CATALOGUE_AND_COVERAGE_GOVERNANCE.md](35_LOCATION_CATALOGUE_AND_COVERAGE_GOVERNANCE.md) — location selector scope, owner-selected active-area register, data provenance, and per-service coverage safeguards.
- [LOCATION_AREA_REGISTER.json](LOCATION_AREA_REGISTER.json) — canonical machine-readable owner-selected location register.
- Website source decision gate: `../scripts/validate_website_source_gate.py` (tested by `../testing/test_validate_website_source_gate.py`).
- Numbered specifications 01–35 define the intended architecture, governance, BI-BUGS website requirements baseline, owner-input discovery, lifecycle-status controls, semantic traceability, and location catalogue/coverage governance.


- [DOCUMENTATION_COMPLETION_MATRIX.md](DOCUMENTATION_COMPLETION_MATRIX.md) — document-by-document completion matrix, owner-input gates, and Documentation Phase 1 acceptance checklist.

## Status meanings

- **DRAFT FOR REVIEW / DRAFT CREATED:** document exists but has not passed its full review and acceptance checks.
- **IMPLEMENTATION NOT STARTED:** architecture is described; working code has not been verified by this document.
- **VERIFIED:** required checks ran against an identified revision and evidence is recorded.
- **RELEASED:** a release record and deployment evidence exist. A commit alone is not a software release.

## Engineering workflow

1. Inspect the exact repository path, branch, current revision, and working-tree changes.
2. Read the relevant canonical specification and linked decisions before editing.
3. Make a scoped change and preserve unrelated work.
4. Run formatting, link, structural, and relevant behavior checks.
5. Record actual outcomes and evidence in the progress tracker.
6. Commit or push only after review and verification; never infer success from an attempted command.

## Important boundary

These files describe intended architecture and acceptance criteria. They do not prove that software, CI, production controls, tests, or integrations are implemented. Mark implementation as verified only when executable evidence supports that claim.

## Auxiliary completion control

`DOCUMENTATION_COMPLETION_MATRIX.md` is a supporting control artifact, not a numbered Master Specification. Master Index entry 35 refers to the website source-gate validator. The matrix tracks semantic review and owner-input gates; it does not replace canonical specifications or constitute owner approval.
