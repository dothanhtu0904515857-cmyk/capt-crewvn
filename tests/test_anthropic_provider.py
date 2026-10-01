from types import SimpleNamespace

import httpx
import pytest

anthropic = pytest.importorskip("anthropic")

from capt_crewvn.core.providers import Message, ModelProvider, ToolCall, ToolSpec  # noqa: E402
from capt_crewvn.core.providers.anthropic_provider import (  # noqa: E402
    FALLBACK_BETA,
    AnthropicProvider,
    ProviderError,
    to_anthropic_messages,
)


class FakeMessages:
    def __init__(self, response=None, error=None):
        self.response, self.error, self.requests = response, error, []

    def create(self, **request):
        self.requests.append(request)
        if self.error:
            raise self.error
        return self.response


def _client(response=None, error=None):
    messages = FakeMessages(response, error)
    return SimpleNamespace(beta=SimpleNamespace(messages=messages)), messages


def _response(blocks, stop_reason="end_turn", **extra):
    return SimpleNamespace(content=blocks, stop_reason=stop_reason, model="claude-opus-5-5", **extra)


def test_request_shape_and_text(monkeypatch):
    monkeypatch.delenv("CAPT_CREWVN_MODEL_ID", raising=False)
    client, calls = _client(_response([SimpleNamespace(type="text", text="ok")]))
    provider = AnthropicProvider(client=client)
    assert isinstance(provider, ModelProvider)
    out = provider.generate(
        [Message(role="system", content="rules"), Message(role="user", content="hi")],
        tools=[ToolSpec(name="get_vessel_context", description="d", input_schema={"type": "object"})],
    )
    req = calls.requests[0]
    assert req["model"] == "claude-opus-5-5" and req["system"] == "rules"
    assert req["output_config"] == {"effort": "high"}
    assert req["fallbacks"] == "default" and req["betas"] == [FALLBACK_BETA]
    assert "thinking" not in req and "tool_choice" not in req
    assert out.text == "ok" and not out.refused


def test_model_id_from_environment(monkeypatch):
    monkeypatch.setenv("CAPT_CREWVN_MODEL_ID", "some-other-model")
    client, _ = _client()
    assert AnthropicProvider(client=client).model_id == "some-other-model"


def test_tool_use_is_normalised():
    block = SimpleNamespace(type="tool_use", id="tu_1", name="get_vessel_context", input={"vessel_id": "V"})
    client, _ = _client(_response([block], stop_reason="tool_use"))
    out = AnthropicProvider(client=client).generate([Message(role="user", content="x")])
    assert out.tool_calls == [ToolCall(call_id="tu_1", name="get_vessel_context", arguments={"vessel_id": "V"})]


def test_refusal_returns_no_text():
    details = SimpleNamespace(category="cyber", explanation="n/a")
    resp = _response([SimpleNamespace(type="text", text="partial")], stop_reason="refusal", stop_details=details)
    client, _ = _client(resp)
    out = AnthropicProvider(client=client).generate([Message(role="user", content="x")])
    assert out.refused and out.text == "" and out.refusal_category == "cyber"


def test_tool_round_trip_messages_merge_results():
    _, turns = to_anthropic_messages([
        Message(role="user", content="q"),
        Message(role="assistant", content="", tool_calls=[
            ToolCall(call_id="a", name="t", arguments={}), ToolCall(call_id="b", name="t", arguments={})]),
        Message(role="tool", content="r1", tool_call_id="a"),
        Message(role="tool", content="r2", tool_call_id="b"),
    ])
    assert [t["role"] for t in turns] == ["user", "assistant", "user"]
    assert [b["tool_use_id"] for b in turns[2]["content"]] == ["a", "b"]


def test_errors_are_mapped():
    req = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    rate = anthropic.RateLimitError("slow", response=httpx.Response(429, request=req), body=None)
    client, _ = _client(error=rate)
    with pytest.raises(ProviderError) as info:
        AnthropicProvider(client=client).generate([Message(role="user", content="x")])
    assert info.value.retryable
    bad = anthropic.BadRequestError("bad", response=httpx.Response(400, request=req), body=None)
    client, _ = _client(error=bad)
    with pytest.raises(ProviderError) as info:
        AnthropicProvider(client=client).generate([Message(role="user", content="x")])
    assert not info.value.retryable


def test_embed_is_not_offered():
    client, _ = _client()
    with pytest.raises(NotImplementedError):
        AnthropicProvider(client=client).embed(["x"])
