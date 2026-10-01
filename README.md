# Capt Crewvn — Maritime AI Platform

Capt Crewvn is a role-aware, vessel-aware, safety-first maritime AI platform for ship and shore professionals.
It grew out of the Cargo Ship Captain methodology. The rules for working in this repository are in [CLAUDE.md](CLAUDE.md).

**Status:** Phase 1 scaffold. Schemas, safety rules, router contracts, role and module catalogs, terminology seed
and the safety eval set are in place. There is no model integration, API or UI yet.

## Layout

| Path | What lives there |
|---|---|
| `capt_crewvn/core/system/` | Core instruction fragments (versioned prompt text) |
| `capt_crewvn/core/router/` | Role router contract, baseline safety triage |
| `capt_crewvn/core/safety/` | Canonical prohibited list, output post-check |
| `capt_crewvn/core/terminology/` | Vietnamese / English / Simplified Chinese term base |
| `capt_crewvn/core/providers/` | LLM provider interface (the only place a vendor SDK may be imported) |
| `capt_crewvn/core/schemas/` | Typed entities: Vessel, Company, Document, InspectionItem, Report… |
| `capt_crewvn/roles/` | One profile per router role |
| `capt_crewvn/skills/` | One contract per specialist module |
| `capt_crewvn/knowledge/` | Retrieval and tenant-scope filtering |
| `capt_crewvn/tools/`, `reports/`, `audit/` | Tool contract, report rendering, audit events |
| `capt_crewvn/evaluation/` | Maritime safety scenarios and grader |
| `backend/`, `frontend/`, `database/`, `deployment/` | Placeholders for later phases |
| `docs/` | Master specification, architecture, roadmap, sources, ADRs |

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

No vessel or company data is ever committed. Secrets go in `.env` (see `.env.example`), never in code.
