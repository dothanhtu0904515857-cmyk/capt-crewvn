from enum import StrEnum
from functools import cache
from pathlib import Path

import yaml
from pydantic import Field

from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.core.schemas.enums import Department

SEED_FILE = Path(__file__).with_name("seed.yaml")


class TermStatus(StrEnum):
    PROPOSED = "PROPOSED"
    REVIEWED = "REVIEWED"
    APPROVED = "APPROVED"


class Term(Strict):
    term_id: str
    canonical_en: str
    vi: str | None = None
    vi_informal: list[str] = Field(default_factory=list)
    zh_hans: str | None = None
    pinyin: str | None = None
    abbreviation: list[str] = Field(default_factory=list)
    synonyms: dict[str, list[str]] = Field(default_factory=dict)
    department: Department | None = None
    equipment_category: str | None = None
    context_notes: str | None = None
    source: str
    status: TermStatus = TermStatus.PROPOSED


@cache
def seed_terms() -> list[Term]:
    data = yaml.safe_load(SEED_FILE.read_text(encoding="utf-8"))
    return [Term(**t) for t in data["terms"]]


@cache
def protected_abbreviations() -> list[str]:
    return yaml.safe_load(SEED_FILE.read_text(encoding="utf-8"))["protected_abbreviations"]
