# ADR 0002 — Technology stack

Status: Accepted (2026-10-01, owner chose default recommendations)

**Decision.** Python 3.11+ with pydantic v2 for `capt_crewvn` and a FastAPI backend, a TypeScript/React frontend, and PostgreSQL with pgvector. The hosting provider is chosen in Phase 7.

**Consequences.** One database holds both entities and vectors. Tenant scoping is enforced in SQL filters as well as in vector namespaces.
