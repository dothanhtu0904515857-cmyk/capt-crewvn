# ADR 0001 — Vendor-neutral model provider

Status: Accepted (2026-10-01)

**Context.** CLAUDE.md §2 forbids tight coupling to one LLM vendor.

**Decision.** There is one `ModelProvider` protocol in `core/providers/base.py`, and only adapters in that package import vendor SDKs. Prompts, schemas, evals and knowledge are provider-neutral. Before any provider switch, the blocking eval set must pass on the new provider.

**Consequences.** Vendor-specific features such as caching or vision go behind capability flags. Some duplication in adapters is accepted.
