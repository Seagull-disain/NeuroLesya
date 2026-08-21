"""Memory-aware wrapper around the NeuroLesya core prototype."""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from main import NeuroLesyaCore
from memory.prototype import MemoryStore


class MemoryAwareNeuroLesyaCore(NeuroLesyaCore):
    """Connect the existing core pipeline to the prototype memory store."""

    def __init__(self, memory: MemoryStore | None = None) -> None:
        super().__init__()
        self.memory = memory or MemoryStore()

    def handle(self, text: str) -> str:
        previous = [item.text for item in self.memory.recent()]
        response = super().handle(text)
        if previous:
            self.last_memory_context = previous
        else:
            self.last_memory_context = []
        if text.strip():
            self.memory.remember(text)
        return response

    def recent_memory(self, limit: int = 5) -> list[str]:
        return [item.text for item in self.memory.recent(limit)]
