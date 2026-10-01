"""Tenant scope: prevents cross-company and cross-vessel leakage."""

from pydantic import Field

from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.core.schemas.document import DocumentMetadata, DocumentStatus, Partition


class RequestScope(Strict):
    """Resolved by authorisation for each request. Retrieval refuses to run without one."""

    user_id: str
    company_ids: list[str] = Field(default_factory=list)
    vessel_ids: list[str] = Field(default_factory=list)


def is_visible(doc: DocumentMetadata, scope: RequestScope, include_unapproved: bool = False) -> bool:
    """True when the document may be retrieved for this request."""
    if not include_unapproved and doc.status != DocumentStatus.APPROVED:
        return False
    if doc.partition == Partition.USER:
        return doc.user_id == scope.user_id
    if doc.company_id is not None and doc.company_id not in scope.company_ids:
        return False
    if doc.vessel_id is not None and doc.vessel_id not in scope.vessel_ids:
        return False
    return True


def filter_visible(
    docs: list[DocumentMetadata], scope: RequestScope, include_unapproved: bool = False
) -> list[DocumentMetadata]:
    return [d for d in docs if is_visible(d, scope, include_unapproved)]
