from pydantic import BaseModel

class SentenceEmbedding(BaseModel):
    sentence: str
    embedding: list=[]