from langchain_core.messages import HumanMessage
def rewrite(q,h):
 if q.lower().split()[:1] in [["it"],["that"],["this"]] and h:
  last=next((m.content for m in reversed(h) if isinstance(m,HumanMessage)),"")
  return f"Previous topic: {last}. Follow-up: {q}"
 return q
