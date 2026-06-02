# Project Synopsis

## Title

DocuMind AI: A Retrieval Augmented Generation Chatbot for Question Answering on
User Documents

## Abstract

DocuMind AI is an AI-based document question-answering system that allows users
to chat with PDFs, knowledge bases, and datasets. The system extracts text from
uploaded files, splits the text into overlapping chunks, stores semantic
representations in a vector database, retrieves relevant chunks for a user
query, and produces source-grounded answers using a large language model.

The project addresses the limitation of manual document search and traditional
keyword-based retrieval. By using embeddings and vector search, the system can
find semantically relevant content even when the query does not exactly match
the document wording. The application includes a Streamlit interface for users
and a FastAPI backend for integration with other systems.

## Problem Definition

Users frequently need to extract information from long documents and datasets.
Manual reading is time-consuming, while simple keyword search often fails when
the query uses different wording from the source document. General-purpose LLMs
may hallucinate or answer from public knowledge instead of private documents.

DocuMind AI solves this by retrieving relevant document chunks before generating
answers, thereby grounding the response in the uploaded material.

## Proposed System

The proposed system follows a retrieval augmented generation pipeline:

1. Load documents from user uploads.
2. Extract text from PDF, Markdown, TXT, and CSV files.
3. Split text into chunks with overlap.
4. Store chunks in ChromaDB with vector embeddings.
5. Retrieve top matching chunks for each question.
6. Generate an answer using the retrieved context.
7. Return answer text and source references.

## Technology Stack

| Layer | Technology |
| --- | --- |
| Programming Language | Python |
| UI | Streamlit |
| API | FastAPI |
| Vector Database | ChromaDB |
| PDF Processing | PyPDF |
| Data Processing | Pandas, CSV utilities |
| LLM Provider | OpenAI API, optional |
| Testing | Pytest |

## Modules

- Document Loader Module
- Text Chunking Module
- Vector Store Module
- Retrieval Module
- Prompt and Answer Generation Module
- Streamlit UI Module
- FastAPI Module
- Testing Module

## Expected Outcome

The expected outcome is a working AI chatbot that can answer user questions from
uploaded documents and show source evidence for retrieved context.
