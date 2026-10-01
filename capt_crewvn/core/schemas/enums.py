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
    """Takeover inspection depth (CLAUDE.md §16)."""

    NOT_SEEN = "NOT_SEEN"
    SEEN = "SEEN"
    INSPECTED = "INSPECTED"
    TESTED = "TESTED"
    VERIFIED = "VERIFIED"


class EvidenceStatus(StrEnum):
    """Takeover evidence statuses (CLAUDE.md §16)."""

    SATISFACTORY_AS_OBSERVED = "SATISFACTORY_AS_OBSERVED"
    DEFECT_OBSERVED = "DEFECT_OBSERVED"
    NOT_TESTED = "NOT_TESTED"
    NOT_ACCESSIBLE = "NOT_ACCESSIBLE"
    NOT_VERIFIED = "NOT_VERIFIED"
    FURTHER_VERIFICATION_REQUIRED = "FURTHER_VERIFICATION_REQUIRED"
