import shutil
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from src.config import settings
from src.ingestion.loaders import load_all
from src.ingestion.chunking import split_documents
def main():
 if not settings.openai_api_key: raise SystemExit("OPENAI_API_KEY required")
 docs,skipped=load_all(settings.knowledge_base_path)
 if len({d.metadata["source"] for d in docs})<10: raise SystemExit("Need 10+ documents")
 chunks=split_documents(docs)
 shutil.rmtree(settings.vector_store_path,ignore_errors=True);settings.vector_store_path.mkdir(parents=True)
 Chroma.from_documents(chunks,OpenAIEmbeddings(model=settings.embedding_model,api_key=settings.openai_api_key),persist_directory=str(settings.vector_store_path),collection_name="supportpearlz")
 print({"documents":len(docs),"chunks":len(chunks),"skipped":skipped})
if __name__=="__main__": main()
