from capt_crewvn.core.schemas.document import DocumentMetadata, DocumentStatus, Partition
from capt_crewvn.core.schemas.enums import Authority
from capt_crewvn.knowledge.scope import RequestScope, filter_visible


def doc(doc_id, partition, authority, company_id=None, vessel_id=None, user_id=None, status=DocumentStatus.APPROVED):
    return DocumentMetadata(
        document_id=doc_id,
        title=doc_id,
        document_type="X",
        authority=authority,
        partition=partition,
        company_id=company_id,
        vessel_id=vessel_id,
        user_id=user_id,
        language="en",
        source="test",
        status=status,
        verified_by="reviewer" if status == DocumentStatus.APPROVED else None,
    )


DOCS = [
    doc("global", Partition.GLOBAL_CAPT_CREWVN, Authority.CAPT_CREWVN),
    doc("co1-sms", Partition.COMPANY, Authority.COMPANY_SMS, company_id="co1"),
    doc("co2-sms", Partition.COMPANY, Authority.COMPANY_SMS, company_id="co2"),
    doc("vA-plan", Partition.VESSEL, Authority.VESSEL_APPROVED, company_id="co1", vessel_id="vA"),
    doc("vB-plan", Partition.VESSEL, Authority.VESSEL_APPROVED, company_id="co1", vessel_id="vB"),
    doc("u1-note", Partition.USER, Authority.CAPT_CREWVN, user_id="u1"),
    doc("draft", Partition.COMPANY, Authority.COMPANY_SMS, company_id="co1", status=DocumentStatus.DRAFT),
]


def ids(scope, **kw):
    return {d.document_id for d in filter_visible(DOCS, scope, **kw)}


def test_no_cross_vessel_leakage():
    visible = ids(RequestScope(user_id="u1", company_ids=["co1"], vessel_ids=["vB"]))
    assert "vB-plan" in visible and "vA-plan" not in visible


def test_no_cross_company_leakage():
    visible = ids(RequestScope(user_id="u2", company_ids=["co1"], vessel_ids=[]))
    assert "co1-sms" in visible and "co2-sms" not in visible and "u1-note" not in visible


def test_drafts_excluded_by_default():
    scope = RequestScope(user_id="u1", company_ids=["co1"])
    assert "draft" not in ids(scope)
    assert "draft" in ids(scope, include_unapproved=True)


def test_empty_scope_sees_only_platform_knowledge():
    assert ids(RequestScope(user_id="nobody")) == {"global"}
