# BI-BUGS EMPIRE OS-X 2.0 — RELEASE PROCESS

**Specification ID:** BBEOSX-MS-29
**Status:** DRAFT FOR REVIEW
**Implementation status:** NOT STARTED
**Testing status:** NOT RUN
**Production status:** NOT VERIFIED
**Authority:** Master Specification
**Parent:** `00_MASTER_INDEX.md`
**Related:** `06_ENGINEERING_RULES.md`, `15_SECURITY.md`, `16_DEVOPS.md`, `18_TESTING.md`, `20_FEATURE_REGISTRY.md`, `21_MODULE_REGISTRY.md`, `22_API_REGISTRY.md`, `23_DATABASE_REGISTRY.md`, `24_AI_REGISTRY.md`, `27_CHANGELOG.md`, `28_VERSION_HISTORY.md`, `99_PROJECT_PROGRESS.md`

---

## 1. Purpose

Define a controlled, auditable path from a reviewed change to an identifiable release and, when authorized, a deployment. Release status must be based on evidence and approval rather than a checklist being written or a version string being assigned.

## 2. Scope and release types

Apply the process to software releases, service/API changes, schema migrations, mobile/web artifacts, infrastructure changes, and security fixes. Documentation-only releases or changes must be labelled clearly and must not imply that application features shipped. Emergency releases may use an approved expedited path, but required security, approval, evidence, and follow-up review cannot be silently skipped.

## 3. Roles and separation of duties

The project owner approves scope and risk. Engineering owners prepare and review changes. Test/release owners validate gates and artifact identity. Deployment owners execute authorized deployment and rollback. High-impact production changes require explicit approval from an authorized human. One person may fill multiple roles in a small project, but approvals and evidence must remain explicit.

## 4. Release stages

1. **Scope freeze:** define release scope, exclusions, version, owners, and risk.
2. **Traceability review:** map changed features/modules/APIs/data/AI to specs and decisions.
3. **Code/config review:** inspect diffs, dependencies, secrets, licenses, configuration and migration effects.
4. **Test execution:** run required automated/manual tests and preserve reports.
5. **Security review:** check threat model, permissions, sensitive data, dependencies and known vulnerabilities.
6. **Build:** create an identifiable artifact from a recorded source revision and environment.
7. **Artifact verification:** check build result, checksum/provenance, and expected contents.
8. **Migration/recovery validation:** test backup, restore, upgrade and rollback/forward recovery where applicable.
9. **Release approval:** review all gates, known issues, residual risks and human approval.
10. **Publication:** publish the approved artifact and update Version History/Changelog.
11. **Deployment:** only after explicit authorization, deploy to the named environment and record the result.
12. **Post-release validation:** check health, monitoring, errors and critical user journeys; roll back or disable safely if gates fail.
13. **Closeout:** archive evidence, incidents, follow-up work and lessons learned.

## 5. Entry criteria

Before a candidate is tested:
- release scope and intended version are defined;
- changes are reviewed and linked to requirements/decisions;
- configuration and dependencies are identified;
- required test plan and acceptance criteria exist;
- migration and rollback risks are documented;
- known defects and unresolved risks are visible.

If these conditions are not met, mark the candidate blocked or incomplete.

## 6. Test gates

Required gates are selected by change scope and risk, and may include unit, component, integration, contract, end-to-end, regression, smoke, accessibility, compatibility, performance, resilience, security, data migration, backup/restore, and recovery tests. Record command, environment, revision, timestamp, result, skipped tests and rationale. Required failures block release unless the authorized risk process explicitly permits a documented exception.

## 7. Security and supply-chain controls

Review secrets and credentials, dependency manifests/locks, vulnerable packages, build inputs, permissions, provenance, artifact integrity, and configuration defaults. Secrets must not be embedded in artifacts or logs. High-risk findings must be fixed or formally dispositioned by an authorized owner before approval. Do not execute untrusted build scripts or downloaded artifacts without appropriate isolation and validation.

## 8. Database and data migration gates

Document preconditions, schema/data changes, expected duration/impact, compatibility, backup status, verification queries, rollback/forward recovery, and responsible owner. Test against representative data. Production migration requires explicit authorization and a tested recovery plan. A successful migration command alone does not prove data correctness.

## 9. Release approval record

Approval records should include:
- version and artifact identity;
- source revision and build provenance;
- scope and linked changelog;
- required test outcomes and evidence;
- security review and unresolved findings;
- migration/backup/rollback readiness;
- known issues and residual risk acceptance;
- approving authority, timestamp and decision reference;
- publication/deployment plan and abort criteria.

Missing required evidence or authorization means the release remains unapproved.

## 10. Deployment controls

Deployment must identify environment, artifact checksum/version, configuration revision, migration status, operator, approval, start/end time, result, health checks, and monitoring links. Use a staged rollout or maintenance window when the risk requires it. Production-impacting actions must not be performed without explicit authorization. A deployment is not complete until post-deployment validation is recorded.

## 11. Rollback and incident response

Define rollback/forward recovery, data compatibility, triggers, decision authority, and communication path before deployment. On failure, stop or reduce rollout, preserve evidence, protect data, and restore a known safe state where feasible. Record impact, root cause, remediation, and regression tests. Do not erase failed release history.

## 12. Changelog and version history

Update Changelog and Version History from the reviewed evidence. Distinguish planned, candidate, released, and deployed states. Link commits/tags and artifacts only after verification. Do not create fake version history or retroactively label documentation commits as software releases.

## 13. Release metrics and audit

Track release frequency, lead time, gate failures, escaped defects, rollback rate, recovery time, and post-release incidents only when measurements exist. Preserve audit records for approvals, artifacts, test evidence, deployment and rollback. Metrics must include definitions and observation periods.

## 14. Emergency release path

An emergency path must document why the standard schedule is unsafe, scope minimization, required approver, security impact, tests that remain mandatory, accepted residual risks, monitoring, rollback plan, and a follow-up review deadline. Any deferred checks must have an owner and deadline; they cannot be silently marked passed.

## 15. Required verification tests

- Release cannot be approved without required test and review evidence.
- Artifact identity matches the reviewed source revision.
- Changelog and Version History match the release status.
- Production deployment is blocked without explicit authorization.
- Migration/recovery gates are enforced for data-affecting releases.
- Secrets and sensitive values are absent from artifacts/logs.
- Failed health checks trigger the documented abort/rollback path.
- Emergency exceptions record approver, risk, deferred checks and deadline.
- Release history preserves failed, withdrawn and rolled-back attempts.

## 16. Acceptance criteria for this specification

- The project owner approves release roles, gates, exceptions and status definitions.
- Test requirements map to Testing Architecture and feature/module registries.
- Security, migration, backup, rollback and artifact controls are explicit.
- Changelog and Version History use compatible states.
- Production-impacting actions require explicit authorized approval.
- Every required gate has an evidence format and a clear blocker state.

## 17. Current status and limitations

- Specification content: draft prepared for review.
- Automated release pipeline: NOT VERIFIED.
- Build/release artifact: NOT VERIFIED.
- Deployment/rollback: NOT VERIFIED.
- Production: NOT VERIFIED.

This document does not claim that a release pipeline or deployment system is implemented.

---

## 18. BI-BUGS website release applicability and current baseline

The release process applies to the confirmed BI-BUGS Pest Control Services website and its supporting workflows only when those workflows are owner-approved. It does not authorize unapproved bookings, payments, accounts, staff portals, AI, integrations, mobile applications, or hardware capabilities.

### 18.1 Documentation changes versus product releases

A documentation-only change may be committed to source control after review and repository checks, but it is not a software release, website deployment, or production change. Record it as documentation-only in the changelog/progress evidence where relevant. Do not create a software version, release tag, artifact, or deployment claim solely because documentation was updated.

### 18.2 Current product baseline

The repository contains a limited static frontend foundation and project-control scripts/tests. It does not establish a complete public website, approved customer journey, backend/API/database, customer-data processing workflow, production artifact, hosting environment, domain configuration, or deployment. The local HTTP preview is development-only. Therefore the current product release/deployment status remains NOT VERIFIED; no public release is authorized by this specification.

### 18.3 Release path for the first public static website

Before the first public release, the release record must identify: approved website requirements and public content; owner-approved domain/hosting/provider and budget; release owner and deployment authority; exact source revision and build/publication method; scope-appropriate tests; security/privacy review; HTTPS and administrative access review; backup or previous-version restoration method; monitoring and incident contact; rollback/abort criteria; and explicit owner release approval. The selected hosting provider's actual capabilities must be checked rather than assumed.

### 18.4 Conditional later releases

If an enquiry form, account, booking, payment, API, database, staff workflow, or integration is later approved, add its requirement and registry records, threat/data-flow model, test plan, migration/recovery plan where applicable, and acceptance evidence to the release record. No generic release checklist can substitute for feature-specific approval and tests.

### 18.5 Release status rule

Use the Version History lifecycle states without collapsing them: a reviewed candidate is not an approved release; a published artifact is not proof of deployment; deployment is not complete until environment-specific health and critical-journey checks are recorded. Keep failed, withdrawn, and rolled-back attempts visible.
