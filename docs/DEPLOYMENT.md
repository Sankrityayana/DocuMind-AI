# Deployment Guide

DocuMind AI can be deployed as either a Streamlit app, a FastAPI service, or
both.

## Streamlit Community Cloud

1. Push the repository to GitHub.
2. Create a new Streamlit app from the repository.
3. Set the main file to:

   ```text
   src/documind_ai/streamlit_app.py
   ```

4. Add secrets for `OPENAI_API_KEY` if generated answers are needed.

For persistent production storage, use a mounted disk or a hosted vector
database instead of local Chroma storage.

## Docker

Create a minimal Dockerfile:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "documind_ai.api:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]
```

## Production Notes

- Put uploads and vector storage on persistent volumes.
- Add authentication before exposing private document Q&A publicly.
- Use request size limits for uploads.
- Log ingestion and query events, but avoid logging sensitive document content.
- Consider a hosted vector database for multiple replicas.
- Add background jobs for large document ingestion.

## Suggested CI Checks

```powershell
python -m compileall src tests
python -m pytest
```
