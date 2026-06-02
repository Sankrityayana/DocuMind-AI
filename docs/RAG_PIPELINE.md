# RAG Pipeline

RAG stands for retrieval augmented generation. The idea is to retrieve relevant
source material first, then ask an LLM to answer from that material.

## 1. Document Loading

Supported formats:

- PDF
- TXT
- Markdown
- CSV

PDF pages are extracted with PyPDF. CSV rows are converted into text records so
they can be embedded like other documents.

## 2. Chunking

Long documents are split into overlapping chunks. Chunking is necessary because
embedding models and LLM prompts have context limits.

Defaults:

- Chunk size: `900`
- Chunk overlap: `150`

Overlap helps preserve context across chunk boundaries.

## 3. Embeddings

ChromaDB embeds each chunk and stores the resulting vectors. At query time, the
question is embedded and compared with stored vectors.

The current implementation uses Chroma's default embedding path. You can replace
that with a custom sentence-transformer or hosted embedding provider by changing
`ChromaVectorStore`.

## 4. Vector Search

For each question, DocuMind AI retrieves the top `k` matching chunks.

The default is:

```text
DOCUMIND_TOP_K=5
```

Higher values provide more context but may add noise and increase prompt cost.

## 5. Prompting

The prompt tells the model to answer only from retrieved context. It also asks
the model to say when the source documents do not contain enough evidence.

This is a grounding strategy. It does not guarantee perfect factuality, but it
reduces unsupported answers and makes source review possible.

## 6. Answer Generation

When `OPENAI_API_KEY` is set, the model generates a concise answer. When it is
not set, DocuMind AI returns an extractive answer from the highest scoring
chunks.

## Quality Tips

- Upload focused documents instead of huge unrelated dumps.
- Tune chunk size for your content. Dense legal or research docs often benefit
  from smaller chunks; long procedural docs may work better with larger chunks.
- Keep `top_k` between 3 and 8 for most use cases.
- Review source previews before trusting important answers.
