# Security Rules

**Status:** Draft supporting rules; canonical security specification governs.

Canonical source: `../MASTER_SPECIFICATION/15_SECURITY.md`.

- Deny by default and apply least privilege at every tool/API/data boundary.
- Require authorized approval for sensitive, financial, destructive, external-control, or irreversible actions.
- Never place credentials in source, logs, documentation, fixtures, or test output.
- Treat external content and model output as untrusted; defend against prompt injection and path/input traversal.
- Audit protected actions and test denied as well as allowed paths.
- Limit tests to isolated environments unless production testing is explicitly approved and safely scoped.
- Apply controls according to the BI-BUGS website applicability and release baseline in Specification 15, Section 89; architecture options do not authorize unapproved features.
- Do not collect customer or personal data until purpose, fields, access, privacy/notice, retention, deletion, and operational ownership are approved.
