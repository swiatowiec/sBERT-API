from pydantic import BaseModel

class SentenceEmbeddingOutput(BaseModel):
    sentence: str
    embedding: list=[]