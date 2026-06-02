# Viva Questions and Answers

## 1. What is the main objective of this project?

The objective is to build a chatbot that answers questions from user-uploaded
documents using semantic search and retrieval augmented generation.

## 2. What is RAG?

RAG stands for retrieval augmented generation. It retrieves relevant information
from a knowledge source before generating an answer with an LLM.

## 3. Why not directly ask the LLM?

An LLM does not automatically know private uploaded documents. RAG provides the
document context needed to answer from private sources.

## 4. What are embeddings?

Embeddings are numerical vector representations of text. Text with similar
meaning tends to have similar vectors.

## 5. Why is a vector database used?

A vector database stores embeddings and supports similarity search, allowing the
system to retrieve semantically relevant chunks efficiently.

## 6. Why did you use ChromaDB?

ChromaDB is easy to run locally, supports persistent storage, and is suitable
for development and academic demonstrations.

## 7. What is chunking?

Chunking splits long documents into smaller overlapping pieces so they can be
embedded, retrieved, and passed into prompts effectively.

## 8. Why is overlap used in chunking?

Overlap preserves context between adjacent chunks and reduces the chance that an
important sentence is split away from supporting information.

## 9. What happens if no OpenAI API key is configured?

The system still performs retrieval and returns an extractive answer from the
most relevant chunks.

## 10. What are the main modules?

The main modules are document loader, text chunker, vector store, answer
generator, RAG service, Streamlit UI, and FastAPI backend.

## 11. How does the system reduce hallucination?

It instructs the LLM to answer only from retrieved context and returns source
previews for verification.

## 12. What are the limitations?

The current system does not support OCR, authentication, production multi-user
storage, or fine-tuned models.

## 13. How can this project be improved?

Future improvements include OCR, user accounts, hosted vector stores, local LLMs,
hybrid search, and evaluation dashboards.
