# Engineering Rules

**Status:** Draft supporting summary; canonical specification governs.

Canonical source: `../MASTER_SPECIFICATION/06_ENGINEERING_RULES.md`.

- Inspect repository status, dependencies, entry points, and callers before editing.
- Maintain one canonical source for each requirement or decision; link summaries rather than copying full specifications.
- Trace features to acceptance criteria, modules, tests, and release records.
- Keep changes scoped and reviewable; preserve user data and unrelated changes.
- Record evidence and blockers honestly. A document, directory, or planned test does not prove implementation.
- Commit/push only after review and verification; confirm exact revision and remote state.

## BI-BUGS applicability

This summary is subordinate to `../MASTER_SPECIFICATION/06_ENGINEERING_RULES.md`. Scope is the BI-BUGS Pest Control Services website and approved supporting workflows. Keep the current static shell distinct from unimplemented backend, database, API, AI, and business capabilities.
