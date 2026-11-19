# Project Rules — Supporting Index

**Status:** Draft summary; canonical rules govern.

Canonical sources: `MASTER_SPECIFICATION/02_ENGINEERING_CONSTITUTION.md`, `MASTER_SPECIFICATION/06_ENGINEERING_RULES.md`, `MASTER_SPECIFICATION/15_SECURITY.md`, `MASTER_SPECIFICATION/16_DEVOPS.md`, and `MASTER_SPECIFICATION/18_TESTING.md`.

- Inspect the repository and current changes before editing.
- Make small, scoped, reviewable changes; preserve unrelated work.
- Never expose credentials or use production data in ordinary tests.
- Run relevant checks and record actual output before changing status.
- Keep documentation aligned with implementation; label unimplemented requirements clearly.
- Do not commit/push until review and verification pass; verify the resulting revision and remote state.

## BI-BUGS scope and evidence boundary

These are concise supporting rules, not a separate authority. The BI-BUGS Pest Control Services website is the primary product; optional AI, plugins, microservices, mobile, hardware, booking, payments, and other workflows require specific owner-approved requirements. Preserve unrelated changes and never infer product completion from documents, folders, or a successful documentation-control test.
