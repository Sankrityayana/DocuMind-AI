from __future__ import annotations

from pathlib import Path

from .config import Settings, settings
from .llm import AnswerGenerator
from .loaders import load_documents
from .models import AskResponse, IngestResponse, SourceResponse
from .text_splitter import RecursiveTextChunker
from .vector_store import ChromaVectorStore


class RagService:
    def __init__(self, app_settings: Settings = settings) -> None:
        self.settings = app_settings
        self.settings.ensure_directories()
        self.chunker = RecursiveTextChunker(
            chunk_size=self.settings.chunk_size,
            chunk_overlap=self.settings.chunk_overlap,
        )
        self.vector_store = ChromaVectorStore(
            persist_dir=self.settings.chroma_dir,
            collection_name=self.settings.collection_name,
        )
        self.answer_generator = AnswerGenerator(
            api_key=self.settings.openai_api_key,
            model=self.settings.openai_model,
        )

    def ingest_paths(self, paths: list[Path]) -> IngestResponse:
        documents = load_documents(paths)
        chunks = self.chunker.split_documents(documents)
        added = self.vector_store.add_chunks(chunks)
        return IngestResponse(
            files=[path.name for path in paths],
            chunks_added=added,
            collection=self.settings.collection_name,
        )

    def ask(self, question: str, top_k: int | None = None) -> AskResponse:
        k = top_k or self.settings.top_k
        chunks = self.vector_store.query(question=question, top_k=k)
        answer, used_llm = self.answer_generator.answer(question, chunks)
        sources = [
            SourceResponse(
                source=str(chunk.metadata.get("filename") or chunk.metadata.get("source") or "unknown"),
                chunk_id=chunk.id,
                score=chunk.score,
                preview=chunk.text[:320],
                metadata=chunk.metadata,
            )
            for chunk in chunks
        ]
        return AskResponse(
            question=question,
            answer=answer,
            used_llm=used_llm,
            sources=sources,
        )

    def document_count(self) -> int:
        return self.vector_store.count()


def save_upload(filename: str, content: bytes, upload_dir: Path) -> Path:
    upload_dir.mkdir(parents=True, exist_ok=True)
    safe_name = Path(filename).name
    if not safe_name:
        raise ValueError("Uploaded file must have a filename")
    destination = upload_dir / safe_name
    destination.write_bytes(content)
    return destination
