# Final Year Project Guide

## Project Title

DocuMind AI: A Retrieval Augmented Generation Chatbot for Question Answering on
User Documents

## Project Category

Artificial Intelligence, Natural Language Processing, Information Retrieval,
Full Stack Application Development

## Problem Statement

Students, researchers, faculty members, and business users often need to search
large PDFs, knowledge bases, and tabular datasets manually. Keyword search is
limited because it cannot understand semantic meaning, and general LLM chatbots
do not automatically know the content of private documents.

This project solves the problem by building a document chatbot that retrieves
relevant passages from user-provided files and generates grounded answers using
retrieval augmented generation.

## Objectives

- Build a chatbot that can answer questions from uploaded PDFs, text files,
  Markdown knowledge bases, and CSV datasets.
- Use semantic embeddings to search by meaning instead of exact keywords.
- Store document chunks in a vector database for efficient retrieval.
- Generate context-aware answers with an LLM when a provider key is configured.
- Provide a local fallback answer mode when no LLM key is available.
- Expose both a web UI and API for practical usability.
- Maintain source references so users can verify answer evidence.

## Scope

### Included

- Document upload and ingestion.
- Text extraction from common academic and knowledge-base formats.
- Chunking with overlap.
- Vector storage and similarity search.
- Source-grounded answer generation.
- Streamlit user interface.
- FastAPI backend.
- Local ChromaDB persistence.
- Documentation and test cases.

### Not Included

- Authentication and user account management.
- Production-grade multi-tenant storage.
- OCR for scanned PDFs.
- Fine-tuning a custom LLM.
- Real-time collaborative document editing.

## Expected Learning Outcomes

- Understanding embeddings and vector similarity search.
- Understanding retrieval augmented generation architecture.
- Designing modular Python services.
- Building API and UI layers around a shared AI pipeline.
- Testing core NLP preprocessing logic.
- Writing technical documentation for an AI software project.

## Suggested Demonstration Flow

1. Start the Streamlit app.
2. Upload `examples/sample_knowledge_base.md`.
3. Click `Ingest documents`.
4. Ask: `What vector database does DocuMind use by default?`
5. Show the answer and source preview.
6. Start FastAPI and open `/docs`.
7. Demonstrate the `/health`, `/ingest`, and `/ask` endpoints.
8. Explain how ChromaDB stores vectors and how retrieved chunks are passed to
   the answer generator.

## Academic Contribution

The contribution is an end-to-end applied RAG system that combines document
processing, semantic retrieval, prompt design, API development, and user
interface design. The system is modular, allowing future replacement of ChromaDB
with hosted vector databases such as Pinecone and future replacement of the LLM
provider with other APIs or local models.

## Future Enhancements

- OCR support for scanned PDFs.
- Pinecone, Qdrant, or Weaviate vector store backend.
- User authentication and per-user document collections.
- Chat history persistence.
- Evaluation dashboard for retrieval precision and answer quality.
- Hybrid search combining keyword search and vector search.
- Support for DOCX, PPTX, and web page ingestion.
- Local LLM support using Ollama or llama.cpp.
