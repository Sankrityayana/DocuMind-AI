# Sample Knowledge Base

DocuMind AI is designed to answer questions from private documents. It uses
retrieval augmented generation so answers can be grounded in uploaded source
material.

The default vector database is ChromaDB. The application can be extended to
Pinecone by implementing the vector store protocol used by the RAG service.

The Streamlit app is useful for analysts and students. The FastAPI service is
useful when integrating document Q&A into another product.
