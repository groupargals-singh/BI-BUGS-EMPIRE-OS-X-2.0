# AI Rules

**Status:** Draft supporting rules; canonical specifications govern.

Canonical sources: `../MASTER_SPECIFICATION/11_AI_CORE.md`, `../MASTER_SPECIFICATION/24_AI_REGISTRY.md`, and `../MASTER_SPECIFICATION/15_SECURITY.md`.

- Treat model outputs, retrieved pages, and tool responses as untrusted until validated.
- Separate generation, retrieval, verification, and execution responsibilities.
- Ground factual answers in traceable sources; express uncertainty and abstain when evidence is inadequate.
- Enforce permissions in code and request approval for protected actions.
- Evaluate prompt injection, privacy leakage, harmful tool calls, grounding, latency, and regressions after changes.
- Do not claim AI quality or production readiness without reproducible evaluation evidence.