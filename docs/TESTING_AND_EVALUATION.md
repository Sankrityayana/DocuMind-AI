# Testing and Evaluation

## Automated Tests

Current automated tests cover:

- Whitespace normalization.
- Chunk splitting with overlap.
- Preservation of source metadata.

Run:

```powershell
python -m pytest
```

## Compile Check

Run:

```powershell
python -m compileall src tests
```

This verifies that all Python modules are syntactically valid.

## Manual Test Cases

| ID | Test Case | Steps | Expected Result |
| --- | --- | --- | --- |
| TC-01 | Upload Markdown file | Upload `examples/sample_knowledge_base.md` and ingest | Chunks are indexed successfully. |
| TC-02 | Ask known-answer question | Ask which vector DB is used by default | Answer mentions ChromaDB. |
| TC-03 | Ask unsupported question | Ask about content not in the document | System says evidence is insufficient or returns no relevant context. |
| TC-04 | API health check | Call `GET /health` | Status is `ok`. |
| TC-05 | API ask endpoint | Call `POST /ask` after ingestion | Answer and sources are returned. |
| TC-06 | Unsupported upload | Upload unsupported extension | API returns validation error. |

## Evaluation Metrics

For a final-year project demonstration, evaluate the system using:

- Retrieval relevance: whether returned chunks contain the answer.
- Answer groundedness: whether the answer is supported by retrieved sources.
- Response usefulness: whether the answer is clear and concise.
- Latency: time taken for ingestion and question answering.
- Usability: ease of uploading files and inspecting sources.

## Suggested Evaluation Dataset

Create a small set of documents:

- One academic PDF.
- One project policy or handbook.
- One CSV dataset.
- One Markdown knowledge base.

Prepare 20 questions:

- 10 direct factual questions.
- 5 summary questions.
- 5 out-of-context questions.

Record:

- Expected answer.
- Retrieved source file.
- Whether source contained the answer.
- Whether generated answer was correct.

## Result Table Template

| Question | Expected Answer | Retrieved Correct Source | Answer Correct | Notes |
| --- | --- | --- | --- | --- |
| What vector DB is used? | ChromaDB | Yes | Yes | Source preview matched. |
