"""Provider-neutral request and response types."""

from typing import Any, Literal, Protocol, runtime_checkable

from pydantic import Field

from capt_crewvn.core.schemas.common import Strict


class Message(Strict):
    role: Literal["system", "user", "assistant", "tool"]
    content: str
    tool_call_id: str | None = None


class ToolSpec(Strict):
    name: str
    description: str
    input_schema: dict[str, Any]


class ToolCall(Strict):
    call_id: str
    name: str
    arguments: dict[str, Any]


class ModelResponse(Strict):
    text: str = ""
    tool_calls: list[ToolCall] = Field(default_factory=list)
    provider: str
    model_id: str
    stop_reason: str | None = None


@runtime_checkable
class ModelProvider(Protocol):
    """Every adapter implements this. Prompts arrive as plain provider-neutral messages."""

    name: str
    model_id: str

    def generate(
        self,
        messages: list[Message],
        tools: list[ToolSpec] | None = None,
        max_output_tokens: int | None = None,
    ) -> ModelResponse: ...

    def embed(self, texts: list[str]) -> list[list[float]]: ...
