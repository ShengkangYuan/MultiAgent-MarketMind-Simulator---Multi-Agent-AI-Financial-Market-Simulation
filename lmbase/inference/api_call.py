"""Mock inference API call module for offline operation."""

from typing import Any, Dict, Optional

from lmbase.inference.base import InferInput, InferOutput


class LangChainAPIInference:
    """Mock inference class — returns canned responses for Rule-based mode.

    For Rule-based simulations this is never actually called; the class
    exists only to satisfy import chains in player code.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.model = kwargs.get("model", "mock")
        self.temperature = kwargs.get("temperature", 0.7)

    def run(self, input_data: InferInput) -> InferOutput:
        return InferOutput(content="Mock response", model=self.model)
