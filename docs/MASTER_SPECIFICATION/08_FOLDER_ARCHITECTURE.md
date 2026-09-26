# 08 — FOLDER ARCHITECTURE

## 1. Purpose

The Folder Architecture Specification defines the permanent architectural
responsibility of project folders and their controlled expansion.

Its purpose is to ensure that every folder has a clear role, ownership,
boundary, dependency direction, and documentation relationship.

Folders are architectural boundaries, not merely storage locations.

No folder should exist without a defined responsibility.

---

## 2. Architectural Authority

This specification operates under:

- 01_PROJECT_VISION.md
- 02_ENGINEERING_CONSTITUTION.md
- 03_MASTER_BLUEPRINT.md
- 06_ENGINEERING_RULES.md
- 07_PROJECT_STRUCTURE.md

Where a conflict exists, the higher-level constitutional and architectural
documents have authority.

This document defines folder-level architecture.

---

## 3. Folder Architecture Principle

Every folder MUST have:

- a defined purpose
- an owner
- an allowed content category
- a dependency boundary
- a naming convention
- a documentation relationship
- a verification requirement

A folder MUST NOT become a miscellaneous storage area.

---

## 4. Repository Root

The repository root contains the primary system domains:

- ai-core/
- backend/
- cloud/
- database/
- deployment/
- docs/
- frontend/
- hardware/
- mobile/
- scripts/
- testing/

Each root domain represents a major architectural boundary.

Root-level domains MUST remain understandable without inspecting their
internal implementation.

---

## 5. ai-core/

Purpose:

Contains the core intelligence, reasoning, decision-support, AI orchestration,
and model-independent intelligence components of BI-BUGS EMPIRE OS X.

Responsibilities MAY include:

- intelligence engines
- reasoning systems
- AI orchestration
- context processing
- agent coordination
- model adapters
- intelligence policies
- AI memory interfaces

Business UI code MUST NOT be placed here.

Database implementation MUST NOT be placed here.

Deployment configuration MUST NOT be placed here.

---

## 6. backend/

Purpose:

Contains server-side application logic and service interfaces.

Responsibilities MAY include:

- application services
- business logic
- API implementation
- request processing
- authentication integration
- authorization integration
- backend orchestration
- service coordination

The backend MUST NOT become a replacement for the AI core.

AI-specific intelligence MUST remain architecturally separated.

---

## 7. cloud/

Purpose:

Contains cloud-oriented infrastructure and integration architecture.

Responsibilities MAY include:

- cloud providers
- cloud services
- cloud storage integration
- cloud messaging
- distributed infrastructure adapters
- cloud deployment integration
- cloud-specific configuration

Cloud-specific implementation MUST remain separable from the core
application architecture wherever practical.

The system MUST NOT become permanently dependent on a single cloud provider
without an explicit architectural decision.

---

## 8. database/

Purpose:

Contains database architecture and implementation.

Responsibilities MAY include:

- schemas
- migrations
- repositories
- database adapters
- query layers
- indexing
- data models
- database utilities
- persistence infrastructure

Database code MUST NOT contain unrelated business interfaces.

Database access MUST occur through defined boundaries.

---

## 9. deployment/

Purpose:

Contains deployment and environment delivery architecture.

Responsibilities MAY include:

- deployment configurations
- container definitions
- infrastructure configuration
- environment templates
- release configuration
- deployment automation
- production delivery configuration

Secrets MUST NOT be committed into deployment files.

Deployment configuration MUST remain traceable to supported environments.

---

## 10. docs/

Purpose:

Contains the authoritative documentation system of the project.

Responsibilities include:

- master specifications
- architecture documentation
- engineering rules
- security rules
- decisions
- project memory
- roadmap
- standards
- registries
- changelog
- progress tracking

Documentation MUST remain synchronized with verified project state.

Documentation MUST NOT falsely represent planned architecture as implemented
architecture.

## 11. frontend/

Purpose:

Contains the user-facing web application and presentation layer.

Responsibilities MAY include:

- pages
- components
- layouts
- frontend state
- client-side services
- frontend routing
- accessibility
- user interaction
- presentation utilities

Frontend code MUST NOT directly own database infrastructure.

Frontend code MUST NOT bypass defined backend or API boundaries.

---

## 12. mobile/

Purpose:

Contains mobile-specific application architecture.

Responsibilities MAY include:

- mobile application code
- mobile UI
- mobile navigation
- device integration
- mobile storage adapters
- notifications
- mobile-specific services
- mobile application configuration

Mobile-specific implementation MUST remain separated from general backend
and AI-core responsibilities.

Shared logic SHOULD be reused through defined interfaces rather than
duplicated without architectural justification.

---

## 13. hardware/

Purpose:

Contains hardware integration and device-control architecture.

Responsibilities MAY include:

- hardware interfaces
- sensor integrations
- device communication
- embedded integrations
- hardware drivers
- hardware abstraction layers
- device configuration
- hardware diagnostics

Hardware-specific code MUST NOT leak uncontrolled device assumptions into
the core application.

Hardware dependencies MUST be isolated behind defined interfaces.

---

## 14. scripts/

Purpose:

Contains controlled development, maintenance, automation, and utility
scripts.

Responsibilities MAY include:

- development utilities
- repository maintenance
- validation scripts
- migration helpers
- build helpers
- release helpers
- administrative automation
- diagnostic utilities

Scripts MUST have a clear purpose.

Temporary experiments MUST NOT accumulate permanently inside scripts/.

---

## 15. testing/

Purpose:

Contains the project's verification and testing architecture.

Responsibilities MAY include:

- unit tests
- integration tests
- system tests
- end-to-end tests
- security tests
- performance tests
- regression tests
- test fixtures
- test utilities
- validation infrastructure

Testing code MUST remain traceable to the system behavior it verifies.

Tests MUST NOT be treated as optional documentation.

---

## 16. Root Folder Ownership

Each root folder MUST have one primary architectural owner.

Ownership means responsibility for:

- structure
- purpose
- allowed contents
- dependency boundaries
- lifecycle
- verification
- documentation

Multiple teams or modules MAY contribute to a folder, but ownership MUST
remain identifiable.

---

## 17. Root Folder Expansion

New root-level folders MUST NOT be created casually.

A new root folder requires:

1. documented purpose
2. architectural justification
3. dependency analysis
4. ownership definition
5. naming validation
6. documentation update
7. progress tracking

If an existing root domain can responsibly contain the functionality,
creating another root domain SHOULD be avoided.

---

## 18. Subfolder Creation

Subfolders MAY be created when they provide a meaningful architectural
boundary.

A subfolder SHOULD exist when at least one of the following is true:

- responsibility is clearly separable
- ownership differs
- lifecycle differs
- security boundary differs
- dependency boundary differs
- testing boundary differs
- deployment boundary differs
- scalability requirement differs

Subfolders MUST NOT be created solely to make a directory appear more
organized.

---

## 19. Folder Naming

Folder names MUST be:

- clear
- predictable
- stable
- descriptive
- consistent
- lowercase where applicable

Names MUST communicate architectural purpose.

Abbreviations SHOULD be avoided unless they are established project-wide
terms.

Ambiguous names such as:

- misc/
- stuff/
- temp/
- random/
- other/

MUST NOT be used as permanent architectural folders.

---

## 20. Folder README Principle

A folder MAY contain a README when additional local documentation is useful.

A README SHOULD explain:

- folder purpose
- ownership
- allowed contents
- important dependencies
- entry points
- testing expectations
- related specifications

A README MUST NOT contradict the Master Specification.

When a folder has complex internal architecture, local documentation SHOULD
be provided rather than placing all details into one central document.

## 21. Domain Boundary

Every major folder represents a domain boundary.

Code SHOULD remain inside the domain responsible for its primary purpose.

Cross-domain access MUST occur through defined interfaces where practical.

Direct access to internal implementation details of another domain SHOULD
be avoided.

---

## 22. Dependency Direction

Folder dependencies MUST follow the architectural dependency direction.

Higher-level coordination MAY depend on lower-level infrastructure.

Lower-level infrastructure MUST NOT unexpectedly depend on higher-level
application behavior.

Circular folder dependencies MUST be prevented.

---

## 23. Shared Infrastructure

Shared infrastructure SHOULD exist only when multiple domains genuinely
require the same capability.

Examples MAY include:

- common configuration
- logging
- validation
- security primitives
- common utilities
- shared contracts

Shared infrastructure MUST NOT become a dumping ground for unrelated code.

---

## 24. Shared Code Ownership

Every shared component MUST have an identifiable owner.

Shared code MUST define:

- purpose
- consumers
- compatibility expectations
- testing responsibility
- change responsibility

A component MUST NOT become shared merely because it is convenient to import.

---

## 25. API Folder Boundaries

API-related implementation MUST remain inside appropriate backend or service
boundaries.

Frontend and mobile applications MUST consume defined API contracts rather
than internal backend implementation.

API contracts SHOULD be documented and version-aware.

Breaking API changes MUST follow the project's change-management process.

---

## 26. Database Folder Boundaries

Database implementation MUST remain inside database-related boundaries.

Other domains MUST NOT duplicate database infrastructure unnecessarily.

Schema changes MUST be traceable to:

- feature requirements
- migration history
- documentation
- testing

Database credentials MUST NOT be stored in source-controlled files.

---

## 27. AI Folder Boundaries

AI-related code MUST remain separated according to responsibility.

AI-core MAY contain:

- reasoning
- orchestration
- model abstraction
- intelligence services
- AI policies

AI-core MUST NOT silently absorb unrelated application, UI, database, or
deployment responsibilities.

---

## 28. Configuration Boundaries

Configuration MUST remain separate from application logic.

Configuration MAY include:

- environment settings
- feature flags
- service endpoints
- runtime options
- deployment parameters

Sensitive configuration MUST use approved secret-management mechanisms.

Configuration precedence MUST be deterministic and documented.

---

## 29. Environment Boundaries

The architecture MUST distinguish environments such as:

- development
- testing
- staging
- production

Environment-specific configuration MUST NOT be mixed accidentally.

Production configuration MUST NOT be used as a development default.

Development shortcuts MUST NOT silently become production behavior.

---

## 30. Secret Boundary

Secrets include, but are not limited to:

- passwords
- API keys
- access tokens
- private keys
- database credentials
- signing credentials

Secrets MUST NOT be committed into the repository.

Secret files MUST be excluded through appropriate repository controls.

Secret access MUST follow least-privilege principles.

If a secret is exposed, the incident MUST be treated as a security event
and the credential SHOULD be rotated immediately.

## 31. Documentation Boundary

Documentation MUST remain inside docs/ unless a local README is required
for a specific implementation domain.

Architectural documentation MUST remain traceable to the Master
Specification.

Documentation MUST distinguish:

- planned
- designed
- implemented
- tested
- deployed
- production-ready

Documentation MUST NOT be used to falsely indicate implementation status.

---

## 32. Testing Boundary

Tests MUST remain inside testing/ unless a framework requires colocated
tests for a specific implementation boundary.

Colocated tests MAY be used when they improve maintainability.

Regardless of location, every test MUST have a clear relationship to the
component or behavior being verified.

---

## 33. Deployment Boundary

Deployment-specific files MUST remain inside deployment/ unless they are
required by a platform-specific convention.

Deployment files MUST NOT contain application business logic.

Deployment MUST consume defined build artifacts and configuration.

---

## 34. Script Boundary

Scripts MUST remain focused on automation.

A script SHOULD perform one clearly defined operational responsibility.

Scripts MUST NOT silently modify architectural rules.

Destructive scripts MUST provide appropriate safeguards and confirmation.

---

## 35. Hardware Boundary

Hardware integrations MUST use abstraction boundaries where practical.

Hardware-specific assumptions MUST NOT propagate throughout the application.

Device failures MUST be isolatable from unrelated software domains.

Hardware access SHOULD be testable through simulated or mocked interfaces
where practical.

---

## 36. Cloud Boundary

Cloud services MUST be accessed through controlled integration boundaries.

Provider-specific code SHOULD be isolated where practical.

Cloud architecture MUST document:

- provider
- service
- purpose
- credentials
- dependency
- failure behavior
- replacement strategy

---

## 37. Mobile Boundary

Mobile applications MUST remain consumers of defined services and APIs.

Mobile code MUST NOT bypass security boundaries.

Device-specific capabilities MUST remain isolated from portable application
logic.

---

## 38. Frontend Boundary

Frontend code MUST remain focused on presentation and user interaction.

Business-critical rules SHOULD remain in authoritative backend or core
services rather than being trusted solely to client-side validation.

Client-side validation MAY improve user experience but MUST NOT replace
server-side security validation.

---

## 39. Backend Boundary

Backend services MUST enforce authoritative application behavior.

Responsibilities MAY include:

- authentication
- authorization
- business rules
- API processing
- service orchestration
- transaction coordination
- server-side validation

Backend MUST NOT become an unstructured monolith.

---

## 40. AI-Core Boundary

AI-core MUST remain model-independent wherever practical.

Model-specific implementations MUST be isolated behind adapters or defined
interfaces.

AI-core MAY coordinate:

- reasoning
- planning
- context
- memory
- model selection
- AI tools
- verification

AI-core MUST NOT directly own unrelated presentation or deployment logic.

---

## 41. Circular Dependency Prevention

Circular dependencies between folders MUST NOT be introduced.

If two domains require each other, the architecture SHOULD introduce:

- an interface
- shared contract
- event
- abstraction
- service boundary

The goal is to preserve directional dependency flow.

---

## 42. Dependency Ownership

Every external dependency MUST have an identifiable purpose.

Dependencies SHOULD be:

- necessary
- maintained
- version-controlled
- security-reviewed
- documented where significant

Unused dependencies MUST be removed.

Duplicate dependencies serving the same purpose SHOULD be avoided.

---

## 43. Package and Module Boundaries

Modules MUST have focused responsibilities.

A module SHOULD NOT contain unrelated features merely because they are
technically compatible.

Large modules SHOULD be decomposed when:

- ownership becomes unclear
- testing becomes difficult
- dependencies become excessive
- change risk increases
- responsibilities become unrelated

---

## 44. Build Boundary

Build configuration MUST remain deterministic.

Build processes MUST identify:

- inputs
- outputs
- dependencies
- environment requirements
- failure conditions

Build artifacts MUST NOT be treated as source code.

Generated build output SHOULD NOT be committed unless explicitly required.

---

## 45. Release Boundary

Release preparation MUST remain separate from ordinary development.

A release MUST have:

- version
- change record
- verification state
- deployment target
- rollback strategy
- release evidence

Unverified changes MUST NOT be represented as production releases.

---

## 46. Backup Boundary

Backup architecture MUST define:

- what is backed up
- backup frequency
- retention
- storage location
- encryption
- restoration process
- verification process

A backup that has never been tested for restoration MUST NOT be assumed
to be reliable.

---

## 47. Migration Boundary

Database and structural migrations MUST be explicit.

Every migration SHOULD define:

- reason
- source state
- target state
- compatibility requirements
- rollback or recovery strategy
- verification

Migrations MUST NOT depend on undocumented manual steps.

---

## 48. Observability Boundary

Observability MAY include:

- logs
- metrics
- traces
- health checks
- alerts
- diagnostics

Observability components MUST respect security and privacy requirements.

Sensitive secrets MUST NOT appear in logs.

---

## 49. Audit Boundary

Important system operations MUST remain auditable.

Audit records SHOULD identify:

- action
- actor
- timestamp
- target
- result
- relevant context

Audit data MUST be protected from unauthorized modification.

---

## 50. Security Boundary

Security architecture MUST remain a cross-domain concern.

Security responsibilities MAY include:

- authentication
- authorization
- secrets
- encryption
- input validation
- audit
- isolation
- dependency security
- secure configuration

Security controls MUST NOT depend solely on frontend behavior.

---

## 51. Permission Boundary

Permission-sensitive operations MUST cross defined authorization boundaries.

Protected operations MAY include:

- write
- delete
- execute
- network access
- credential access
- system changes
- financial operations
- external control

Permissions MUST be explicit and auditable.

---

## 52. User Authority Boundary

The user remains the highest authority for protected project operations
where the system constitution requires user approval.

Automation MUST NOT silently bypass required approval gates.

System convenience MUST NOT override explicit user authority.

---

## 53. Self-Modification Boundary

The system MUST distinguish ordinary runtime behavior from modification of
its own architecture or source.

Self-modification MUST NOT bypass:

- authorization
- verification
- audit
- change management
- rollback requirements

Architectural self-change MUST require the appropriate approval.

---

## 54. Data Ownership Boundary

Every persistent data category MUST have an identifiable owner.

Ownership includes:

- creation
- modification
- access
- retention
- deletion
- backup
- migration
- security

Data ownership MUST remain documented for important datasets.

---

## 55. Data Lifecycle Boundary

Data SHOULD follow a defined lifecycle:

1. creation
2. validation
3. storage
4. use
5. update
6. archival
7. deletion

Retention MUST be based on documented requirements.

Unused data SHOULD NOT be retained indefinitely without justification.

---

## 56. Failure Isolation

Failure in one domain SHOULD NOT unnecessarily bring down unrelated domains.

Architecture SHOULD use:

- boundaries
- timeouts
- retries
- queues
- fallback mechanisms
- circuit breakers
- isolation

Failure behavior MUST be documented for critical services.

---

## 57. Performance Boundary

Performance-sensitive components MUST have identifiable boundaries.

Performance optimization MUST be based on evidence such as:

- profiling
- measurements
- benchmarks
- production metrics

Premature optimization MUST NOT unnecessarily complicate architecture.

---

## 58. Scalability Boundary

Scalable components MUST identify their scaling model.

Possible models include:

- vertical scaling
- horizontal scaling
- asynchronous processing
- caching
- partitioning
- queue-based workloads

Scaling decisions MUST remain traceable to actual system requirements.

---

## 59. Reliability Boundary

Critical services SHOULD define:

- availability expectations
- failure modes
- recovery behavior
- health checks
- retry behavior
- data integrity requirements

Reliability MUST be measured rather than assumed.

---

## 60. Change Management Boundary

Architectural changes MUST follow controlled change management.

Significant changes SHOULD include:

- reason
- affected components
- dependency impact
- security impact
- migration requirements
- testing requirements
- rollback strategy
- documentation impact

---

## 61. Structural Change Rule

Changes to folder architecture MUST NOT be made casually.

Structural changes include:

- creating folders
- deleting folders
- moving domains
- renaming architectural folders
- changing ownership
- changing dependency direction

Such changes MUST be documented.

---

## 62. Folder Creation Rule

Before creating a permanent folder, verify:

1. existing folders cannot responsibly contain the responsibility
2. the responsibility is architecturally meaningful
3. ownership is defined
4. dependencies are understood
5. documentation is updated
6. tests are considered

Only then SHOULD the folder be created.

---

## 63. Folder Removal Rule

A folder MUST NOT be deleted merely because it is currently unused.

Before removal:

- identify dependents
- migrate required contents
- update documentation
- update references
- verify tests
- verify deployment
- verify Git history requirements

Removal MUST be deliberate.

---

## 64. Folder Rename Rule

Folder renames MUST consider:

- imports
- scripts
- deployment
- documentation
- CI/CD
- references
- tests
- external integrations

A rename is an architectural change, not merely a cosmetic change.

---

## 65. Documentation Synchronization

When folder architecture changes, related documentation MUST be reviewed.

At minimum, review:

- 07_PROJECT_STRUCTURE.md
- 08_FOLDER_ARCHITECTURE.md
- relevant registries
- project memory
- changelog
- decision records

---

## 66. Living Blueprint Integration

The Folder Architecture MUST remain compatible with the Living Blueprint
System.

Structural evolution MUST be represented through controlled blueprint
updates.

The blueprint MUST NOT claim a folder exists when the repository state does
not support that claim.

---

## 67. Digital DNA Integration

Folder architecture forms part of the project's Digital DNA.

Important structural properties SHOULD remain reproducible from documented
rules.

Structural identity MUST remain stable across controlled versions.

---

## 68. Project Memory Integration

Important folder decisions MUST be recorded in project memory.

Project memory SHOULD preserve:

- why a folder exists
- major structural decisions
- deprecated structures
- migration history
- architectural constraints

---

## 69. Decision Registry Integration

Significant architectural folder decisions MUST be represented in the
Decision Registry when they affect long-term architecture.

Examples include:

- new root domain
- major folder merge
- domain split
- dependency direction change
- infrastructure relocation

---

## 70. Feature Registry Integration

Features SHOULD reference the folders responsible for their implementation.

A feature MUST NOT rely solely on folder names as its architectural
definition.

Feature ownership MUST remain traceable.

---

## 71. Module Registry Integration

Important modules MUST identify their parent architectural domain.

The Module Registry SHOULD provide:

- module name
- purpose
- location
- owner
- dependencies
- status
- testing state

---

## 72. API Registry Integration

APIs MUST identify their implementation boundary.

The API Registry SHOULD identify:

- endpoint
- owner
- purpose
- version
- authentication
- authorization
- consumer
- status

---

## 73. Database Registry Integration

Database components SHOULD identify:

- schema
- owner
- purpose
- migrations
- consumers
- sensitivity
- status

Database architecture MUST remain traceable to folder ownership.

---

## 74. AI Registry Integration

AI components SHOULD identify:

- AI capability
- implementation location
- model dependency
- owner
- inputs
- outputs
- verification
- status

AI architecture MUST remain traceable to ai-core boundaries.

---

## 75. Development Workflow

Folder-aware development SHOULD follow:

1. understand responsibility
2. identify owning domain
3. identify dependencies
4. modify implementation
5. update tests
6. update documentation
7. verify structural consistency
8. review Git diff
9. commit
10. push
11. update project progress when the milestone is complete

---

## 76. Structural Quality Gate

A folder architecture change passes its quality gate only when:

- purpose is clear
- ownership is clear
- naming is valid
- dependencies are understood
- security boundaries are preserved
- documentation is synchronized
- tests are considered
- Git verification passes

---

## 77. Repository Health

Repository health MUST be periodically verified.

Minimum checks MAY include:

- expected folders exist
- unexpected architectural folders are identified
- Git status is understood
- documentation references are valid
- dependency boundaries remain valid
- tests remain discoverable
- deployment structure remains valid

---

## 78. Anti-Patterns

The following are prohibited as permanent architecture without explicit
justification:

- misc/
- random/
- stuff/
- dumping unrelated files into root
- duplicate domain folders
- circular domain dependencies
- hidden architectural boundaries
- undocumented generated architecture
- secret-containing folders
- temporary folders treated as permanent

---

## 79. Temporary Folder Rule

Temporary files MAY exist during development when necessary.

Temporary folders MUST:

- be clearly identifiable
- have limited lifetime
- not become architectural dependencies
- not contain required production state
- be cleaned when no longer needed

---

## 80. Generated Content Rule

Generated files MUST be distinguishable from authored source.

Generated content SHOULD include reproducible generation instructions.

Generated artifacts MUST NOT become the only source of truth when source
definitions exist elsewhere.

---

## 81. Compatibility Principle

Folder architecture SHOULD evolve without unnecessary breakage.

When compatibility cannot be preserved, the migration MUST be explicit.

Long-lived integrations SHOULD use stable interfaces rather than internal
folder assumptions.

---

## 82. Long-Term Expansion

Future system expansion MAY introduce additional domains such as:

- analytics
- automation
- intelligence services
- plugins
- marketplace
- research
- advanced hardware
- distributed services

Future domains MUST follow the same architectural governance.

Expansion MUST NOT bypass existing constitutional and security rules.

---

## 83. Architecture Documentation Completeness

Folder architecture documentation is complete only when it defines:

- root domains
- folder responsibilities
- ownership
- dependency direction
- naming
- boundaries
- security
- data
- testing
- deployment
- change management
- integration with project governance

---

## 84. Implementation Readiness

Folder architecture is implementation-ready when:

- all required root domains are defined
- responsibilities are documented
- dependency direction is established
- security boundaries are defined
- naming rules are defined
- structural change rules are defined
- verification requirements are defined

Implementation readiness MUST NOT be confused with implementation completion.

---

## 85. Definition of Done

This specification is DONE when:

1. all planned sections are present
2. root domains are documented
3. folder responsibilities are documented
4. ownership rules are documented
5. dependency rules are documented
6. security boundaries are documented
7. data boundaries are documented
8. testing boundaries are documented
9. deployment boundaries are documented
10. structural change rules are documented
11. governance integrations are documented
12. verification requirements are documented
13. Git validation passes
14. the specification is committed
15. the specification is pushed
16. project progress is updated

---

## 86. Authority Statement

This specification defines the folder-level architectural structure of
BI-BUGS EMPIRE OS X.

It does not override:

- the Engineering Constitution
- the Master Blueprint
- higher-level security rules
- user authority
- explicit architectural decisions

Where conflicts occur, the higher-authority document prevails.

---

## 87. Current Status

Specification:

08_FOLDER_ARCHITECTURE.md

Status:

IN PROGRESS

Documentation:

UNDER DEVELOPMENT

Implementation:

NOT STARTED

Testing:

NOT STARTED

Deployment:

NOT STARTED

Production:

NOT STARTED

This status MUST be updated after the specification passes verification
and is committed.

---

## 88. Final Architectural Principle

The folder structure is a physical representation of system architecture.

Every important architectural boundary SHOULD be visible in the repository.

Every folder MUST have a reason.

Every dependency MUST have a direction.

Every structural change MUST have an explanation.

Every important decision MUST remain traceable.

The repository MUST remain understandable as the system grows.

BI-BUGS EMPIRE OS X MUST evolve without allowing folder structure to become
an uncontrolled accumulation of files.

The architecture exists to preserve clarity, ownership, security,
maintainability, scalability, and long-term evolution.
