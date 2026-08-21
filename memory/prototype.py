"""Minimal in-memory memory layer for the NeuroLesya prototype."""

from dataclasses import dataclass, field
import re


@dataclass
class MemoryItem:
    text: str
    kind: str = "conversation"
    tags: list[str] = field(default_factory=list)


class MemoryStore:
    """Simple replaceable memory store for the first prototype."""

    def __init__(self) -> None:
        self.items: list[MemoryItem] = []

    def remember(self, text: str, kind: str = "conversation", tags: list[str] | None = None) -> None:
        self.items.append(MemoryItem(text=text, kind=kind, tags=tags or []))

    def recent(self, limit: int = 5) -> list[MemoryItem]:
        if limit < 1:
            return []
        return self.items[-limit:]

    def search(self, query: str, limit: int = 5) -> list[MemoryItem]:
        """Return memories ranked by simple token overlap with the query."""
        if limit < 1 or not query.strip():
            return []

        query_tokens = self._tokens(query)
        if not query_tokens:
            return []

        scored: list[tuple[int, int, MemoryItem]] = []
        for index, item in enumerate(self.items):
            item_tokens = self._tokens(item.text) | {tag.lower() for tag in item.tags}
            score = len(query_tokens & item_tokens)
            if score:
                scored.append((score, index, item))

        scored.sort(key=lambda entry: (entry[0], entry[1]), reverse=True)
        return [item for _, _, item in scored[:limit]]

    @staticmethod
    def _tokens(text: str) -> set[str]:
        return set(re.findall(r"[\w'-]{3,}", text.lower(), flags=re.UNICODE))

    def clear(self) -> None:
        self.items.clear()
