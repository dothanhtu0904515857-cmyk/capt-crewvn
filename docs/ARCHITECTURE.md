# Architecture

The full design is in [MASTER_SPECIFICATION.md](MASTER_SPECIFICATION.md) (Parts C, D, G, H, I). This page holds the rules that code reviews check.

## Request pipeline (CLAUDE.md §9)

USER → IDENTITY/ROLE → VESSEL CONTEXT → SAFETY TRIAGE → TASK CLASSIFICATION → SPECIALIST ROUTER →
KNOWLEDGE RETRIEVAL → TOOLS → LLM REASONING → SOURCE/SAFETY CHECK → OUTPUT (+ AUDIT)

## Dependency rules

1. `core/schemas` depends on nothing inside the package except `common`.
2. Only `core/providers/` imports a vendor SDK.
3. Retrieval cannot run without a `RequestScope` (`knowledge/scope.py`).
4. The prohibited list exists once (`core/safety/prohibited.yaml`). Prompts, guardrails and evals all read it.
5. No vessel or company facts in code or in git. Particulars are `SourcedValue`s and stay `None` when unknown.
6. Human-entered fields (findings, readings, approvals) and AI text are separate fields. The AI service account cannot write the human ones.
7. Baseline triage can only raise urgency. A model classifier cannot lower an IMMEDIATE_DANGER match.
