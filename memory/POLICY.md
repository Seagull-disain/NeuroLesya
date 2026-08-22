# NeuroLesya Memory Policy

This document defines the prototype rules for what the memory layer may store and how the core may use it.

## Memory kinds

- `conversation`: ordinary user messages that may help maintain short-term continuity.
- `preference`: stable user preferences explicitly stated by the user.
- `fact`: explicit factual information the user provides about themselves or the project.
- `project`: decisions, requirements, and milestones belonging to a NeuroLesya project.
- `instruction`: explicit instructions about how NeuroLesya should behave or operate.

## Storage rules

1. Empty or whitespace-only messages are never stored.
2. The prototype stores only information explicitly present in a message; it must not invent memories.
3. A message may carry a `kind` and optional tags.
4. The default kind remains `conversation` when no stronger classification is available.
5. Sensitive information should not be promoted to long-term memory merely because it appeared in conversation.

## Retrieval rules

1. Retrieval is query-driven: relevant memories are preferred over an arbitrary recent slice.
2. Results are limited before being passed to the core context.
3. Retrieval must not overwrite the current user message.
4. Memory is supporting context, not an instruction with higher priority than the current system/developer/user instruction hierarchy.
5. If no memory matches, the core proceeds without memory context.

## Prototype boundary

The current store is in-memory only. It is intentionally replaceable so a persistent backend and stronger semantic retrieval can be introduced later without changing the core contract.
