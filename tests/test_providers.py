import ast
from pathlib import Path

from capt_crewvn.core.providers import Message, ModelProvider
from capt_crewvn.core.providers.scripted import ScriptedProvider

PACKAGE = Path(__file__).resolve().parents[1] / "capt_crewvn"
VENDOR_SDKS = {"anthropic", "openai", "google", "mistralai", "cohere", "ollama"}


def test_scripted_provider_satisfies_protocol():
    provider = ScriptedProvider(["ok"])
    assert isinstance(provider, ModelProvider)
    assert provider.generate([Message(role="user", content="hi")]).text == "ok"


def test_vendor_sdks_only_imported_in_providers():
    for path in PACKAGE.rglob("*.py"):
        if "providers" in path.parts:
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module]
            for name in names:
                assert name.split(".")[0] not in VENDOR_SDKS, f"{path} imports {name}"
