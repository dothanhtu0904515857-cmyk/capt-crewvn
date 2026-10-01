"""Importer for source 02: "Tài liệu tam ngữ học Việt Anh Trung Crewvn 2026 bản Full" (PDF).

Input is the text produced by ``pdftotext -layout`` (pages separated by form feeds).
The document has two entry shapes:

* numbered entries ``N. <vi|en> → <en|vi> → 中文 → Pinyin`` (also with ``–``), and
* six-column tables ``Trang PDF | Mục | STT | Việt | English | 中文 | Pinyin``.

The importer copies the source as written. Where the same English term appears with
different Vietnamese or Chinese renderings, the most frequent rendering becomes the
working value and every variant is kept with its pages, and the term is marked
NEEDS_REVIEW. Nothing is corrected from general knowledge.

Usage:
    python -m capt_crewvn.core.terminology.importers.crewvn_trilingual <text.txt> <out.yaml> [<review.csv>]
"""

import collections
import csv
import re
import sys
from pathlib import Path

import yaml

SOURCE_ID = "02"
SOURCE_TITLE = "Tài liệu tam ngữ học Việt Anh Trung Crewvn 2026 bản Full (PDF)"

CJK = re.compile(r"[㐀-鿿]")
VI = re.compile(
    r"[ăâđêôơưàáạảãằắặẳẵầấậẩẫèéẹẻẽềếệểễìíịỉĩòóọỏõồốộổỗờớợởỡùúụủũừứựửữỳýỵỷỹ]",
    re.IGNORECASE,
)
ENTRY = re.compile(r"^\s*(\d+[A-Z]?)\.\s+(.+)$")
SEP = re.compile(r"\s*(?:→|–)\s*")
TABLE_ROW = re.compile(r"^\s*(\d+)\s+(\d+(?:\.[0-9A-Z]+)+)\s+(\d+[A-Z]?)\s+(.*)$")
TABLE_ROW_NAMED = re.compile(r"^\s*(\d+)\s+(\d+\.\d+)\s+(.+?)\s+(\d+[A-Z]?)\s{2,}(.*)$")


def _norm(text: str | None) -> str:
    return re.sub(r"\s+", " ", (text or "").replace("’", "'")).strip()


class _Parser:
    def __init__(self) -> None:
        self.order = "vi_first"  # order of the last unambiguous entry, used for ambiguous ones

    def entry(self, body: str) -> dict | None:
        parts = [p.strip() for p in SEP.split(body) if p.strip()]
        zh = [p for p in parts if CJK.search(p)]
        if len(zh) != 1 or len(parts) not in (3, 4) or parts.index(zh[0]) != 2:
            return None
        a, b = parts[0], parts[1]
        ambiguous = False
        if VI.search(a) and not VI.search(b):
            vi, en, self.order = a, b, "vi_first"
        elif VI.search(b) and not VI.search(a):
            vi, en, self.order = b, a, "en_first"
        else:
            ambiguous = True
            vi, en = (a, b) if self.order == "vi_first" else (b, a)
        return {"vi": vi, "en": en, "zh": parts[2], "pinyin": parts[3] if len(parts) == 4 else None,
                "order_inferred": ambiguous}

    @staticmethod
    def table(cells: str) -> dict | None:
        tokens = cells.split()
        zi = next((i for i, tk in enumerate(tokens) if CJK.search(tk)), None)
        if zi is None:
            return None
        left = cells[: cells.index(tokens[zi])].strip()
        columns = re.split(r"\s{2,}", left)
        inferred = False
        if len(columns) == 1:
            words = columns[0].split()
            vi_idx = [i for i, w in enumerate(words) if VI.search(w)]
            if not vi_idx:
                return None
            k = vi_idx[-1] + 1
            en = words[k:]
            if not en or any(VI.search(w) for w in en) or not (en[0][0].isupper() or en[0][0].isdigit()):
                return None
            columns, inferred = [" ".join(words[:k]), " ".join(en)], True
        if len(columns) != 2:
            return None
        return {"vi": columns[0], "en": columns[1], "zh": tokens[zi], "pinyin": " ".join(tokens[zi + 1 :]) or None,
                "order_inferred": inferred}


def parse(text: str) -> tuple[list[dict], list[dict]]:
    parser = _Parser()
    found: list[dict] = []
    unparsed: list[dict] = []
    for page_no, page in enumerate(text.split("\f"), start=1):
        for line in page.split("\n"):
            if not CJK.search(line):
                continue
            record = None
            m = TABLE_ROW.match(line)
            if m:
                record = parser.table(m.group(4))
            elif (m := TABLE_ROW_NAMED.match(line)):
                record = parser.table(m.group(5))
            elif (m := ENTRY.match(line)) and ("→" in line or "–" in line):
                record = parser.entry(m.group(2))
            else:
                continue
            if record is None:
                unparsed.append({"page": page_no, "line": line.strip()})
            else:
                record["page"] = page_no
                found.append(record)
    return found, unparsed


def _term_id(en: str, used: set[str]) -> str:
    base = re.sub(r"[^A-Z0-9]+", "_", en.upper()).strip("_") or "TERM"
    tid, n = base, 2
    while tid in used:
        tid, n = f"{base}_{n}", n + 1
    used.add(tid)
    return tid


def consolidate(records: list[dict]) -> list[dict]:
    groups: dict[str, list[dict]] = collections.defaultdict(list)
    display: dict[str, str] = {}
    for r in records:
        key = _norm(r["en"]).lower().rstrip(".")
        groups[key].append(r)
        display.setdefault(key, _norm(r["en"]).rstrip("."))
    used: set[str] = set()
    terms = []
    for key in sorted(groups):
        rows = groups[key]
        vi_counts = collections.Counter(_norm(r["vi"]) for r in rows)
        zh_counts = collections.Counter(_norm(r["zh"]) for r in rows)
        vi_main = vi_counts.most_common(1)[0][0]
        zh_main = zh_counts.most_common(1)[0][0]
        pinyin = next((_norm(r["pinyin"]) for r in rows if _norm(r["zh"]) == zh_main and r["pinyin"]), None)
        pages = sorted({r["page"] for r in rows})

        def variants(field: str, counts: collections.Counter) -> list[dict]:
            return [
                {"value": v, "count": c, "pages": sorted({r["page"] for r in rows if _norm(r[field]) == v})}
                for v, c in counts.most_common()
            ]

        needs_review = len(vi_counts) > 1 or len(zh_counts) > 1 or any(r["order_inferred"] for r in rows)
        term = {
            "term_id": _term_id(display[key], used),
            "canonical_en": display[key],
            "vi": vi_main,
            "zh_hans": zh_main,
            "pinyin": pinyin,
            "source": f"{SOURCE_ID} {SOURCE_TITLE}, pp. {pages[0]}–{pages[-1]}" if len(pages) > 1
            else f"{SOURCE_ID} {SOURCE_TITLE}, p. {pages[0]}",
            "status": "NEEDS_REVIEW" if needs_review else "IMPORTED",
        }
        if len(vi_counts) > 1 or len(zh_counts) > 1:
            term["context_notes"] = "Source gives more than one rendering; working value is the most frequent."
            term["source_variants"] = {"vi": variants("vi", vi_counts), "zh_hans": variants("zh", zh_counts)}
        terms.append(term)
    return terms


def write_review_csv(terms: list[dict], unparsed: list[dict], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["status", "term_id", "English", "Việt (working)", "中文 (working)", "Việt variants", "中文 variants",
                    "pages", "owner decision"])
        for t in terms:
            if t["status"] != "NEEDS_REVIEW":
                continue
            sv = t.get("source_variants", {})
            fmt = lambda vs: " | ".join(f"{v['value']} (×{v['count']}, p.{','.join(map(str, v['pages'][:6]))})" for v in vs)
            w.writerow([t["status"], t["term_id"], t["canonical_en"], t["vi"], t["zh_hans"],
                        fmt(sv.get("vi", [])) if len(sv.get("vi", [])) > 1 else "",
                        fmt(sv.get("zh_hans", [])) if len(sv.get("zh_hans", [])) > 1 else "",
                        t["source"].rsplit(", ", 1)[-1], ""])
        for u in unparsed:
            w.writerow(["UNPARSED", "", "", "", "", "", "", f"p. {u['page']}", u["line"]])


def main(argv: list[str]) -> None:
    text = Path(argv[1]).read_text(encoding="utf-8")
    records, unparsed = parse(text)
    terms = consolidate(records)
    doc = {
        "source_id": SOURCE_ID,
        "source_title": SOURCE_TITLE,
        "importer": "capt_crewvn.core.terminology.importers.crewvn_trilingual",
        "entries_read": len(records),
        "lines_not_parsed": len(unparsed),
        "terms": terms,
    }
    Path(argv[2]).write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=200), encoding="utf-8")
    if len(argv) > 3:
        write_review_csv(terms, unparsed, Path(argv[3]))
    review = sum(t["status"] == "NEEDS_REVIEW" for t in terms)
    print(f"entries={len(records)} terms={len(terms)} needs_review={review} unparsed={len(unparsed)}")


if __name__ == "__main__":
    main(sys.argv)
