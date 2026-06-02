# Presentation Outline

## Slide 1: Title

DocuMind AI: RAG Chatbot on Your Own Documents

Include:

- Student name
- Guide name
- Department
- University
- Academic year

## Slide 2: Problem Statement

Manual document search is slow, keyword search is limited, and normal LLMs do
not know private user documents.

## Slide 3: Objectives

- Upload documents.
- Search semantically.
- Retrieve relevant context.
- Generate source-grounded answers.
- Provide UI and API access.

## Slide 4: Technologies Used

- Python
- Streamlit
- FastAPI
- ChromaDB
- PyPDF
- OpenAI API
- Pytest

## Slide 5: System Architecture

Show:

```text
Upload -> Text Extraction -> Chunking -> Embeddings -> Vector DB
Question -> Retrieval -> Prompt -> LLM/Fallback -> Answer + Sources
```

## Slide 6: RAG Pipeline

Explain:

- Embeddings convert text into vectors.
- Vector search finds semantic matches.
- Retrieved context is passed to the answer generator.
- Source previews support verification.

## Slide 7: Modules

- Loader
- Chunker
- Vector store
- Retriever
- Answer generator
- Streamlit UI
- FastAPI backend

## Slide 8: Implementation Screens

Add screenshots of:

- Streamlit upload and chat UI.
- FastAPI Swagger docs.
- Example answer with sources.

## Slide 9: Testing

Mention:

- Unit tests.
- Compile checks.
- Manual ingestion and Q&A test cases.

## Slide 10: Results

Show:

- Supported file types.
- Example question and answer.
- Retrieved source preview.

## Slide 11: Limitations

- No OCR.
- No authentication.
- Local vector DB only by default.
- LLM quality depends on retrieved context.

## Slide 12: Future Scope

- OCR
- Pinecone or Qdrant
- User accounts
- Local LLM
- Evaluation dashboard

## Slide 13: Conclusion

DocuMind AI demonstrates a practical AI system using embeddings, vector search,
prompting, and RAG to help users interact with their own documents.
