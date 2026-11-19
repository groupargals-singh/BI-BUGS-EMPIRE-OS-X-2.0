# Coding Rules

**Status:** Draft supporting rules; canonical engineering rules govern.

Canonical source: `../MASTER_SPECIFICATION/06_ENGINEERING_RULES.md`.

- Prefer small, cohesive modules with explicit contracts and clear ownership.
- Validate untrusted input; handle errors intentionally; avoid leaking internal details or secrets.
- Keep configuration separate from code and use approved secret handling.
- Add tests for new behavior and regression tests for fixed defects.
- Avoid unrelated refactors in bug-fix changes; preserve backwards compatibility or document migrations.
- Run formatter, static checks, targeted tests, and relevant regression tests; record actual outcomes.

## BI-BUGS applicability

Apply coding rules to approved BI-BUGS website/workflow implementation only after Documentation Phase 1 and requirements approval. Prefer the simplest architecture that meets approved needs; do not add unapproved product features or speculative service boundaries.
