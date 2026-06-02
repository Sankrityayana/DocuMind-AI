# User Guide

DocuMind AI helps you chat with private documents.

## Streamlit Workflow

1. Start the app:

   ```powershell
   streamlit run src/documind_ai/streamlit_app.py
   ```

2. Upload one or more documents in the sidebar.
3. Click `Ingest documents`.
4. Ask a question in the chat box.
5. Expand `Sources` under an answer to inspect retrieved evidence.

## Good Questions

Ask specific questions grounded in uploaded files:

- What is the refund policy?
- Summarize the onboarding steps.
- Which dataset row mentions delayed delivery?
- What assumptions are listed in the project plan?

## Weak Questions

Avoid questions that require information outside uploaded documents unless you
expect the answer to say there is not enough evidence:

- What happened in today's news?
- What is the best product on the market?
- What should I invest in?

## Source Scores

Scores are approximate similarity values derived from vector search. Higher
scores generally mean the chunk is more relevant, but always read the preview
when accuracy matters.

## Privacy

Files remain in your local `storage/uploads` folder. If `OPENAI_API_KEY` is set,
retrieved context is sent to OpenAI for answer generation. Without an API key,
answers are generated locally from retrieved excerpts.
