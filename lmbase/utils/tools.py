"""Mock BlockBasedStoreManager — minimal file-based persistence.

Replaces the real lmbase.utils.tools.BlockBasedStoreManager with a simple
JSON-per-file implementation so masim can run offline.
"""

import json
import os
from typing import Any, Dict, List, Optional


class BlockBasedStoreManager:
    """Simple file-keyed JSON store — one file per savename."""

    def __init__(self, folder: str, file_format: str = "json", block_size: int = 50):
        self.folder = folder
        self.file_format = file_format
        self.block_size = block_size
        os.makedirs(folder, exist_ok=True)

    def _path(self, savename: str) -> str:
        ext = ".json" if self.file_format == "json" else f".{self.file_format}"
        if not savename.endswith(ext):
            savename += ext
        return os.path.join(self.folder, savename)

    def save(self, savename: str, data: Any) -> None:
        path = self._path(savename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)

    def load(self, savename: str) -> Any:
        path = self._path(savename)
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def flush(self) -> None:
        pass  # No-op for the mock implementation
