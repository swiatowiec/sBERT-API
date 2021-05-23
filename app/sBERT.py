from sentence_transformers import SentenceTransformer
from .models import SentenceEmbedding

def get_embedding(sentences):
    model = SentenceTransformer('paraphrase-distilroberta-base-v1')
    embeddings = model.encode(sentences)
    result = []
    for sentence, embedding in zip(sentences, embeddings):
        result.append(SentenceEmbedding( sentence=sentence, embedding=embedding.tolist()))
    return result