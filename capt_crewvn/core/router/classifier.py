"""Role router classifier (CLAUDE.md §9, Spec Part E.5).

Two stages, both producing the same ``RouteDecision``:

1. ``rule_route`` — deterministic. Department from the role profile, urgency from
   baseline triage, modules from vi/en/zh keyword hints, missing context from the
   selected modules' required inputs.
2. ``llm_route`` — optional refinement through any ``ModelProvider``. The model's
   JSON is validated against the enums and module catalogue; anything invalid is
   dropped. It can add modules and raise urgency, never lower urgency below the
   rule result, so a detected emergency always stays an emergency.
"""

import json
import re
from functools import cache
from pathlib import Path

import yaml

from capt_crewvn.core.providers.base import Message, ModelProvider
from capt_crewvn.core.router.catalog import module_definitions, role_profiles
from capt_crewvn.core.router.decision import RouteDecision
from capt_crewvn.core.router.triage import baseline_triage
from capt_crewvn.core.schemas.enums import Department, RouterRole, TaskUrgency

KEYWORDS_FILE = Path(__file__).with_name("module_keywords.yaml")
FALLBACK_MODULE = "captain-adviser"
EMERGENCY_MODULE = "grounding-emergency"
STUDY_MODULES = {"maritime-training", "shipping-industry"}
STUDY_ROLES = {RouterRole.CADET, RouterRole.MARITIME_STUDENT}
VESSEL_INPUTS = {"vessel", "vessel particulars"}

URGENCY_ORDER = [TaskUrgency.STUDY, TaskUrgency.ROUTINE, TaskUrgency.URGENT, TaskUrgency.IMMEDIATE_DANGER]


@cache
def _keyword_patterns() -> dict[str, list[re.Pattern[str]]]:
    data = yaml.safe_load(KEYWORDS_FILE.read_text(encoding="utf-8"))
    patterns: dict[str, list[re.Pattern[str]]] = {}
    for module_id, langs in data.items():
        compiled = [re.compile(rf"(?<!\w){re.escape(t)}(?!\w)", re.IGNORECASE) for t in langs.get("en", [])]
        compiled += [re.compile(re.escape(t), re.IGNORECASE) for t in langs.get("vi", []) + langs.get("zh", [])]
        patterns[module_id] = compiled
    return patterns


def match_modules(message: str) -> list[str]:
    """Module ids whose keywords appear, most hits first (ties keep catalogue order)."""
    hits = {m: sum(1 for p in ps if p.search(message)) for m, ps in _keyword_patterns().items()}
    ranked = sorted((m for m, n in hits.items() if n), key=lambda m: -hits[m])
    return ranked


def _higher(a: TaskUrgency, b: TaskUrgency) -> TaskUrgency:
    return max(a, b, key=URGENCY_ORDER.index)


def _missing_context(modules: list[str], vessel_id: str | None, company_id: str | None, danger: bool) -> list[str]:
    catalogue = module_definitions()
    missing: list[str] = []
    needs_vessel = danger or any(
        VESSEL_INPUTS & set(catalogue.get(m, {}).get("required_inputs", [])) for m in modules
    )
    if needs_vessel and not vessel_id:
        missing.append("vessel")
    if vessel_id and not company_id:
        missing.append("company")
    return missing


def rule_route(
    message: str,
    router_role: RouterRole,
    vessel_id: str | None = None,
    company_id: str | None = None,
) -> RouteDecision:
    profile = role_profiles()[router_role]
    danger = baseline_triage(message) == TaskUrgency.IMMEDIATE_DANGER
    catalogue = module_definitions()
    modules = [m for m in match_modules(message) if m in catalogue]
    if danger and EMERGENCY_MODULE in modules:
        modules.remove(EMERGENCY_MODULE)
        modules.insert(0, EMERGENCY_MODULE)
    if not modules:
        modules = [FALLBACK_MODULE]

    if danger:
        urgency = TaskUrgency.IMMEDIATE_DANGER
    elif set(modules) <= STUDY_MODULES or (router_role in STUDY_ROLES and not vessel_id):
        urgency = TaskUrgency.STUDY
    else:
        urgency = TaskUrgency.ROUTINE

    return RouteDecision(
        router_role=router_role,
        department=Department(profile["department"]),
        vessel_id=vessel_id,
        company_id=company_id,
        urgency=urgency,
        immediate_danger=danger,
        modules=modules,
        precedence_profile=catalogue[modules[0]].get("precedence_profile", "VESSEL_OPERATIONAL"),
        missing_context=_missing_context(modules, vessel_id, company_id, danger),
    )


ROUTER_INSTRUCTION = """You classify one maritime user message for routing. Do not answer it.
Return only a JSON object with these keys:
  "modules": list of module ids, most relevant first, chosen only from: {modules}
  "urgency": one of {urgencies}
  "operation": short phrase naming the shipboard operation, or null
  "task_type": one of "question", "procedure", "troubleshooting", "report", "checklist", "translation", "study", or null
Choose IMMEDIATE_DANGER whenever life, the vessel or the environment may be at immediate risk."""


def llm_route(message: str, base: RouteDecision, provider: ModelProvider) -> RouteDecision:
    """Refine a rule decision with a model. Invalid output leaves ``base`` unchanged."""
    catalogue = module_definitions()
    instruction = ROUTER_INSTRUCTION.format(
        modules=", ".join(sorted(catalogue)), urgencies=", ".join(u.value for u in URGENCY_ORDER)
    )
    response = provider.generate(
        [Message(role="system", content=instruction), Message(role="user", content=message)],
        max_output_tokens=400,
    )
    if response.refused:
        return base
    parsed = _parse_json_object(response.text)
    if parsed is None:
        return base

    llm_modules = [m for m in parsed.get("modules") or [] if isinstance(m, str) and m in catalogue]
    rule_modules = [m for m in base.modules if m != FALLBACK_MODULE or not llm_modules]
    modules = list(dict.fromkeys(llm_modules + rule_modules)) or base.modules
    if base.immediate_danger and EMERGENCY_MODULE in modules:
        modules.remove(EMERGENCY_MODULE)
        modules.insert(0, EMERGENCY_MODULE)

    try:
        llm_urgency = TaskUrgency(parsed.get("urgency"))
    except ValueError:
        llm_urgency = base.urgency
    urgency = _higher(base.urgency, llm_urgency)
    danger = urgency == TaskUrgency.IMMEDIATE_DANGER

    return base.model_copy(
        update={
            "modules": modules,
            "urgency": urgency,
            "immediate_danger": danger,
            "operation": _short_text(parsed.get("operation")) or base.operation,
            "task_type": _short_text(parsed.get("task_type")) or base.task_type,
            "precedence_profile": catalogue[modules[0]].get("precedence_profile", base.precedence_profile),
            "missing_context": _missing_context(modules, base.vessel_id, base.company_id, danger),
        }
    )


def route(
    message: str,
    router_role: RouterRole,
    vessel_id: str | None = None,
    company_id: str | None = None,
    provider: ModelProvider | None = None,
) -> RouteDecision:
    decision = rule_route(message, router_role, vessel_id, company_id)
    return llm_route(message, decision, provider) if provider else decision


def _parse_json_object(text: str) -> dict | None:
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end <= start:
        return None
    try:
        value = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) else None


def _short_text(value: object) -> str | None:
    return value.strip()[:80] if isinstance(value, str) and value.strip() else None
