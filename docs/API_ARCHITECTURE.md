# API Architecture — Supporting Guide

**Status:** Supporting guide; canonical specification governs.

Canonical source: `MASTER_SPECIFICATION/10_API_ARCHITECTURE.md`; registry: `MASTER_SPECIFICATION/22_API_REGISTRY.md`.

## API contract checklist
- Assign an owner and stable API-ID; document method, path/topic, version, schemas, consumers, and deprecation policy.
- Validate inputs at trust boundaries and define stable error responses, timeouts, retries, rate limits, and idempotency.
- Enforce authentication and authorization in executable code; use payload limits and safe structured logging.
- Maintain contract tests and record the revision and result of each verification run.

This guide describes requirements only. API availability and security must be proven by tests against actual implementations.