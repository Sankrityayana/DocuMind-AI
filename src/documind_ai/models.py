from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


@dataclass(frozen=True)
class DocumentChunk:
    id: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RetrievedChunk:
    id: str
    text: str
    score: float
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class LoadedDocument:
    source_path: Path
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)
    top_k: int | None = Field(default=None, ge=1, le=20)


class SourceResponse(BaseModel):
    source: str
    chunk_id: str
    score: float
    preview: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class AskResponse(BaseModel):
    question: str
    answer: str
    used_llm: bool
    sources: list[SourceResponse]


class IngestResponse(BaseModel):
    files: list[str]
    chunks_added: int
    collection: str
