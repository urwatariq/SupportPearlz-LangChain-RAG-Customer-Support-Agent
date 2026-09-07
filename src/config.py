from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
ROOT=Path(__file__).resolve().parents[1]
class Settings(BaseSettings):
 openai_api_key:str|None=None; chat_model:str="gpt-4o-mini"; embedding_model:str="text-embedding-3-small"; chunk_size:int=800; chunk_overlap:int=120; top_k:int=5; relevance_threshold:float=.35; temperature:float=0
 knowledge_base_path:Path=ROOT/"data/knowledge_base"; vector_store_path:Path=ROOT/"data/vector_store"
 model_config=SettingsConfigDict(env_file=ROOT/".env",extra="ignore")
settings=Settings()
