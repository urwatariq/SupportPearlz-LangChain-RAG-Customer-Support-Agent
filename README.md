# SupportPearlz — LangChain RAG Customer Support Agent

## 🚀 Live App
### [Open SupportPearlz](PASTE_YOUR_STREAMLIT_LINK_HERE)

Evidence-grounded customer support using LangChain, persistent Chroma retrieval, conversation-aware query rewriting, relevance gating, structured responses and citations.

## Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python -m src.ingestion.build_index
streamlit run app.py
```

## Intentional gaps
Student discounts, NSF certification and instalment payments are intentionally not covered so refusal behaviour can be evaluated.
