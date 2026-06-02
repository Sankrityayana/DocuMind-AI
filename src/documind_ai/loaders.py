from __future__ import annotations

import csv
from pathlib import Path

from pypdf import PdfReader

from .models import LoadedDocument


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md", ".markdown", ".csv"}


def load_document(path: Path) -> LoadedDocument:
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        supported = ", ".join(sorted(SUPPORTED_EXTENSIONS))
        raise ValueError(f"Unsupported file type {suffix!r}. Supported: {supported}")

    if suffix == ".pdf":
        text = _load_pdf(path)
    elif suffix == ".csv":
        text = _load_csv(path)
    else:
        text = path.read_text(encoding="utf-8", errors="ignore")

    return LoadedDocument(
        source_path=path,
        text=text,
        metadata={"filename": path.name, "file_type": suffix.lstrip(".")},
    )


def load_documents(paths: list[Path]) -> list[LoadedDocument]:
    return [load_document(path) for path in paths]


def _load_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    pages: list[str] = []
    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        if page_text.strip():
            pages.append(f"[Page {page_number}]\n{page_text}")
    return "\n\n".join(pages)


def _load_csv(path: Path) -> str:
    rows: list[str] = []
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames:
            for row_number, row in enumerate(reader, start=1):
                values = [f"{key}: {value}" for key, value in row.items()]
                rows.append(f"Row {row_number}. " + "; ".join(values))
        else:
            handle.seek(0)
            raw_reader = csv.reader(handle)
            for row_number, row in enumerate(raw_reader, start=1):
                rows.append(f"Row {row_number}. " + "; ".join(row))
    return "\n".join(rows)
