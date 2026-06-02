# API Reference

Run the API:

```powershell
uvicorn documind_ai.api:app --reload --app-dir src
```

Interactive docs:

```text
http://127.0.0.1:8000/docs
```

## `GET /health`

Returns service status.

Example response:

```json
{
  "status": "ok",
  "collection": "documind_documents",
  "chunks_indexed": 42,
  "llm_enabled": true
}
```

## `POST /ingest`

Uploads and indexes one or more files.

Content type:

```text
multipart/form-data
```

Field:

```text
files
```

Example:

```powershell
curl.exe -X POST "http://127.0.0.1:8000/ingest" `
  -F "files=@examples/sample_knowledge_base.md"
```

Example response:

```json
{
  "files": ["sample_knowledge_base.md"],
  "chunks_added": 1,
  "collection": "documind_documents"
}
```

## `POST /ask`

Asks a question against indexed documents.

Request:

```json
{
  "question": "What vector database does DocuMind use by default?",
  "top_k": 3
}
```

Response:

```json
{
  "question": "What vector database does DocuMind use by default?",
  "answer": "DocuMind uses ChromaDB as the default local vector database.",
  "used_llm": true,
  "sources": [
    {
      "source": "sample_knowledge_base.md",
      "chunk_id": "examples/sample_knowledge_base.md:0:...",
      "score": 0.82,
      "preview": "DocuMind AI is designed...",
      "metadata": {
        "filename": "sample_knowledge_base.md",
        "file_type": "md"
      }
    }
  ]
}
```

## Error Handling

Unsupported file extensions return HTTP 400. Empty indexes return an answer that
asks the caller to upload or ingest documents first.
