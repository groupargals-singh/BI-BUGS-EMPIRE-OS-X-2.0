# AI Core — Supporting Guide

**Status:** Supporting guide; defer to the canonical specification.

Canonical source: `MASTER_SPECIFICATION/11_AI_CORE.md`.
Related sources: `MASTER_SPECIFICATION/12_KNOWLEDGE_GRAPH.md`, `MASTER_SPECIFICATION/24_AI_REGISTRY.md`, `MASTER_SPECIFICATION/15_SECURITY.md`, and `MASTER_SPECIFICATION/18_TESTING.md`.

## Required boundaries
- Separate model output from verified facts and approved actions.
- Track provider/model/version, configuration, data exposure, permissions, latency, and evaluation evidence for each AI component.
- Treat retrieved content and tool output as untrusted input; enforce permissions outside the model.
- Test grounding, uncertainty, prompt injection, privacy leakage, fallback behavior, and regressions.

This summary does not claim that an AI runtime, evaluation pipeline, or production integration is implemented.

## BI-BUGS current AI boundary

AI is not a first-release dependency, and no BI-BUGS AI runtime/provider is verified. Any AI capability requires a specific owner-approved business use case, data/privacy review, evaluation thresholds, permission boundaries, human oversight, cost/latency limits, fallback, and disable path. The canonical specifications remain 11, 15, 18, and 24.
