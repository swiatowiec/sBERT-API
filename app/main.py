from fastapi import FastAPI
from .sBERT import get_embedding
from .models import SentenceEmbeddingOutput
from typing import List


app = FastAPI()

@app.post("/sentences_transformator", response_model=List[SentenceEmbeddingOutput])
def sentences_transformator(request: List[str]):
    """
    Transform list of sentences to sBERT embedding and for each sentence return:
    - **sentence**: a transformed sentence as string
    - **embedding**: a sentence embedding as list
    """
    embeddings = get_embedding(request)
    return embeddings