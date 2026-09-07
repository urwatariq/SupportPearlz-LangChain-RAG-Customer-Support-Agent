from pathlib import Path
from langchain_community.document_loaders import TextLoader,PyPDFLoader,Docx2txtLoader,CSVLoader
def load_file(p:Path):
 s=p.suffix.lower()
 if s in {".md",".txt"}: docs=TextLoader(str(p),encoding="utf-8").load()
 elif s==".pdf": docs=PyPDFLoader(str(p)).load()
 elif s==".docx": docs=Docx2txtLoader(str(p)).load()
 elif s==".csv": docs=CSVLoader(str(p)).load()
 else: raise ValueError("Unsupported file")
 for i,d in enumerate(docs):
  d.metadata.update({"source":p.name,"doc_type":"policy" if "policy" in p.name else ("faq" if "faq" in p.name else "guide"),"product_line":"AquaPearl","version":"2026-01","location":f"page {d.metadata.get('page',i)+1}"})
 return docs
def load_all(folder):
 docs=[];skipped=[]
 for p in folder.iterdir():
  if p.is_file():
   try: docs+=load_file(p)
   except Exception as e: skipped.append({"file":p.name,"error":str(e)})
 return docs,skipped
