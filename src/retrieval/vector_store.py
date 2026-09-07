from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from src.config import settings
def load_store(key):
 if not key: raise ValueError("OpenAI API key required")
 if not settings.vector_store_path.exists() or not any(settings.vector_store_path.iterdir()): raise FileNotFoundError("Missing index. Run python -m src.ingestion.build_index")
 return Chroma(collection_name="supportpearlz",persist_directory=str(settings.vector_store_path),embedding_function=OpenAIEmbeddings(model=settings.embedding_model,api_key=key))
