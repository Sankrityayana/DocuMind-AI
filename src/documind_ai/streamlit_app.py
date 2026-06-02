from __future__ import annotations

from pathlib import Path

import streamlit as st

from documind_ai.config import settings
from documind_ai.rag import RagService, save_upload


st.set_page_config(page_title="DocuMind AI", page_icon="D", layout="wide")


@st.cache_resource
def get_rag_service() -> RagService:
    return RagService(settings)


rag_service = get_rag_service()

st.title("DocuMind AI")
st.caption("Chat with PDFs, knowledge bases, and datasets using semantic search plus LLM answers.")

with st.sidebar:
    st.header("Documents")
    uploads = st.file_uploader(
        "Upload PDF, text, Markdown, or CSV files",
        type=["pdf", "txt", "md", "markdown", "csv"],
        accept_multiple_files=True,
    )
    if st.button("Ingest documents", type="primary", disabled=not uploads):
        saved_paths: list[Path] = []
        for upload in uploads or []:
            saved_paths.append(save_upload(upload.name, upload.getvalue(), settings.upload_dir))
        response = rag_service.ingest_paths(saved_paths)
        st.success(f"Indexed {response.chunks_added} chunks from {len(response.files)} file(s).")

    st.divider()
    st.metric("Indexed chunks", rag_service.document_count())
    llm_mode = "enabled" if rag_service.answer_generator.llm_enabled else "local extractive fallback"
    st.write("LLM generation:", llm_mode)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sources"):
            with st.expander("Sources"):
                for source in message["sources"]:
                    st.write(f"**{source['source']}** - score {source['score']}")
                    st.caption(source["preview"])

question = st.chat_input("Ask a question about your indexed documents")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Retrieving relevant context..."):
            response = rag_service.ask(question)
        st.markdown(response.answer)
        if response.sources:
            with st.expander("Sources"):
                for source in response.sources:
                    st.write(f"**{source.source}** - score {source.score}")
                    st.caption(source.preview)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.answer,
            "sources": [source.model_dump() for source in response.sources],
        }
    )
