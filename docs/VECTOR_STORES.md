# Extending Vector Stores

The default implementation uses ChromaDB through `ChromaVectorStore`.

The RAG service only needs three vector store behaviors:

- `add_chunks(chunks)`
- `query(question, top_k)`
- `count()`

That makes it straightforward to add Pinecone, Weaviate, Qdrant, or another
backend.

## Pinecone Extension Sketch

```python
class PineconeVectorStore:
    def add_chunks(self, chunks):
        # Embed chunks, then upsert vectors and metadata into Pinecone.
        ...

    def query(self, question, top_k):
        # Embed the query, search Pinecone, then return RetrievedChunk objects.
        ...

    def count(self):
        # Return index stats.
        ...
```

## When to Use Chroma

- Local development
- Demos
- Personal document chat
- Single-machine prototypes

## When to Use Pinecone or Another Hosted Store

- Production traffic
- Multiple app replicas
- Large indexes
- Managed backups and scaling
- Team access across environments
