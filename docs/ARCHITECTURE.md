# Architecture

DocuMind AI separates the RAG pipeline from presentation layers.

```text
Streamlit UI  ----\
                  +--> RagService --> Loader --> Chunker --> Vector Store
FastAPI API   ----/                      |                       |
                                         +------ AnswerGenerator <-+
```

## Main Modules

| Module | Responsibility |
| --- | --- |
| `config.py` | Loads environment settings and creates runtime directories. |
| `loaders.py` | Extracts text from PDF, TXT, Markdown, and CSV files. |
| `text_splitter.py` | Splits long documents into overlapping semantic chunks. |
| `vector_store.py` | Stores and retrieves chunks using ChromaDB. |
| `llm.py` | Builds grounded prompts and calls OpenAI when configured. |
| `rag.py` | Coordinates ingestion, retrieval, and answer generation. |
| `api.py` | Exposes FastAPI endpoints. |
| `streamlit_app.py` | Provides the interactive document chat UI. |

## Design Decisions

### One Shared Service

Both Streamlit and FastAPI call `RagService`. This avoids two separate RAG
implementations and keeps answers consistent across UI and API usage.

### Local First

ChromaDB is used as the default vector database because it runs locally and is
simple to persist in a project folder. This keeps development friction low.

### LLM Optional

Generated answers require an OpenAI API key. Without a key, the app still
performs semantic retrieval and returns the best matching excerpts.

### Source Grounding

Every answer includes source previews. This makes it possible to inspect what
the model used and reduces blind trust in generated responses.

## Data Flow

1. A user uploads files.
2. Files are saved to the configured upload directory.
3. The loader extracts raw text.
4. The chunker normalizes and splits the text.
5. Chunks are upserted into ChromaDB with source metadata.
6. A question is embedded by Chroma's embedding function.
7. The top matching chunks are retrieved.
8. Retrieved chunks are formatted as context.
9. The answer generator either calls the LLM or returns extractive excerpts.
