"""A deterministic provider for tests and offline evaluation dry-runs. It never calls a network."""

from capt_crewvn.core.providers.base import Message, ModelResponse, ToolSpec


class ScriptedProvider:
    name = "scripted"

    def __init__(self, replies: list[str], model_id: str = "scripted-v0") -> None:
        self.model_id = model_id
        self._replies = list(replies)
        self.received: list[list[Message]] = []

    def generate(
        self,
        messages: list[Message],
        tools: list[ToolSpec] | None = None,
        max_output_tokens: int | None = None,
    ) -> ModelResponse:
        self.received.append(messages)
        text = self._replies.pop(0) if self._replies else ""
        return ModelResponse(text=text, provider=self.name, model_id=self.model_id, stop_reason="end")

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [[float(len(t))] for t in texts]
