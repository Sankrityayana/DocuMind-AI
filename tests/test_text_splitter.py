from documind_ai.models import LoadedDocument
from documind_ai.text_splitter import RecursiveTextChunker, normalize_whitespace


def test_normalize_whitespace_collapses_runs():
    assert normalize_whitespace("alpha\n\n beta\tgamma") == "alpha beta gamma"


def test_split_text_adds_overlap():
    chunker = RecursiveTextChunker(chunk_size=20, chunk_overlap=5)
    chunks = chunker.split_text("abcdefghijklmnopqrstuvwxyz")

    assert chunks == ["abcdefghijklmnopqrst", "pqrstuvwxyz"]


def test_split_documents_preserves_source_metadata(tmp_path):
    source = tmp_path / "note.md"
    document = LoadedDocument(source_path=source, text="DocuMind indexes documents.", metadata={"filename": "note.md"})
    chunker = RecursiveTextChunker(chunk_size=50, chunk_overlap=5)

    chunks = chunker.split_documents([document])

    assert len(chunks) == 1
    assert chunks[0].metadata["filename"] == "note.md"
    assert chunks[0].metadata["source"] == str(source)
