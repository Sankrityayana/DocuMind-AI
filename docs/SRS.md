# Software Requirements Specification

## 1. Introduction

### 1.1 Purpose

This document defines the software requirements for DocuMind AI, a RAG chatbot
for question answering over user-provided documents.

### 1.2 Intended Users

- Students
- Researchers
- Faculty members
- Knowledge workers
- Developers integrating document Q&A into applications

### 1.3 Product Perspective

DocuMind AI is a standalone AI application with a web interface and API. It can
run locally and persist embeddings in a local ChromaDB database.

## 2. Functional Requirements

| ID | Requirement |
| --- | --- |
| FR-01 | The system shall allow users to upload PDF, TXT, Markdown, and CSV files. |
| FR-02 | The system shall extract text from supported file formats. |
| FR-03 | The system shall split extracted text into overlapping chunks. |
| FR-04 | The system shall store chunks in a vector database. |
| FR-05 | The system shall retrieve relevant chunks for a user question. |
| FR-06 | The system shall generate answers using retrieved chunks. |
| FR-07 | The system shall return source references with each answer. |
| FR-08 | The system shall provide a Streamlit web interface. |
| FR-09 | The system shall expose FastAPI endpoints for health, ingestion, and Q&A. |
| FR-10 | The system shall work in fallback mode when no LLM API key is configured. |

## 3. Non-Functional Requirements

| ID | Requirement |
| --- | --- |
| NFR-01 | The system should be modular and easy to extend. |
| NFR-02 | The system should persist vector data locally. |
| NFR-03 | The system should provide clear documentation. |
| NFR-04 | The system should be testable using automated unit tests. |
| NFR-05 | The system should avoid exposing secrets in source control. |

## 4. External Interface Requirements

### 4.1 User Interface

The Streamlit interface shall include:

- File uploader
- Ingest button
- Indexed chunk count
- Chat input
- Assistant responses
- Expandable source previews

### 4.2 API Interface

The FastAPI service shall include:

- `GET /health`
- `POST /ingest`
- `POST /ask`

### 4.3 Environment Interface

The system shall read runtime configuration from environment variables defined
in `.env.example`.

## 5. Constraints

- The default vector store is ChromaDB.
- The application requires Python 3.10 or newer.
- Generated LLM answers require an API key.
- Scanned PDFs without embedded text are not supported unless OCR is added.

## 6. Assumptions

- Uploaded documents contain extractable text.
- Users understand that answers should be verified using source previews.
- Local storage is sufficient for development and academic demonstration.
