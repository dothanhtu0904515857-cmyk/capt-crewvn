"""Vessel entity (CLAUDE.md §5, Spec Part H).

Every particular is a ``SourcedValue``; nothing is defaulted. No vessel data is
hard-coded anywhere in the package.
"""

from pydantic import Field

from capt_crewvn.core.schemas.common import SourcedValue, Strict
from capt_crewvn.core.schemas.enums import VesselType


class Vessel(Strict):
    vessel_id: str
    company_id: str
    current_name: SourcedValue[str] = SourcedValue()
    former_names: list[str] = Field(default_factory=list)
    imo_number: SourcedValue[str] = SourcedValue()
    call_sign: SourcedValue[str] = SourcedValue()
    flag: SourcedValue[str] = SourcedValue()
    class_society: SourcedValue[str] = SourcedValue()
    vessel_type: SourcedValue[VesselType] = SourcedValue()
    built: SourcedValue[str] = SourcedValue()
    shipyard: SourcedValue[str] = SourcedValue()
    dwt: SourcedValue[float] = SourcedValue()
    gt: SourcedValue[float] = SourcedValue()
    nt: SourcedValue[float] = SourcedValue()
    loa: SourcedValue[float] = SourcedValue()
    breadth: SourcedValue[float] = SourcedValue()
    depth: SourcedValue[float] = SourcedValue()
    summer_draft: SourcedValue[float] = SourcedValue()
    ice_class: SourcedValue[str] = SourcedValue()
    main_engine_equipment_id: str | None = None
    auxiliary_engine_equipment_ids: list[str] = Field(default_factory=list)
    bwms_equipment_id: str | None = None
    owners: SourcedValue[str] = SourcedValue()
    managers: SourcedValue[str] = SourcedValue()
    sms_profile: SourcedValue[str] = SourcedValue()

    def unknown_fields(self) -> list[str]:
        """Names of particulars with no recorded value: these must be reported as UNKNOWN, never guessed."""
        return [
            name
            for name, field_value in self
            if isinstance(field_value, SourcedValue) and not field_value.known
        ]
