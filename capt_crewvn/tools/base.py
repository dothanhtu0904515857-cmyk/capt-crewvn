"""Tool contract. Concrete tools arrive in Phase 3."""

from enum import StrEnum
from typing import Generic, Protocol, TypeVar

from pydantic import BaseModel

from capt_crewvn.core.schemas.common import Strict
from capt_crewvn.knowledge.scope import RequestScope

In = TypeVar("In", bound=BaseModel, contravariant=True)
Out = TypeVar("Out", bound=BaseModel, covariant=True)


class ToolErrorCode(StrEnum):
    NOT_FOUND = "NOT_FOUND"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    FORBIDDEN = "FORBIDDEN"
    VALIDATION = "VALIDATION"
    MISSING_SOURCE = "MISSING_SOURCE"
    UPSTREAM_UNAVAILABLE = "UPSTREAM_UNAVAILABLE"


class ToolError(Exception):
    def __init__(self, code: ToolErrorCode, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


class ToolMeta(Strict):
    name: str
    description: str
    writes: bool
    required_permission: str


class Tool(Protocol, Generic[In, Out]):
    meta: ToolMeta
    input_model: type[In]
    output_model: type[Out]

    def run(self, payload: In, scope: RequestScope) -> Out: ...
