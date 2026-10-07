"""Mock inference base classes for offline operation."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class InferInput:
    """Mock input container for LLM inference."""
    messages: List[Dict[str, str]] = field(default_factory=list)
    model: str = ""
    temperature: float = 0.7
    max_tokens: int = 4096
    extra: Dict[str, Any] = field(default_factory=dict)


@dataclass
class InferOutput:
    """Mock output container for LLM inference."""
    content: str = ""
    model: str = ""
    usage: Dict[str, int] = field(default_factory=dict)

    @property
    def outputs(self) -> List["InferOutput"]:
        return [self]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "content": self.content,
            "model": self.model,
            "usage": self.usage,
        }
