# ADR 0003 — No platform copies of regulatory publications in v1

Status: Accepted (2026-10-01, owner chose default recommendations)

**Decision.** Capt Crewvn does not store IMO, Class or Flag publication texts in v1. It cites frameworks by name and uses only documents that a company is entitled to upload. `search_regulation` returns MISSING_SOURCE when nothing has been ingested.

**Consequences.** Exact regulatory answers depend on tenant uploads. The model must state that verification is needed when no source is available (CLAUDE.md §12).
