"""Access to the canonical prohibited list and the output post-check."""

import re
from functools import cache
from pathlib import Path

import yaml
from pydantic import Field

from capt_crewvn.core.schemas.common import Strict

PROHIBITED_FILE = Path(__file__).with_name("prohibited.yaml")

# Patterns that look like a specific regulatory citation. If an output contains one,
# the request context must hold a retrieved source supporting it (CLAUDE.md §12).
CITATION_PATTERNS = [
    re.compile(r"\b(SOLAS|MARPOL|STCW|COLREGs?|MLC|IMSBC|IMDG|ISM|ISPS|BWM)\b[^.\n]{0,20}?\b(reg(ulation)?|rule|annex|chapter|section|code)\.?\s*[IVX0-9]", re.I),
    re.compile(r"\bResolution\s+[A-Z]{1,4}\.\s?\d+", re.I),
    re.compile(r"\b(MSC|MEPC)\.\d+\(\d+\)", re.I),
    re.compile(r"\bMSC\.\d+/Circ\.\d+", re.I),
]


@cache
def prohibited_items() -> list[dict]:
    return yaml.safe_load(PROHIBITED_FILE.read_text(encoding="utf-8"))["items"]


class PostCheckResult(Strict):
    unsourced_citations: list[str] = Field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.unsourced_citations


def find_citations(text: str) -> list[str]:
    found: list[str] = []
    for pattern in CITATION_PATTERNS:
        found.extend(m.group(0) for m in pattern.finditer(text))
    return found


def post_check(output_text: str, retrieved_source_text: str = "") -> PostCheckResult:
    """Flag regulation-like citations that do not appear in the retrieved sources."""
    normalised_sources = retrieved_source_text.lower()
    unsourced = [c for c in find_citations(output_text) if c.lower() not in normalised_sources]
    return PostCheckResult(unsourced_citations=unsourced)
