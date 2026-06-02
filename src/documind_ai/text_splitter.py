from __future__ import annotations

from collections.abc import Iterable
from hashlib import sha256

from .models import DocumentChunk, LoadedDocument


def normalize_whitespace(text: str) -> str:
    return " ".join(text.replace("\x00", " ").split())


class RecursiveTextChunker:
    """Small dependency-light chunker with LangChain-style overlap semantics."""

    def __init__(self, chunk_size: int = 900, chunk_overlap: int = 150) -> None:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if chunk_overlap < 0:
            raise ValueError("chunk_overlap cannot be negative")
        if chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be smaller than chunk_size")
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str) -> list[str]:
        normalized = normalize_whitespace(text)
        if not normalized:
            return []
        if len(normalized) <= self.chunk_size:
            return [normalized]

        chunks: list[str] = []
        start = 0
        while start < len(normalized):
            end = min(start + self.chunk_size, len(normalized))
            if end < len(normalized):
                boundary = max(
                    normalized.rfind(". ", start, end),
                    normalized.rfind("? ", start, end),
                    normalized.rfind("! ", start, end),
                    normalized.rfind("\n", start, end),
                )
                if boundary > start + self.chunk_size // 2:
                    end = boundary + 1

            chunk = normalized[start:end].strip()
            if chunk:
                chunks.append(chunk)
            if end >= len(normalized):
                break
            start = max(end - self.chunk_overlap, start + 1)
        return chunks

    def split_documents(self, documents: Iterable[LoadedDocument]) -> list[DocumentChunk]:
        chunks: list[DocumentChunk] = []
        for document in documents:
            source = str(document.source_path)
            for index, text in enumerate(self.split_text(document.text)):
                chunk_key = f"{source}:{index}:{sha256(text.encode('utf-8')).hexdigest()[:16]}"
                chunks.append(
                    DocumentChunk(
                        id=chunk_key,
                        text=text,
                        metadata={
                            **document.metadata,
                            "source": source,
                            "chunk_index": index,
                        },
                    )
                )
        return chunks
