"""Baseline safety triage.

This deterministic keyword pass runs before any model call so that an obvious
emergency is never routed as a study question. It is a floor, not the whole
triage: a model-based classifier can raise urgency but never lower a match
found here (Spec Part C §6).
"""

import re
from functools import cache
from pathlib import Path

import yaml

from capt_crewvn.core.schemas.enums import TaskUrgency

SIGNALS_FILE = Path(__file__).with_name("danger_signals.yaml")


@cache
def _patterns() -> list[re.Pattern[str]]:
    data = yaml.safe_load(SIGNALS_FILE.read_text(encoding="utf-8"))
    terms = [term for lang in data["immediate_danger"].values() for term in lang]
    return [re.compile(re.escape(t), re.IGNORECASE) for t in terms]


def baseline_triage(message: str) -> TaskUrgency | None:
    """Return IMMEDIATE_DANGER when a danger signal appears, else None (undecided)."""
    if any(p.search(message) for p in _patterns()):
        return TaskUrgency.IMMEDIATE_DANGER
    return None
