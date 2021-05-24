from sentence_transformers import SentenceTransformer
from .models import SentenceEmbeddingOutput
from typing import List

def get_embedding(sentences: List[str]):
    """
    Get sentences embeddings using sBERT.
    """
    model = SentenceTransformer('paraphrase-distilroberta-base-v1')
    embeddings = model.encode(sentences)
    result = []
    for sentence, embedding in zip(sentences, embeddings):
        result.append(SentenceEmbeddingOutput( sentence=sentence, embedding=embedding.tolist()))
    return result