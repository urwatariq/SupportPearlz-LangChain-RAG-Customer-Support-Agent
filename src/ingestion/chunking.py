from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import settings
def split_documents(docs):
 out=RecursiveCharacterTextSplitter(chunk_size=settings.chunk_size,chunk_overlap=settings.chunk_overlap,add_start_index=True).split_documents(docs)
 for i,d in enumerate(out): d.metadata["chunk_id"]=f"C-{i:04d}"
 return out
