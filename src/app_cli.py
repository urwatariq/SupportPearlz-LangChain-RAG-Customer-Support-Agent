from langchain_core.messages import HumanMessage,AIMessage
from src.config import settings
from src.chains.rag_chain import answer_question
h=[]
while True:
 q=input("You > ")
 if q.lower() in {"exit","quit"}:break
 r,_=answer_question(q,h,settings.openai_api_key);print("Bot >",r.answer);print("Sources:",[f"{s.source} — {s.location}" for s in r.sources]);h += [HumanMessage(content=q),AIMessage(content=r.answer)]
