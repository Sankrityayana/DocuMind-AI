from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None or value == "":
        return default
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer, got {value!r}") from exc


@dataclass(frozen=True)
class Settings:
    chroma_dir: Path = Path(os.getenv("DOCUMIND_CHROMA_DIR", "./storage/chroma"))
    collection_name: str = os.getenv("DOCUMIND_COLLECTION", "documind_documents")
    upload_dir: Path = Path(os.getenv("DOCUMIND_UPLOAD_DIR", "./storage/uploads"))
    chunk_size: int = _int_env("DOCUMIND_CHUNK_SIZE", 900)
    chunk_overlap: int = _int_env("DOCUMIND_CHUNK_OVERLAP", 150)
    top_k: int = _int_env("DOCUMIND_TOP_K", 5)
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY") or None
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def ensure_directories(self) -> None:
        self.chroma_dir.mkdir(parents=True, exist_ok=True)
        self.upload_dir.mkdir(parents=True, exist_ok=True)


settings = Settings()
