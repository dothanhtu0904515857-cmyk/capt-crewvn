"""Company entity (CLAUDE.md §6). One company's SMS never applies to another."""

from pydantic import Field

from capt_crewvn.core.schemas.common import Strict


class Company(Strict):
    company_id: str
    organization_id: str
    name: str
    sms_version: str | None = None
    pms_system: str | None = None
    vessel_ids: list[str] = Field(default_factory=list)
    reporting_rules_document_id: str | None = None
    defect_policy_document_id: str | None = None
    purchasing_policy_document_id: str | None = None
