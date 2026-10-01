"""Provider-neutral request and response types."""

from typing import Any, Literal, Protocol, runtime_checkable

from pydantic import Field

from capt_crewvn.core.schemas.common import Strict


class ToolCall(Strict):
    call_id: str
    name: str
    arguments: dict[str, Any]


class Message(Strict):
    role: Literal["system", "user", "assistant", "tool"]
    content: str
    tool_call_id: str | None = None  # on role="tool": which call this result answers
    tool_calls: list[ToolCall] = Field(default_factory=list)  # on role="assistant"


class ToolSpec(Strict):
    name: str
    description: str
    input_schema: dict[str, Any]


class ModelResponse(Strict):
    text: str = ""
    tool_calls: list[ToolCall] = Field(default_factory=list)
    provider: str
    model_id: str
    stop_reason: str | None = None
    refused: bool = False  # the model (and any fallback) declined; text is not an answer
    refusal_category: str | None = None


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
