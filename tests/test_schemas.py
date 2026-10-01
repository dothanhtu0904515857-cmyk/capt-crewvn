import pytest
from pydantic import ValidationError

from capt_crewvn.core.schemas.common import SourcedValue
from capt_crewvn.core.schemas.document import DocumentMetadata, DocumentStatus, Partition
from capt_crewvn.core.schemas.enums import Authority, EvidenceStatus, InspectionDepth, Provenance
from capt_crewvn.core.schemas.inspection import AccessRestriction, InspectionItem
from capt_crewvn.core.schemas.report import Report, ReportLine, ReportStatus
from capt_crewvn.core.schemas.vessel import Vessel


def test_particular_with_value_requires_source():
    with pytest.raises(ValidationError):
        SourcedValue[float](value=123.0)
    assert SourcedValue[float](value=123.0, source_document_id="doc-1").known


def test_new_vessel_has_every_particular_unknown():
    vessel = Vessel(vessel_id="v1", company_id="c1")
    unknown = vessel.unknown_fields()
    assert "dwt" in unknown and "imo_number" in unknown and "summer_draft" in unknown


def test_vessel_rejects_unknown_fields():
    with pytest.raises(ValidationError):
        Vessel(vessel_id="v1", company_id="c1", favourite_colour="blue")


def _item(**kw):
    base = dict(item_id="i1", inspection_id="ins1", area="ER", check_description="Emergency generator")
    base.update(kw)
    return InspectionItem(**base)


def test_verified_requires_evidence():
    with pytest.raises(ValidationError):
        _item(inspection_depth=InspectionDepth.VERIFIED)
    assert _item(inspection_depth=InspectionDepth.VERIFIED, evidence_ids=["e1"]).can_be_called_operational


def test_seen_but_untested_is_not_operational():
    item = _item(inspection_depth=InspectionDepth.SEEN, evidence_status=EvidenceStatus.NOT_TESTED)
    assert not item.can_be_called_operational


def test_not_seen_cannot_be_observed_satisfactory():
    with pytest.raises(ValidationError):
        _item(evidence_status=EvidenceStatus.SATISFACTORY_AS_OBSERVED)


def test_not_accessible_requires_restriction_record():
    with pytest.raises(ValidationError):
        _item(evidence_status=EvidenceStatus.NOT_ACCESSIBLE)
    restriction = AccessRestriction(
        requested_inspection="Enter No.2 DB tank",
        restriction="Seller declined tank entry",
        follow_up="Inspect at next dry-dock or request class records",
    )
    assert _item(evidence_status=EvidenceStatus.NOT_ACCESSIBLE, restriction=restriction).restriction


def test_measured_line_must_cite_evidence():
    with pytest.raises(ValidationError):
        ReportLine(text="Reading taken", provenance=Provenance.MEASURED)
    ReportLine(text="Assumed", provenance=Provenance.ASSUMPTION)


def test_approved_report_needs_human_approval():
    with pytest.raises(ValidationError):
        Report(report_id="r1", report_type="TAKEOVER", status=ReportStatus.APPROVED, bundle_version="0.1.0")


def test_document_scope_rules():
    common = dict(document_id="d", title="t", document_type="MANUAL", language="en", source="upload")
    with pytest.raises(ValidationError):
        DocumentMetadata(authority=Authority.MAKER, partition=Partition.MAKER, **common)
    with pytest.raises(ValidationError):
        DocumentMetadata(authority=Authority.VESSEL_APPROVED, partition=Partition.VESSEL, company_id="c1", **common)
    with pytest.raises(ValidationError):
        DocumentMetadata(
            authority=Authority.CAPT_CREWVN,
            partition=Partition.GLOBAL_CAPT_CREWVN,
            status=DocumentStatus.APPROVED,
            **common,
        )
