from fastapi import FastAPI
from .sBERT import get_embedding
from .models import SentenceEmbeddingOutput
from typing import List


app = FastAPI()

@app.post("/sentences_transformator", response_model=List[SentenceEmbeddingOutput])
def create_item(request: List[str]):
    """
    Create an item with the information:
    - **sentence**: a sentence to transform as string
    - **embedding**: a sentence embedding as list
    """
    embeddings = get_embedding(request)
    return embeddings