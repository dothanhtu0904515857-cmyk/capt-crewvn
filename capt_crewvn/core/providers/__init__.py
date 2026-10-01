"""Model-provider abstraction (CLAUDE.md §2, Spec Part C §27).

Only this package may import a vendor SDK. Everything else talks to ``ModelProvider``.
"""

from capt_crewvn.core.providers.base import (
    Message,
    ModelProvider,
    ModelResponse,
    ToolCall,
    ToolSpec,
)

__all__ = ["Message", "ModelProvider", "ModelResponse", "ToolCall", "ToolSpec"]
