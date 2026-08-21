"""Minimal in-memory memory layer for the NeuroLesya prototype."""

from dataclasses import dataclass, field


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

    def clear(self) -> None:
        self.items.clear()
