from enum import StrEnum
from functools import cache
from pathlib import Path

import yaml
from pydantic import Field

from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.core.schemas.enums import Department

SEED_FILE = Path(__file__).with_name("seed.yaml")
SOURCES_DIR = Path(__file__).with_name("sources")
DECISIONS_FILE = Path(__file__).with_name("decisions.yaml")


class TermStatus(StrEnum):
    IMPORTED = "IMPORTED"  # copied from an owner source, consistent within that source
    NEEDS_REVIEW = "NEEDS_REVIEW"  # source gives several renderings, or column order was inferred
    VARIANT = "VARIANT"  # kept for search only; an owner decision chose another rendering
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
    source_variants: dict[str, list[dict]] | None = None
    decision_ref: str | None = None


@cache
def seed_terms() -> list[Term]:
    data = yaml.safe_load(SEED_FILE.read_text(encoding="utf-8"))
    return [Term(**t) for t in data["terms"]]


@cache
def protected_abbreviations() -> list[str]:
    return yaml.safe_load(SEED_FILE.read_text(encoding="utf-8"))["protected_abbreviations"]


@cache
def decisions() -> list[dict]:
    return yaml.safe_load(DECISIONS_FILE.read_text(encoding="utf-8"))["decisions"]


@cache
def imported_terms() -> list[Term]:
    """Source files with owner decisions applied (sources themselves are never edited)."""
    variant_notes: dict[str, tuple[str, str]] = {}
    for d in decisions():
        for term_id, note in d.get("effect", {}).get("variant_terms", {}).items():
            variant_notes[term_id] = (d["id"], note)
    terms: list[Term] = []
    for path in sorted(SOURCES_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        for raw in data["terms"]:
            term = Term(**raw)
            if term.term_id in variant_notes:
                ref, note = variant_notes[term.term_id]
                term = term.model_copy(update={"status": TermStatus.VARIANT, "decision_ref": ref, "context_notes": note})
            terms.append(term)
    return terms


@cache
def all_terms() -> list[Term]:
    """Seed terms first; an imported term with the same English is shadowed by the seed entry."""
    seed = seed_terms()
    seen = {t.canonical_en.lower() for t in seed}
    return [*seed, *(t for t in imported_terms() if t.canonical_en.lower() not in seen)]


def lookup(text: str) -> list[Term]:
    """Exact, case-insensitive match on English, Vietnamese or Chinese."""
    needle = text.strip().lower()
    return [
        t
        for t in all_terms()
        if needle in {t.canonical_en.lower(), (t.vi or "").lower(), (t.zh_hans or "").lower()}
        or needle in (v.lower() for v in t.vi_informal)
    ]
