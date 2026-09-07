import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage
from src.chains.rag_chain import answer_question
st.set_page_config(page_title="SupportPearlz",page_icon="💧");st.title("💧 SupportPearlz");st.caption("Evidence-grounded LangChain RAG customer support")
with st.sidebar:
 key=st.text_input("OpenAI API Key",type="password")
 st.markdown("""**Safety controls**
- persisted index
- relevance gate
- grounded sources
- injection resistance
- explicit refusal
""")
if "history" not in st.session_state: st.session_state.history=[]
for m in st.session_state.history:
 with st.chat_message("user" if isinstance(m,HumanMessage) else "assistant"):st.write(m.content)
q=st.chat_input("Ask a support question...")
if q:
 if not key: st.error("Enter your OpenAI API key.");st.stop()
 with st.chat_message("user"):st.write(q)
 try:
  with st.spinner("Retrieving evidence..."):r,meta=answer_question(q,st.session_state.history,key)
  with st.chat_message("assistant"):
   st.write(r.answer);st.caption("Confidence: "+r.confidence)
   if r.sources:
    st.markdown("**Sources**")
    for s in r.sources: st.write(f"• {s.source} — {s.location}")
  st.session_state.history += [HumanMessage(content=q),AIMessage(content=r.answer)]
 except Exception as e: st.error(f"Controlled error: {e}")
