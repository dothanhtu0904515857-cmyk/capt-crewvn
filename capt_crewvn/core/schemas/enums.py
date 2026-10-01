"""Controlled vocabularies.

Each enum names the CLAUDE.md section or specification part it comes from so a
change to the source can be traced to the code.
"""

from enum import StrEnum


class Authority(StrEnum):
    """Source authority of a document (CLAUDE.md §8)."""

    IMO = "IMO"
    FLAG = "FLAG"
    CLASS = "CLASS"
    PORT = "PORT"
    TERMINAL = "TERMINAL"
    COMPANY_SMS = "COMPANY_SMS"
    MAKER = "MAKER"
    VESSEL_APPROVED = "VESSEL_APPROVED"
    CAPT_CREWVN = "CAPT_CREWVN"
    TRAINING_REFERENCE = "TRAINING_REFERENCE"


class Provenance(StrEnum):
    """Where a statement in an output or report came from (CLAUDE.md §18, Spec Part C §7)."""

    OBSERVATION = "OBSERVATION"
    MEASURED = "MEASURED"
    DOCUMENT_EVIDENCE = "DOCUMENT_EVIDENCE"
    OPERATOR_STATEMENT = "OPERATOR_STATEMENT"
    ASSUMPTION = "ASSUMPTION"
    RECOMMENDATION = "RECOMMENDATION"
    UNRESOLVED = "UNRESOLVED"
    AI_DRAFT = "AI_DRAFT"


class VesselType(StrEnum):
    """Vessel types, in the priority order of the project goal."""

    BULK_CARRIER = "BULK_CARRIER"
    GENERAL_CARGO = "GENERAL_CARGO"
    MULTIPURPOSE = "MULTIPURPOSE"
    CONTAINER = "CONTAINER"
    OIL_TANKER = "OIL_TANKER"
    CHEMICAL_TANKER = "CHEMICAL_TANKER"
    RO_RO = "RO_RO"
    GAS_CARRIER = "GAS_CARRIER"
    OTHER = "OTHER"


class Department(StrEnum):
    DECK = "DECK"
    ENGINE = "ENGINE"
    CATERING = "CATERING"
    SHORE = "SHORE"
    TRAINING = "TRAINING"


class RouterRole(StrEnum):
    """The 21 router roles from the First Prompt, Task 4 (Spec Part E)."""

    MASTER = "MASTER"
    CHIEF_OFFICER = "CHIEF_OFFICER"
    SECOND_OFFICER = "SECOND_OFFICER"
    THIRD_OFFICER = "THIRD_OFFICER"
    DECK_CREW = "DECK_CREW"
    CHIEF_ENGINEER = "CHIEF_ENGINEER"
    SECOND_ENGINEER = "SECOND_ENGINEER"
    THIRD_ENGINEER = "THIRD_ENGINEER"
    FOURTH_ENGINEER = "FOURTH_ENGINEER"
    ETO = "ETO"
    ELECTRICIAN = "ELECTRICIAN"
    FITTER = "FITTER"
    ENGINE_CREW = "ENGINE_CREW"
    MARINE_SUPERINTENDENT = "MARINE_SUPERINTENDENT"
    TECHNICAL_SUPERINTENDENT = "TECHNICAL_SUPERINTENDENT"
    DPA = "DPA"
    CSO = "CSO"
    HSQE = "HSQE"
    SHORE_STAFF = "SHORE_STAFF"
    CADET = "CADET"
    MARITIME_STUDENT = "MARITIME_STUDENT"


class TaskUrgency(StrEnum):
    """Safety triage result (CLAUDE.md §9, Spec Part C §6)."""

    IMMEDIATE_DANGER = "IMMEDIATE_DANGER"
    URGENT = "URGENT"
    ROUTINE = "ROUTINE"
    STUDY = "STUDY"


class FindingConfidence(StrEnum):
    """Diagnosis ladder (CLAUDE.md §13). Observation is not diagnosis."""

    OBSERVED = "OBSERVED"
    SUSPECTED = "SUSPECTED"
    TESTED = "TESTED"
    VERIFIED = "VERIFIED"


class InspectionDepth(StrEnum):
    """Takeover inspection depth (CLAUDE.md §16; Knowledge Pack 04 §1; ADR 0004).

    Pack 04 splits CLAUDE.md's four levels into five:
    L1 SEEN, L2 INSPECTED, L3 DOC (document verified), L4 TESTED (function tested),
    L5 PERF (performance verified). CLAUDE.md's VERIFIED is accepted as input and
    means PERF. "Never report Level 1 evidence as Level 5" (pack 04 §1).
    """

    NOT_SEEN = "NOT_SEEN"
    SEEN = "SEEN"
    INSPECTED = "INSPECTED"
    DOC = "DOC"
    TESTED = "TESTED"
    PERF = "PERF"
    VERIFIED = "PERF"  # alias kept for CLAUDE.md §16 wording

    @classmethod
    def _missing_(cls, value: object) -> "InspectionDepth | None":
        if isinstance(value, str) and value.upper() == "VERIFIED":
            return cls.PERF
        return None

    @property
    def level(self) -> int:
        """0 for NOT_SEEN, then pack 04 levels 1-5."""
        return _DEPTH_LEVEL[self]


_DEPTH_LEVEL = {
    InspectionDepth.NOT_SEEN: 0,
    InspectionDepth.SEEN: 1,
    InspectionDepth.INSPECTED: 2,
    InspectionDepth.DOC: 3,
    InspectionDepth.TESTED: 4,
    InspectionDepth.PERF: 5,
}


class EvidenceStatus(StrEnum):
    """Takeover evidence statuses (CLAUDE.md §16)."""

    SATISFACTORY_AS_OBSERVED = "SATISFACTORY_AS_OBSERVED"
    DEFECT_OBSERVED = "DEFECT_OBSERVED"
    NOT_TESTED = "NOT_TESTED"
    NOT_ACCESSIBLE = "NOT_ACCESSIBLE"
    NOT_VERIFIED = "NOT_VERIFIED"
    FURTHER_VERIFICATION_REQUIRED = "FURTHER_VERIFICATION_REQUIRED"


# Pack 04 §2 short codes, as written on takeover checklists.
PACK_STATUS_CODES: dict[str, EvidenceStatus] = {
    "S": EvidenceStatus.SATISFACTORY_AS_OBSERVED,
    "D": EvidenceStatus.DEFECT_OBSERVED,
    "NT": EvidenceStatus.NOT_TESTED,
    "NA": EvidenceStatus.NOT_ACCESSIBLE,
    "NV": EvidenceStatus.NOT_VERIFIED,
    "FVR": EvidenceStatus.FURTHER_VERIFICATION_REQUIRED,
}


class DefectClass(StrEnum):
    """Knowledge Pack 04 §9. Assign from defined company/project criteria, not impression."""

    A = "A"  # immediate safety / statutory significance
    B = "B"  # important operational deficiency
    C = "C"  # maintenance deficiency
    D = "D"  # cosmetic / minor
