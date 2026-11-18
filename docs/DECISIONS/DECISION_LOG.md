# Decision Log

**Status:** Record template; decisions must be reviewed before acceptance.

Canonical policy: `../MASTER_SPECIFICATION/25_DECISION_REGISTRY.md`.

## Decision record template
- ID / title:
- Status: PROPOSED / UNDER_REVIEW / ACCEPTED / REJECTED / SUPERSEDED / WITHDRAWN
- Date / owner / approver:
- Context and constraints:
- Options considered:
- Evidence, assumptions, and uncertainty:
- Decision and rationale:
- Consequences, risks, and alternatives rejected:
- Related requirements, features, modules, commits, and tests:
- Reversal conditions / review date:

Accepted decisions should not be silently overwritten; supersede them with a linked decision. Do not include credentials or unnecessary personal data.

---

## DEC-BBE-001 — BI-BUGS Pest Control website is the primary project scope

- **Status:** ACCEPTED
- **Date:** 2026-11-17
- **Owner / approver:** Project Owner (explicit scope instruction)
- **Context and constraints:** Earlier project documents described BI-BUGS EMPIRE OS-X 2.0 inconsistently as a broad digital ecosystem or a platform for multiple field-service industries. The project owner clarified that BI-BUGS EMPIRE is being built for BI-BUGS Pest Control Services Pvt Ltd and its website; unrelated SAHIBEX work and generic enterprise scope must not be mixed into it.
- **Options considered:** (1) Continue with broad multi-industry platform scope; (2) make the BI-BUGS Pest Control Services website and its connected business workflows the primary and controlling scope.
- **Evidence, assumptions, and uncertainty:** The project owner's explicit instruction establishes the business purpose. Detailed website sitemap, approved service content, enquiry fields, booking rules, payment methods, and staff workflows still require requirements capture; they are not assumed by this decision.
- **Decision and rationale:** Option 2 is accepted. The public BI-BUGS Pest Control Services website is the primary customer-facing product. Backend, database, administration, communications, AI, automation, security, deployment, and reporting are supporting capabilities only where they serve the website and pest-control business workflows.
- **Consequences, risks, and alternatives rejected:** Generic multi-industry expansion, unrelated products, and speculative enterprise layers must not be treated as current delivery requirements. Existing architecture concepts are retained as future possibilities where appropriate; no historical material is deleted. Scope changes require a new owner-approved decision.
- **Related requirements, features, modules, commits, and tests:** `01_PROJECT_VISION.md`, `03_MASTER_BLUEPRINT.md`, `30_ROADMAP_20_YEARS.md`, `docs/MASTER_BLUEPRINT.md`, and the BI-BUGS website requirements to be specified.
- **Reversal conditions / review date:** Review only if the project owner explicitly changes the primary business purpose.
