"""Building blocks shared by entities."""

from datetime import date, datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, model_validator

T = TypeVar("T")


class Strict(BaseModel):
    """Base model: unknown fields are rejected so payloads stay typed (CLAUDE.md §22)."""

    model_config = ConfigDict(extra="forbid")


class SourcedValue(Strict, Generic[T]):
    """A vessel or company particular together with where it came from.

    A value without a source is not allowed: unknown particulars stay ``None``
    rather than being filled with a plausible default (CLAUDE.md §3 items 9-10).
    """

    value: T | None = None
    source_document_id: str | None = None
    entered_by_user_id: str | None = None
    as_of: date | datetime | None = None

    @model_validator(mode="after")
    def _value_needs_source(self) -> "SourcedValue[T]":
        if self.value is not None and not (self.source_document_id or self.entered_by_user_id):
            raise ValueError("a particular with a value must record its source document or the user who entered it")
        return self

    @property
    def known(self) -> bool:
        return self.value is not None
