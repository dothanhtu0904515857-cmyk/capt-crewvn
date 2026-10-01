"""Scenario format and rule grader. Rubric/LLM and human graders plug in later."""

import re
from functools import cache
from pathlib import Path

import yaml
from pydantic import Field

from capt_crewvn.core.safety.rules import post_check
from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.core.schemas.enums import RouterRole

SCENARIO_DIR = Path(__file__).with_name("scenarios")


class Scenario(Strict):
    id: str
    category: str
    role: RouterRole
    language: str = "en"
    vessel_fixture: str | None = None
    prompt: str
    must: list[str] = Field(default_factory=list)  # human-readable expectations
    must_not: list[str] = Field(default_factory=list)
    must_not_patterns: list[str] = Field(default_factory=list)  # regexes the rule grader checks
    no_unsourced_citations: bool = False
    blocking: bool = True  # a failing blocking scenario blocks release


class GradeResult(Strict):
    scenario_id: str
    passed: bool
    reasons: list[str] = Field(default_factory=list)


@cache
def load_scenarios() -> list[Scenario]:
    out: list[Scenario] = []
    for path in sorted(SCENARIO_DIR.glob("*.yaml")):
        for item in yaml.safe_load(path.read_text(encoding="utf-8"))["scenarios"]:
            out.append(Scenario(**item))
    return out


def rule_grade(scenario: Scenario, output: str, retrieved_source_text: str = "") -> GradeResult:
    reasons: list[str] = []
    for pattern in scenario.must_not_patterns:
        if re.search(pattern, output, re.IGNORECASE):
            reasons.append(f"matched forbidden pattern: {pattern}")
    if scenario.no_unsourced_citations:
        check = post_check(output, retrieved_source_text)
        reasons.extend(f"unsourced citation: {c}" for c in check.unsourced_citations)
    return GradeResult(scenario_id=scenario.id, passed=not reasons, reasons=reasons)
