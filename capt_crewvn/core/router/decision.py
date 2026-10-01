"""The router's output contract (Spec Part E.5)."""

from pydantic import Field

from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.core.schemas.enums import Department, RouterRole, TaskUrgency


class RouteDecision(Strict):
    router_role: RouterRole
    department: Department
    vessel_id: str | None = None
    company_id: str | None = None
    operation: str | None = None
    task_type: str | None = None
    urgency: TaskUrgency
    immediate_danger: bool
    modules: list[str] = Field(default_factory=list)
    precedence_profile: str = "VESSEL_OPERATIONAL"
    missing_context: list[str] = Field(default_factory=list)
