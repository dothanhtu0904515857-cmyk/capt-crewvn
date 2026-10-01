"""Takeover / inspection items (CLAUDE.md §16, Project Instructions §11)."""

from pydantic import Field, model_validator

from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.core.schemas.enums import EvidenceStatus, InspectionDepth


class AccessRestriction(Strict):
    """Restricted access is preserved as evidence, not replaced by a conclusion."""

    requested_inspection: str
    restriction: str
    imposed_by: str | None = None
    stated_reason: str | None = None
    follow_up: str


class InspectionItem(Strict):
    item_id: str
    inspection_id: str
    area: str
    check_description: str
    equipment_id: str | None = None
    inspection_depth: InspectionDepth = InspectionDepth.NOT_SEEN
    evidence_status: EvidenceStatus = EvidenceStatus.NOT_VERIFIED
    restriction: AccessRestriction | None = None
    findings_text: str | None = None  # human-entered only
    ai_suggestion_text: str | None = None  # AI text kept separate (Project Instructions §17)
    evidence_ids: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _status_matches_depth(self) -> "InspectionItem":
        depth = self.inspection_depth
        if depth == InspectionDepth.VERIFIED and not self.evidence_ids:
            raise ValueError("VERIFIED requires at least one evidence record")
        if depth == InspectionDepth.NOT_SEEN and self.evidence_status in (
            EvidenceStatus.SATISFACTORY_AS_OBSERVED,
            EvidenceStatus.DEFECT_OBSERVED,
        ):
            raise ValueError("an item that was not seen cannot carry an observed status")
        if self.evidence_status == EvidenceStatus.NOT_ACCESSIBLE and self.restriction is None:
            raise ValueError("NOT_ACCESSIBLE items must record the access restriction")
        return self

    @property
    def can_be_called_operational(self) -> bool:
        """Untested machinery is never represented as verified operational (CLAUDE.md §16)."""
        return self.inspection_depth in (InspectionDepth.TESTED, InspectionDepth.VERIFIED)
