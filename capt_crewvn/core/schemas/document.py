"""Knowledge document metadata (CLAUDE.md §8, Spec Part G.3)."""

from datetime import date
from enum import StrEnum

from pydantic import model_validator

from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.core.schemas.enums import Authority, Department, RouterRole, VesselType


class Partition(StrEnum):
    GLOBAL_CAPT_CREWVN = "GLOBAL_CAPT_CREWVN"
    REGULATORY = "REGULATORY"
    FLAG = "FLAG"
    CLASS = "CLASS"
    PORT = "PORT"
    MAKER = "MAKER"
    COMPANY = "COMPANY"
    VESSEL = "VESSEL"
    USER = "USER"
    TRAINING = "TRAINING"


class DocumentStatus(StrEnum):
    DRAFT = "DRAFT"
    APPROVED = "APPROVED"
    SUPERSEDED = "SUPERSEDED"
    WITHDRAWN = "WITHDRAWN"


TENANT_PARTITIONS = {Partition.MAKER, Partition.COMPANY, Partition.VESSEL}


class DocumentMetadata(Strict):
    document_id: str
    title: str
    document_type: str
    authority: Authority
    partition: Partition
    company_id: str | None = None
    vessel_id: str | None = None
    user_id: str | None = None
    vessel_type: VesselType | None = None
    department: Department | None = None
    role: RouterRole | None = None
    module: str | None = None
    language: str
    revision: str | None = None
    effective_date: date | None = None
    source: str
    status: DocumentStatus = DocumentStatus.DRAFT
    supersedes: str | None = None
    verified_by: str | None = None
    licence: str | None = None

    @model_validator(mode="after")
    def _scope_is_consistent(self) -> "DocumentMetadata":
        if self.partition in TENANT_PARTITIONS and not self.company_id:
            raise ValueError(f"{self.partition} documents must belong to a company")
        if self.partition == Partition.VESSEL and not self.vessel_id:
            raise ValueError("VESSEL documents must name the vessel")
        if self.partition == Partition.USER and not self.user_id:
            raise ValueError("USER documents must name the user")
        if self.status == DocumentStatus.APPROVED and not self.verified_by:
            raise ValueError("a document is APPROVED only after a human verified its metadata")
        return self
