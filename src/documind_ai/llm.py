from __future__ import annotations

from openai import OpenAI

from .models import RetrievedChunk


SYSTEM_PROMPT = """You are DocuMind AI, a document question-answering assistant.
Answer only from the provided context. If the context does not contain enough
information, say that the uploaded documents do not provide enough evidence.
Keep answers clear and cite source names when useful."""


def build_context(chunks: list[RetrievedChunk]) -> str:
    sections: list[str] = []
    for index, chunk in enumerate(chunks, start=1):
        source = chunk.metadata.get("filename") or chunk.metadata.get("source") or "unknown"
        sections.append(f"[Source {index}: {source}; score={chunk.score}]\n{chunk.text}")
    return "\n\n".join(sections)


class AnswerGenerator:
    def __init__(self, api_key: str | None, model: str) -> None:
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=api_key) if api_key else None

    @property
    def llm_enabled(self) -> bool:
        return self.client is not None

    def answer(self, question: str, chunks: list[RetrievedChunk]) -> tuple[str, bool]:
        if not chunks:
            return (
                "I could not find relevant context in the indexed documents. "
                "Upload or ingest documents first, then ask again.",
                False,
            )

        if self.client is None:
            return self._extractive_answer(question, chunks), False

        context = build_context(chunks)
        completion = self.client.chat.completions.create(
            model=self.model,
            temperature=0.2,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Question: {question}\n\nContext:\n{context}",
                },
            ],
        )
        message = completion.choices[0].message.content
        return (message or "").strip(), True

    def _extractive_answer(self, question: str, chunks: list[RetrievedChunk]) -> str:
        top = chunks[:3]
        lines = [
            "No LLM key is configured, so here is an extractive answer from the most relevant sources.",
            "",
        ]
        for chunk in top:
            source = chunk.metadata.get("filename") or chunk.metadata.get("source") or "unknown"
            excerpt = chunk.text[:700].strip()
            if len(chunk.text) > 700:
                excerpt += "..."
            lines.append(f"- {source}: {excerpt}")
        return "\n".join(lines)
