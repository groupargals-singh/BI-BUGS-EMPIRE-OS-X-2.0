# Security — Supporting Guide

**Status:** Supporting guide; canonical specification governs.

Canonical source: `MASTER_SPECIFICATION/15_SECURITY.md`; related sources: `MASTER_SPECIFICATION/02_ENGINEERING_CONSTITUTION.md`, `MASTER_SPECIFICATION/06_ENGINEERING_RULES.md`, and `MASTER_SPECIFICATION/18_TESTING.md`.

## Minimum controls
- Apply least privilege, deny by default, and enforce authorization outside AI/model prompts.
- Keep credentials out of source, logs, test fixtures, and documentation; redact sensitive output.
- Validate untrusted input and retrieved content; defend against injection and unsafe tool use.
- Audit protected actions, keep dependencies/configuration reviewed, and test recovery and rollback.
- Record security findings, severity, owner, fix, regression evidence, and accepted residual risk.

This page is not proof of a security audit or deployed controls. Record evidence for each implemented control.