import hashlib
from collections import Counter
from pathlib import Path

import pytest

from capt_crewvn.core.schemas.document import DocumentStatus, Partition
from capt_crewvn.core.schemas.enums import (
    PACK_STATUS_CODES,
    Authority,
    DefectClass,
    Department,
    EvidenceStatus,
    InspectionDepth,
)
from capt_crewvn.core.schemas.inspection import InspectionItem
from capt_crewvn.knowledge.mvp_pack import PACK_DIR, checklist_systems, pack_documents, takeover_checklist


def test_manifest_covers_every_pack_file_and_nothing_else():
    listed = {path.name for path, _ in pack_documents().values()}
    on_disk = {p.name for p in PACK_DIR.iterdir() if p.suffix in (".md", ".csv")}
    assert listed == on_disk
    assert all(path.exists() for path, _ in pack_documents().values())


def test_pack_is_global_capt_crewvn_knowledge_never_company_sms():
    for _, meta in pack_documents().values():
        assert meta.partition == Partition.GLOBAL_CAPT_CREWVN
        assert meta.authority == Authority.CAPT_CREWVN
        assert meta.company_id is None and meta.vessel_id is None
    docs = pack_documents()
    assert "NOT a company" in docs["CCV-MVP-07"][1].title
    assert "NOT a company" in docs["CCV-MVP-05"][1].title


def test_claude_drafted_checklist_stays_draft():
    docs = pack_documents()
    for doc_id in ("CCV-MVP-04A", "CCV-MVP-04A-CSV"):
        assert docs[doc_id][1].status == DocumentStatus.DRAFT
        assert docs[doc_id][1].verified_by is None


def test_checklist_has_49_systems_and_287_lines():
    items = takeover_checklist()
    assert len(checklist_systems()) == 49
    assert len(items) == 287
    assert Counter(i.checklist_group for i in items) == {"DECK": 121, "ENGINE": 119, "ETO / ELECTRICAL": 47}
    assert all(i.department in (Department.DECK, Department.ENGINE) for i in items)
    assert all(i.system_en and i.system_vi and i.system_zh for i in items)
    assert len({i.item_no for i in items}) == len(items)


def test_checklist_targets_use_pack_levels():
    depths = {i.target_depth for i in takeover_checklist()}
    assert depths <= {InspectionDepth.SEEN, InspectionDepth.INSPECTED, InspectionDepth.DOC,
                      InspectionDepth.TESTED, InspectionDepth.PERF}


def test_template_csv_carries_no_results(tmp_path, monkeypatch):
    from capt_crewvn.knowledge import mvp_pack

    bad = tmp_path / "bad.csv"
    lines = mvp_pack.CHECKLIST_CSV.read_text(encoding="utf-8-sig").splitlines()
    bad.write_text("\n".join([lines[0], lines[1].rstrip(",") + ",TESTED,S,,"]), encoding="utf-8")
    monkeypatch.setattr(mvp_pack, "CHECKLIST_CSV", bad)
    mvp_pack.takeover_checklist.cache_clear()
    try:
        with pytest.raises(ValueError, match="carries results"):
            mvp_pack.takeover_checklist()
    finally:
        mvp_pack.takeover_checklist.cache_clear()


def test_pack_copy_matches_project_files_when_available():
    project = Path("/mnt/project-files/CAPT_CREWVN_MVP_KNOWLEDGE")
    if not project.exists():
        pytest.skip("project files not mounted")
    for path, _ in pack_documents().values():
        source = project / path.name
        assert hashlib.sha256(source.read_bytes()).digest() == hashlib.sha256(path.read_bytes()).digest(), path.name


def test_five_level_depth_and_verified_alias():
    assert InspectionDepth("VERIFIED") is InspectionDepth.PERF
    assert InspectionDepth.VERIFIED is InspectionDepth.PERF
    assert [d.level for d in (InspectionDepth.SEEN, InspectionDepth.INSPECTED, InspectionDepth.DOC,
                              InspectionDepth.TESTED, InspectionDepth.PERF)] == [1, 2, 3, 4, 5]


def _item(**kw):
    return InspectionItem(item_id="i", inspection_id="x", area="ER", check_description="c", **kw)


def test_document_verified_is_not_operational_and_needs_evidence():
    with pytest.raises(ValueError):
        _item(inspection_depth=InspectionDepth.DOC)
    assert not _item(inspection_depth=InspectionDepth.DOC, evidence_ids=["log-1"]).can_be_called_operational
    assert _item(inspection_depth=InspectionDepth.TESTED).can_be_called_operational


def test_pack_status_codes_and_defect_classes():
    assert PACK_STATUS_CODES["NA"] == EvidenceStatus.NOT_ACCESSIBLE
    assert set(PACK_STATUS_CODES.values()) == set(EvidenceStatus)
    assert [c.value for c in DefectClass] == ["A", "B", "C", "D"]
