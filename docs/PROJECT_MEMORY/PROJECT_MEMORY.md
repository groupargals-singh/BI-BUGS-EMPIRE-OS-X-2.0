# Project Memory — Supporting Index

**Status:** Draft index; canonical memory design is under review.

Canonical source: `../MASTER_SPECIFICATION/19_PROJECT_MEMORY.md`.
Related registries: `../MASTER_SPECIFICATION/20_FEATURE_REGISTRY.md`, `../MASTER_SPECIFICATION/21_MODULE_REGISTRY.md`, `../MASTER_SPECIFICATION/25_DECISION_REGISTRY.md`, `../MASTER_SPECIFICATION/27_CHANGELOG.md`, and `../MASTER_SPECIFICATION/99_PROJECT_PROGRESS.md`.

## Memory record principles
- Preserve stable IDs, status, timestamps, provenance, related records, and revision history.
- Distinguish proposed from accepted, implemented, verified, and released facts.
- Keep unresolved conflicts visible; detect duplicates without silently discarding records.
- Never store credentials; minimize sensitive data and limit access.
- Verify backups through restore tests before claiming recoverability.

No memory engine or persistence behavior is claimed implemented by this document.

## BI-BUGS data boundary

This index is for project documentation and traceable delivery knowledge only. It is not a customer/staff database, CRM, surveillance store, or live memory service. Follow `../MASTER_SPECIFICATION/19_PROJECT_MEMORY.md` for the canonical privacy, retention, provenance, and scope rules. Do not place customer records, staff personal data, credentials, or secrets in Markdown or Git.
