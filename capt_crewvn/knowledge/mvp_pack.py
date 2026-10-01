"""Loader for the MVP Knowledge Pack: document metadata and the 04A takeover checklists."""

import csv
from functools import cache
from pathlib import Path

import yaml

from capt_crewvn.core.schemas.document import DocumentMetadata
from capt_crewvn.core.schemas.enums import Department, InspectionDepth
from capt_crewvn.core.schemas.inspection import ChecklistTemplateItem

PACK_DIR = Path(__file__).resolve().parent / "global" / "mvp_pack"
MANIFEST = PACK_DIR / "manifest.yaml"
CHECKLIST_CSV = PACK_DIR / "04A_SHIP_TAKEOVER_EQUIPMENT_CHECKLISTS.csv"

OWNER = "Crewvn (owner)"

# 04A groups ETO / electrical systems separately; organisationally they sit in the engine department.
_GROUP_DEPARTMENT = {
    "DECK": Department.DECK,
    "ENGINE": Department.ENGINE,
    "ETO / ELECTRICAL": Department.ENGINE,
}

# Columns that must stay empty in a template: results are recorded on board, never shipped.
RESULT_COLUMNS = ("reached_level", "status", "evidence_ref", "remarks")


@cache
def pack_documents() -> dict[str, tuple[Path, DocumentMetadata]]:
    """document_id -> (file path, metadata) for every file listed in the manifest."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    defaults = data["defaults"]
    out: dict[str, tuple[Path, DocumentMetadata]] = {}
    for entry in data["documents"]:
        entry = dict(entry)
        path = PACK_DIR / entry.pop("file")
        note = entry.pop("note", None)
        source = defaults["source"] + (f". {note}" if note else "")
        meta = DocumentMetadata(
            **{k: v for k, v in defaults.items() if k != "source"},
            **entry,
            source=source,
            verified_by=OWNER if entry.get("status") == "APPROVED" else None,
        )
        out[meta.document_id] = (path, meta)
    return out


@cache
def takeover_checklist() -> tuple[ChecklistTemplateItem, ...]:
    """The 04A checklist lines, typed. Raises if a template line carries a result."""
    items: list[ChecklistTemplateItem] = []
    with CHECKLIST_CSV.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            filled = [c for c in RESULT_COLUMNS if row[c].strip()]
            if filled:
                raise ValueError(f"{row['item_no']}: template carries results in {filled}")
            items.append(
                ChecklistTemplateItem(
                    checklist_group=row["dept"],
                    department=_GROUP_DEPARTMENT[row["dept"]],
                    system_code=row["code"],
                    system_en=row["system_en"],
                    system_vi=row["system_vi"],
                    system_zh=row["system_zh"],
                    typical_rank=row["typical_rank"],
                    item_no=row["item_no"],
                    check_item=row["check_item"],
                    target_depth=InspectionDepth(row["target_level"]),
                )
            )
    return tuple(items)


def checklist_systems() -> dict[str, list[ChecklistTemplateItem]]:
    """system_code -> its checklist lines, in file order."""
    systems: dict[str, list[ChecklistTemplateItem]] = {}
    for item in takeover_checklist():
        systems.setdefault(item.system_code, []).append(item)
    return systems
