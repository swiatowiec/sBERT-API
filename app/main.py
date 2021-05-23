from fastapi import FastAPI
from .sBERT import get_embedding
from .models import SentenceEmbedding
from typing import List


app = FastAPI()

@app.post("/sentences_transformator", response_model=List[SentenceEmbedding])
async def create_item(sentences: List[str]):
    embeddings = get_embedding(sentences)
    return embeddings


