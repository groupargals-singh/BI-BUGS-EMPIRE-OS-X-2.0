# Database Architecture — Supporting Guide

**Status:** Supporting guide; canonical specification governs.

Canonical source: `MASTER_SPECIFICATION/09_DATABASE_ARCHITECTURE.md`; registry: `MASTER_SPECIFICATION/23_DATABASE_REGISTRY.md`.

## Data governance checklist
- Document entities, fields, keys, constraints, indexes, ownership, consumers, classification, and retention.
- Version migrations and test upgrade and rollback paths using isolated test data.
- Apply least privilege, minimize sensitive data, and define deletion and concurrent-update behavior.
- Define backup frequency, retention, recovery-point and recovery-time objectives; verify by restoring and checking integrity.

A schema description or backup file is not evidence of a working database or successful recovery.

## BI-BUGS current data baseline

No application database, schema, migration, or customer/staff data store is verified in the current repository. Do not design customer fields or collect personal data until the business purpose, minimum fields, notice/consent, access, retention, deletion, audit, backup, and recovery requirements are approved. The canonical design and registry remain Specifications 09 and 23.
