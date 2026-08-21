"""Minimal, provider-agnostic NeuroLesya core prototype."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Request:
    text: str


@dataclass
class Context:
    messages: list[str] = field(default_factory=list)
    data: dict[str, Any] = field(default_factory=dict)


class IntentDetector:
    def detect(self, request: Request) -> str:
        text = request.text.strip().lower()
        if not text:
            return "empty"
        if "?" in text:
            return "question"
        return "general"


class ContextBuilder:
    def build(self, request: Request) -> Context:
        return Context(messages=[request.text])


class Orchestrator:
    def run(self, intent: str, context: Context) -> str:
        if intent == "empty":
            return "Потрібно отримати запит від користувача."
        if intent == "question":
            return f"Отримано запит: {context.messages[-1]}"
        return f"Отримано повідомлення: {context.messages[-1]}"


class ResponseBuilder:
    def build(self, result: str) -> str:
        return result


class NeuroLesyaCore:
    def __init__(self) -> None:
        self.intent = IntentDetector()
        self.context = ContextBuilder()
        self.orchestrator = Orchestrator()
        self.response = ResponseBuilder()

    def handle(self, text: str) -> str:
        request = Request(text=text)
        intent = self.intent.detect(request)
        context = self.context.build(request)
        result = self.orchestrator.run(intent, context)
        return self.response.build(result)


if __name__ == "__main__":
    core = NeuroLesyaCore()
    print(core.handle("Привіт, НейроЛесю!"))
