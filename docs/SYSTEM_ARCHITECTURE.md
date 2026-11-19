# System Architecture — Supporting Entry Point

**Status:** Supporting overview; canonical specifications govern.

Canonical sources: `MASTER_SPECIFICATION/03_MASTER_BLUEPRINT.md`, `MASTER_SPECIFICATION/07_PROJECT_STRUCTURE.md`, `MASTER_SPECIFICATION/08_FOLDER_ARCHITECTURE.md`, and `MASTER_SPECIFICATION/14_MICROSERVICES.md`.

## Architecture review checklist
- Map user journeys to frontend/mobile, backend/API, AI/core services, data stores, deployment, and observability where these actually exist.
- For each boundary, document owner, interface, data classification, authorization, timeout, retry, and failure behavior.
- Define source-of-truth ownership and trace dependencies; avoid unapproved cyclic dependencies.
- Separate design intent from discovered code and verified runtime behavior.
- Validate diagrams and references against the current repository before treating them as authoritative.

This overview is a navigation aid, not proof that all listed components are implemented or connected.

## BI-BUGS current implementation boundary

This is a supporting checklist only. The current repository verifies a limited static frontend shell and documentation-control scripts/tests. Backend/API, database, AI runtime, business workflows, mobile/hardware integrations, and production deployment are not verified. Select architecture only from approved BI-BUGS requirements; the existence of a domain in a diagram does not approve or implement it.
