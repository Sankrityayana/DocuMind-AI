# Setup Guide

This guide explains how to run DocuMind AI locally.

## Prerequisites

- Python 3.10 or newer
- Git
- Optional OpenAI API key for generated answers

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configure

Copy the example environment file:

```powershell
Copy-Item .env.example .env
```

The app works without an LLM key. In that mode, it retrieves relevant chunks and
returns an extractive answer. To enable generated answers, set:

```text
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini
```

## Run Streamlit

```powershell
streamlit run src/documind_ai/streamlit_app.py
```

Use the sidebar to upload PDF, TXT, Markdown, or CSV files, then ask questions in
the chat input.

## Run FastAPI

```powershell
uvicorn documind_ai.api:app --reload --app-dir src
```

Visit:

```text
http://127.0.0.1:8000/docs
```

## Runtime Storage

The app writes local data to `storage/`:

- `storage/uploads`: files uploaded through Streamlit or FastAPI
- `storage/chroma`: persistent ChromaDB collection data

These runtime files are ignored by git.
