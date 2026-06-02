# Project Report Template

## 1. Title

DocuMind AI: A Retrieval Augmented Generation Chatbot for Question Answering on
User Documents

## 2. Abstract

DocuMind AI is a document question-answering system that uses retrieval
augmented generation to answer user queries from uploaded PDFs, knowledge bases,
and datasets. The system extracts text, divides it into chunks, stores semantic
vectors in ChromaDB, retrieves relevant context, and generates grounded answers
with source references. It includes a Streamlit interface and a FastAPI backend.

## 3. Introduction

Large documents are difficult to search manually. Traditional keyword search is
limited because it depends on exact terms. Large language models are powerful
but do not automatically know the contents of private documents. This project
combines vector search and LLM prompting so answers are grounded in uploaded
documents.

## 4. Literature Background

The project is based on three core concepts:

- Embeddings: numerical representations of text meaning.
- Vector search: similarity search over embeddings.
- Retrieval augmented generation: retrieving relevant knowledge before
  generating a response.

## 5. Existing System

Existing document search systems often use keyword matching. General chatbots
can answer broad questions but cannot reliably answer from private documents
unless document context is provided. Manual PDF search also becomes inefficient
when documents are long or when many files are involved.

## 6. Proposed System

The proposed system accepts user documents, extracts text, chunks the content,
indexes it in a vector database, and answers questions using retrieved context.
The system provides both a UI and API, making it useful for demonstrations and
future product integration.

## 7. System Architecture

The system has these main layers:

- Presentation layer: Streamlit UI and FastAPI endpoints.
- Application layer: RAG orchestration service.
- Processing layer: document loading and chunking.
- Retrieval layer: ChromaDB vector database.
- Generation layer: OpenAI LLM or local extractive fallback.

## 8. Implementation

Implementation is organized under `src/documind_ai`:

- `loaders.py`: document extraction.
- `text_splitter.py`: chunking logic.
- `vector_store.py`: ChromaDB integration.
- `llm.py`: prompt and answer generation.
- `rag.py`: pipeline orchestration.
- `api.py`: FastAPI routes.
- `streamlit_app.py`: user interface.

## 9. Testing

The project includes unit tests for text normalization, chunking, and metadata
preservation. Additional manual testing can be performed by uploading sample
documents and asking known-answer questions.

## 10. Results

The system successfully indexes supported document formats and returns relevant
source previews with answers. It can operate with an LLM API key or in local
extractive fallback mode.

## 11. Limitations

- No OCR for scanned PDFs.
- No user authentication.
- Local ChromaDB is best suited for development and demonstration.
- LLM answer quality depends on retrieved context quality.

## 12. Future Scope

- Add OCR support.
- Add hosted vector database support.
- Add user accounts and document collections.
- Add evaluation metrics.
- Add local LLM integration.
- Add chat history persistence.

## 13. Conclusion

DocuMind AI demonstrates a practical application of embeddings, vector search,
prompting, and retrieval augmented generation. It provides a working AI system
that can help users extract information from their own documents efficiently.
