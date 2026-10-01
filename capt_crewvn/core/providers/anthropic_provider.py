"""Anthropic Claude adapter.

The only module that imports the ``anthropic`` SDK (install with ``pip install -e ".[anthropic]"``).
Everything outside ``core/providers`` sees ``Message`` / ``ModelResponse`` only, so the
model or vendor can change without touching prompts, router or tools (ADR 0001).

Configuration comes from the environment, never from source:
  CAPT_CREWVN_MODEL_ID          model id (default ``claude-opus-5-5``)
  CAPT_CREWVN_MODEL_EFFORT      low | medium | high | xhigh | max (default ``high``)
  CAPT_CREWVN_PROVIDER_API_KEY  API key; falls back to the SDK's own ANTHROPIC_API_KEY

Server-side refusal fallbacks are on: if the primary model declines, the API reruns
the same request on the default fallback model inside the same call. A response that
is still a refusal is returned with ``refused=True`` and no answer text.
"""

import os
from typing import Any

from capt_crewvn.core.providers.base import Message, ModelResponse, ToolCall, ToolSpec

DEFAULT_MODEL_ID = "claude-opus-5-5"
DEFAULT_EFFORT = "high"
DEFAULT_MAX_OUTPUT_TOKENS = 16000
FALLBACK_BETA = "server-side-fallback-2026-07-01"


class ProviderError(RuntimeError):
    """Raised for provider failures; ``retryable`` tells the caller whether a retry may help."""

    def __init__(self, message: str, retryable: bool) -> None:
        super().__init__(message)
        self.retryable = retryable


class AnthropicProvider:
    name = "anthropic"

    def __init__(
        self,
        model_id: str | None = None,
        effort: str | None = None,
        client: Any | None = None,
    ) -> None:
        self.model_id = model_id or os.environ.get("CAPT_CREWVN_MODEL_ID") or DEFAULT_MODEL_ID
        self.effort = effort or os.environ.get("CAPT_CREWVN_MODEL_EFFORT") or DEFAULT_EFFORT
        if client is None:
            import anthropic

            api_key = os.environ.get("CAPT_CREWVN_PROVIDER_API_KEY") or None
            client = anthropic.Anthropic(api_key=api_key)
        self._client = client

    def generate(
        self,
        messages: list[Message],
        tools: list[ToolSpec] | None = None,
        max_output_tokens: int | None = None,
    ) -> ModelResponse:
        system, turns = to_anthropic_messages(messages)
        request: dict[str, Any] = {
            "model": self.model_id,
            "max_tokens": max_output_tokens or DEFAULT_MAX_OUTPUT_TOKENS,
            "messages": turns,
            "output_config": {"effort": self.effort},
            "betas": [FALLBACK_BETA],
            "fallbacks": "default",
        }
        if system:
            request["system"] = system
        if tools:
            request["tools"] = [
                {"name": t.name, "description": t.description, "input_schema": t.input_schema}
                for t in tools
            ]
        response = self._call(request)
        return from_anthropic_response(response, provider=self.name)

    def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError("Anthropic has no embedding endpoint; configure a separate embedding provider")

    def _call(self, request: dict[str, Any]) -> Any:
        import anthropic

        try:
            return self._client.beta.messages.create(**request)
        except anthropic.RateLimitError as exc:
            raise ProviderError("rate limited by provider", retryable=True) from exc
        except anthropic.APIStatusError as exc:
            retryable = exc.status_code >= 500
            raise ProviderError(f"provider returned HTTP {exc.status_code}", retryable=retryable) from exc
        except anthropic.APIConnectionError as exc:
            raise ProviderError("could not reach provider", retryable=True) from exc


def to_anthropic_messages(messages: list[Message]) -> tuple[str, list[dict[str, Any]]]:
    """Split out system text and convert turns; adjacent same-role turns are merged."""
    system_parts: list[str] = []
    turns: list[dict[str, Any]] = []
    for m in messages:
        if m.role == "system":
            system_parts.append(m.content)
            continue
        if m.role == "tool":
            if not m.tool_call_id:
                raise ValueError("a tool message must name the tool_call_id it answers")
            role, blocks = "user", [
                {"type": "tool_result", "tool_use_id": m.tool_call_id, "content": m.content}
            ]
        elif m.role == "assistant":
            role = "assistant"
            blocks = [{"type": "text", "text": m.content}] if m.content else []
            blocks += [
                {"type": "tool_use", "id": c.call_id, "name": c.name, "input": c.arguments}
                for c in m.tool_calls
            ]
        else:
            role, blocks = "user", [{"type": "text", "text": m.content}]
        if turns and turns[-1]["role"] == role:
            turns[-1]["content"].extend(blocks)
        else:
            turns.append({"role": role, "content": blocks})
    return "\n\n".join(system_parts), turns


def from_anthropic_response(response: Any, provider: str) -> ModelResponse:
    """Normalise an SDK response. A refusal carries no answer text."""
    model_id = getattr(response, "model", "") or ""
    if response.stop_reason == "refusal":
        details = getattr(response, "stop_details", None)
        return ModelResponse(
            provider=provider,
            model_id=model_id,
            stop_reason="refusal",
            refused=True,
            refusal_category=getattr(details, "category", None) if details else None,
        )
    texts: list[str] = []
    calls: list[ToolCall] = []
    for block in response.content:
        if block.type == "text":
            texts.append(block.text)
        elif block.type == "tool_use":
            calls.append(ToolCall(call_id=block.id, name=block.name, arguments=dict(block.input)))
        # thinking, fallback markers and other block types carry no answer text
    return ModelResponse(
        text="".join(texts),
        tool_calls=calls,
        provider=provider,
        model_id=model_id,
        stop_reason=response.stop_reason,
    )
