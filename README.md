# DocuMind AI

DocuMind AI is a RAG chatbot for your own documents. It ingests PDFs, text files,
Markdown knowledge bases, and CSV datasets, stores semantic chunks in a vector
database, retrieves the most relevant context, and answers questions with an LLM.

The project ships with:

- Streamlit app for interactive document upload and chat.
- FastAPI service for programmatic ingestion and question answering.
- ChromaDB as the default local vector database.
- Optional OpenAI chat completion support when `OPENAI_API_KEY` is configured.
- Local extractive fallback answers when no LLM key is available.
- A modular RAG pipeline that can be extended to Pinecone or LlamaIndex.

## AI Skills Covered

- Embeddings
- Vector search
- Retrieval augmented generation
- Prompting
- Source-grounded answer generation

## Tech Stack

- Python 3.10+
- LangChain-style document chunking and retrieval patterns
- ChromaDB for local vector search
- FastAPI for API access
- Streamlit for UI
- PyPDF for PDF parsing
- Sentence Transformers or Chroma default embeddings

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create environment config:

```powershell
Copy-Item .env.example .env
```

Run the Streamlit app:

```powershell
streamlit run src/documind_ai/streamlit_app.py
```

Run the FastAPI server:

```powershell
uvicorn documind_ai.api:app --reload --app-dir src
```

Open API docs at:

```text
http://127.0.0.1:8000/docs
```

## Environment Variables

| Variable | Default | Description |
| --- | --- | --- |
| `DOCUMIND_CHROMA_DIR` | `./storage/chroma` | Persistent Chroma database path. |
| `DOCUMIND_COLLECTION` | `documind_documents` | Chroma collection name. |
| `DOCUMIND_UPLOAD_DIR` | `./storage/uploads` | Directory for uploaded files. |
| `DOCUMIND_CHUNK_SIZE` | `900` | Target text chunk size. |
| `DOCUMIND_CHUNK_OVERLAP` | `150` | Overlap between adjacent chunks. |
| `DOCUMIND_TOP_K` | `5` | Number of retrieved chunks per query. |
| `OPENAI_API_KEY` | unset | Enables OpenAI answer generation when set. |
| `OPENAI_MODEL` | `gpt-4o-mini` | OpenAI chat model. |

## Repository Layout

```text
.
├── docs/                         Detailed documentation
├── examples/                     Sample documents and API requests
├── src/documind_ai/              Application package
├── storage/                      Local runtime data, ignored by git
├── tests/                        Unit tests
├── .env.example                  Environment template
├── pyproject.toml                Project metadata and tooling config
└── requirements.txt              Runtime dependencies
```

## How It Works

1. Files are uploaded through Streamlit or the API.
2. The loader extracts text from PDF, TXT, MD, and CSV inputs.
3. Text is split into overlapping chunks.
4. Chunks are embedded and stored in ChromaDB.
5. User questions are embedded and matched against stored chunks.
6. Retrieved context is formatted into a grounded prompt.
7. The LLM answers using only the retrieved context, with source references.

If no LLM provider is configured, DocuMind AI returns a concise extractive answer
from the retrieved chunks so local development still works.

## Documentation

- [Setup Guide](docs/SETUP.md)
- [Architecture](docs/ARCHITECTURE.md)
- [RAG Pipeline](docs/RAG_PIPELINE.md)
- [API Reference](docs/API.md)
- [User Guide](docs/USER_GUIDE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Extending Vector Stores](docs/VECTOR_STORES.md)

## Development

Run checks:

```powershell
python -m compileall src tests
python -m pytest
```

Format and lint tools can be added on top of the existing `pyproject.toml`
configuration if your team wants stricter CI.

## License

MIT. See [LICENSE](LICENSE).
