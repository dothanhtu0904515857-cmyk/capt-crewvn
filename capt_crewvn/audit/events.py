"""Audit event shape. Storage is supplied by the backend; this module defines what is recorded."""

from datetime import UTC, datetime
from enum import StrEnum

from pydantic import Field

from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.core.schemas.enums import RouterRole


class AuditEventType(StrEnum):
    REQUEST = "REQUEST"
    TOOL_CALL = "TOOL_CALL"
    SAFETY_DECLINE = "SAFETY_DECLINE"
    POST_CHECK_FAILED = "POST_CHECK_FAILED"
    REPORT_DRAFTED = "REPORT_DRAFTED"
    HUMAN_EDIT = "HUMAN_EDIT"
    HUMAN_APPROVAL = "HUMAN_APPROVAL"


class AuditEvent(Strict):
    event_id: str
    event_type: AuditEventType
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    user_id: str
    router_role: RouterRole | None = None
    company_id: str | None = None
    vessel_id: str | None = None
    bundle_version: str
    modules: list[str] = Field(default_factory=list)
    retrieved_document_revisions: list[str] = Field(default_factory=list)
    tool_name: str | None = None
    model_provider: str | None = None
    model_id: str | None = None
    input_hash: str | None = None
    output_hash: str | None = None
    safety_flags: list[str] = Field(default_factory=list)
    parent_event_id: str | None = None
    actor_is_human: bool = False
