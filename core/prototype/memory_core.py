"""Memory-aware wrapper around the NeuroLesya core prototype."""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from main import NeuroLesyaCore, Request
from memory.persistent import PersistentMemoryStore
from memory.prototype import MemoryStore


class MemoryAwareNeuroLesyaCore(NeuroLesyaCore):
    """Connect the core pipeline to persistent memory by default."""

    def __init__(self, memory: MemoryStore | None = None, memory_path: str | Path = "memory.json") -> None:
        super().__init__()
        self.memory = memory if memory is not None else PersistentMemoryStore(memory_path)

    def handle(self, text: str) -> str:
        request = Request(text=text)
        intent = self.intent.detect(request)
        relevant = self.memory.search(text, limit=5)
        context = self.context.build(request)
        context.messages = [item.text for item in relevant] + context.messages
        context.data["memory_count"] = len(relevant)
        result = self.orchestrator.run(intent, context)
        response = self.response.build(result)
        if text.strip():
            self.memory.remember(text)
        self.last_memory_context = [item.text for item in relevant]
        return response

    def recent_memory(self, limit: int = 5) -> list[str]:
        return [item.text for item in self.memory.recent(limit)]
