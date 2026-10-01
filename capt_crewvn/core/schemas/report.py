"""Report line items with provenance (CLAUDE.md §18, §21)."""

from enum import StrEnum

from pydantic import Field, model_validator

from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.core.schemas.enums import Provenance


class LanguageLayout(StrEnum):
    VI = "VI"
    EN = "EN"
    ZH = "ZH"
    EN_ZH = "EN_ZH"
    VI_EN_ZH = "VI_EN_ZH"


class ReportStatus(StrEnum):
    DRAFT = "DRAFT"
    UNDER_REVIEW = "UNDER_REVIEW"
    APPROVED = "APPROVED"
    ISSUED = "ISSUED"


class ReportLine(Strict):
    text: str
    provenance: Provenance
    evidence_ids: list[str] = Field(default_factory=list)
    source_refs: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _evidence_backed(self) -> "ReportLine":
        if self.provenance in (Provenance.MEASURED, Provenance.DOCUMENT_EVIDENCE) and not (
            self.evidence_ids or self.source_refs
        ):
            raise ValueError(f"{self.provenance} lines must cite evidence or a source")
        return self


class ReportSection(Strict):
    heading: str
    lines: list[ReportLine] = Field(default_factory=list)


class Report(Strict):
    report_id: str
    report_type: str
    vessel_id: str | None = None
    language_layout: LanguageLayout = LanguageLayout.EN
    sections: list[ReportSection] = Field(default_factory=list)
    status: ReportStatus = ReportStatus.DRAFT
    approval_id: str | None = None
    bundle_version: str

    @model_validator(mode="after")
    def _approval_is_human(self) -> "Report":
        if self.status in (ReportStatus.APPROVED, ReportStatus.ISSUED) and not self.approval_id:
            raise ValueError("APPROVED or ISSUED reports must reference a human Approval record")
        return self
