from pydantic import BaseModel
from typing import Literal
class SourceRef(BaseModel): source:str;location:str;chunk_id:str
class GroundedResponse(BaseModel): answer:str;sources:list[SourceRef]=[];confidence:Literal["high","partial","none"];answered:bool;refusal:bool=False
