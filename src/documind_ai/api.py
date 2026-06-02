from __future__ import annotations

from fastapi import FastAPI, File, HTTPException, UploadFile

from .config import settings
from .models import AskRequest, AskResponse, IngestResponse
from .rag import RagService, save_upload


app = FastAPI(
    title="DocuMind AI API",
    description="RAG chatbot API for PDFs, knowledge bases, and datasets.",
    version="0.1.0",
)
rag_service = RagService(settings)


@app.get("/health")
def health() -> dict[str, int | str | bool]:
    return {
        "status": "ok",
        "collection": settings.collection_name,
        "chunks_indexed": rag_service.document_count(),
        "llm_enabled": rag_service.answer_generator.llm_enabled,
    }


@app.post("/ingest", response_model=IngestResponse)
async def ingest(files: list[UploadFile] = File(...)) -> IngestResponse:
    try:
        paths = []
        for file in files:
            content = await file.read()
            paths.append(save_upload(file.filename or "upload", content, settings.upload_dir))
        return rag_service.ingest_paths(paths)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    return rag_service.ask(question=request.question, top_k=request.top_k)
