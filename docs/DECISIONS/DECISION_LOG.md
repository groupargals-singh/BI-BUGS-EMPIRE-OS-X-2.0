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


## DEC-BBE-002 — Build a new official BI-BUGS website from scratch

- **Status:** ACCEPTED
- **Date:** 2026-11-17
- **Owner / approver:** Project Owner (explicit instruction in the current ChatGPT conversation)
- **Context and constraints:** The project must establish its official BI-BUGS Pest Control Services website as a new build, rather than migrating, redesigning, or auditing an existing website as the source.
- **Options considered:** (1) Audit/migrate/redesign an existing official website; (2) build a new official BI-BUGS website from scratch.
- **Evidence, assumptions, and uncertainty:** Owner instruction: “BI-BUGS के लिए नई official website शुरू से बनानी है।” This confirms the new-build route only. It does not establish that no external website or business record exists, nor does it approve a domain, hosting provider, brand assets, service claims, sitemap, customer journey, payment/booking behavior, privacy terms, or production deployment.
- **Decision and rationale:** Option 2 is ACCEPTED. The official BI-BUGS website will be built from scratch. The owner-controlled source gate is recorded in `../MASTER_SPECIFICATION/32_WEBSITE_DISCOVERY_WORKBOOK.md` and validated by `scripts/validate_website_source_gate.py`.
- **Consequences, risks, and alternatives rejected:** Do not treat an unverified external URL as the official source. Domain, DNS, hosting, content, integrations, and release remain separately gated. Preserve all existing repository history and files.
- **Related requirements, features, modules, commits, and tests:** `31_WEBSITE_REQUIREMENTS.md`, `32_WEBSITE_DISCOVERY_WORKBOOK.md`, `scripts/validate_website_source_gate.py`, `testing/test_validate_website_source_gate.py`.
- **Reversal conditions / review date:** Change only through a new explicit owner-approved decision that supersedes this record.


## DEC-BBE-003 — India-wide and international geographic selector

- **Status:** ACCEPTED
- **Date:** 2026-11-23
- **Owner / approver:** Project Owner (explicit instruction in current conversation)
- **Context and constraints:** The new BI-BUGS website needs a location-selection scope that is not restricted to the company's currently confirmed service areas.
- **Decision:** Provide a distinct India selector covering all States/Union Territories and cities, plus a separate `International / World` option with country selection.
- **Evidence / approval boundary:** Owner instruction: “All India sabhi rajy or sabhi Sahar or ek agal se world ke desh ka option bhi rajhnA.” This approves the geographic selection scope only. It does not confirm service availability in all Indian locations or any overseas country.
- **Consequences / controls:** Requested/customer-selected location must remain distinct from confirmed service coverage. Never claim availability unless the relevant service has owner-confirmed coverage and has passed its evidence, compliance/safety, owner-approval and public-content publication gates. Enquiry-form use remains subject to customer-journey and privacy approval.
- **Related requirements:** `WREQ-GEO-001` in `../MASTER_SPECIFICATION/31_WEBSITE_REQUIREMENTS.md`; OI-03 in `../MASTER_SPECIFICATION/32_WEBSITE_DISCOVERY_WORKBOOK.md`.
- **Reversal conditions:** Change only through a subsequent explicit owner-approved decision.


## DEC-BBE-004 — Initial owner-declared active areas and public contact channels

- **Status:** ACCEPTED — PARTIAL GEOGRAPHIC/CONTACT INPUT
- **Date:** 2026-11-23
- **Owner / approver:** Project Owner (explicit instruction in current conversation)
- **Decision / supplied inputs:** Owner-declared active areas: Madhya Pradesh — Chambal region, Gwalior, Bhopal, Indore; Rajasthan — Jaipur, Jaisalmer; Uttar Pradesh — Agra. Owner supplied `Sambhav` as an additional Madhya Pradesh name and `Bolpur` as an additional Rajasthan name; both are retained verbatim pending clarification. Other India locations and all international countries remain inactive for now, while remaining available in the geographic selector.
- **Head office:** Morena, Madhya Pradesh (city only; exact address/landmark/map pin pending).
- **Public contact channels:** `7049967806`, `7869120139`, `bibugspest24@gmail.com`. Owner supplied these for website contact display. This does not approve WhatsApp integration or emergency/business-hour promises.
- **Evidence / boundary:** These are owner-provided website area declarations, not independent proof of every service's availability. Each service must still pass its own evidence, coverage, safety/compliance, owner approval and public-content gate. Chambal boundary is not yet defined.
- **Related records:** OI-03 in `../MASTER_SPECIFICATION/32_WEBSITE_DISCOVERY_WORKBOOK.md`; Specification 31 Section 22.
- **Reversal / update:** Owner may later activate additional locations or revise this list through an explicit instruction.
