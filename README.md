# DocuMind AI

DocuMind AI is a final-year university project that demonstrates a Retrieval
Augmented Generation chatbot for user documents. It allows users to upload PDFs,
knowledge-base files, and datasets, then ask natural-language questions and
receive source-grounded answers.

The system combines semantic search, vector databases, prompt engineering, and
LLM-based answer generation in a practical full-stack AI application.

## Final Year Project Summary

| Item | Details |
| --- | --- |
| Project Title | DocuMind AI: A RAG Chatbot on Your Own Documents |
| Domain | Artificial Intelligence, NLP, Information Retrieval |
| Core Technique | Retrieval Augmented Generation |
| AI Skills | Embeddings, Vector Search, Prompting, Source Grounding |
| UI | Streamlit |
| API | FastAPI |
| Vector Database | ChromaDB |
| Optional LLM | OpenAI API |

## Problem Statement

Users often need to search large PDFs, knowledge bases, and datasets manually.
Keyword search is limited because it cannot understand semantic meaning, while
general LLMs cannot reliably answer from private documents unless the document
content is provided.

DocuMind AI solves this by retrieving relevant document chunks with vector
search and then generating answers from that retrieved context.

## Objectives

- Build a chatbot that answers questions from uploaded documents.
- Support PDF, TXT, Markdown, and CSV inputs.
- Use embeddings and vector search for semantic retrieval.
- Generate source-grounded answers with an LLM when configured.
- Provide a local extractive fallback when no LLM key is available.
- Expose both Streamlit UI and FastAPI API access.
- Provide documentation suitable for university submission.

## Features

- Document upload and ingestion.
- Text extraction from common file formats.
- Overlapping chunk generation.
- Persistent ChromaDB vector storage.
- Semantic similarity search.
- LLM answer generation with grounded context.
- Source previews for answer verification.
- REST API for integration.
- Final-year project docs, report template, viva questions, and presentation
  outline.

## Tech Stack

- Python 3.10+
- Streamlit
- FastAPI
- ChromaDB
- PyPDF
- Pandas
- OpenAI API
- Pytest

## Repository Layout

```text
.
|-- docs/                         Detailed project and academic docs
|-- examples/                     Sample document and API request examples
|-- src/documind_ai/              Application package
|-- storage/                      Local runtime data, ignored by git
|-- tests/                        Unit tests
|-- .env.example                  Environment template
|-- pyproject.toml                Project metadata and tooling config
|-- requirements.txt              Runtime dependencies
`-- README.md                     Project overview
```

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

## How It Works

1. Files are uploaded through Streamlit or the API.
2. The loader extracts text from PDF, TXT, Markdown, or CSV inputs.
3. Text is split into overlapping chunks.
4. Chunks are embedded and stored in ChromaDB.
5. User questions are matched against stored chunks using semantic search.
6. Retrieved context is formatted into a grounded prompt.
7. The LLM generates an answer using the retrieved context.
8. The system returns the answer with source previews.

If no LLM provider is configured, DocuMind AI returns an extractive answer from
the retrieved chunks so local development and academic demonstrations still
work.

## Academic Documentation

- [Final Year Project Guide](docs/FINAL_YEAR_PROJECT_GUIDE.md)
- [Project Synopsis](docs/SYNOPSIS.md)
- [Software Requirements Specification](docs/SRS.md)
- [Project Report Template](docs/PROJECT_REPORT.md)
- [Testing and Evaluation](docs/TESTING_AND_EVALUATION.md)
- [Presentation Outline](docs/PRESENTATION_OUTLINE.md)
- [Viva Questions](docs/VIVA_QUESTIONS.md)
- [Project Plan](docs/PROJECT_PLAN.md)

## Technical Documentation

- [Setup Guide](docs/SETUP.md)
- [Architecture](docs/ARCHITECTURE.md)
- [RAG Pipeline](docs/RAG_PIPELINE.md)
- [API Reference](docs/API.md)
- [User Guide](docs/USER_GUIDE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Extending Vector Stores](docs/VECTOR_STORES.md)

## Development Checks

```powershell
python -m compileall src tests
python -m pytest
```

## Future Scope

- OCR support for scanned PDFs.
- Pinecone, Qdrant, or Weaviate vector database support.
- User authentication and document collections.
- Chat history persistence.
- Evaluation dashboard for retrieval and answer quality.
- Local LLM support through Ollama or llama.cpp.

## License

MIT. See [LICENSE](LICENSE).
