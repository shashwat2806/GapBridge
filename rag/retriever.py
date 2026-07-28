import numpy as np
from sentence_transformers import SentenceTransformer

from rag.embedding_store import load_store
from config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
def retrieve_context(query_text, top_k=3):
    chunks, embeddings = load_store()
    query_embedding = model.encode(query_text)

    scores = [cosine_similarity(query_embedding, emb) for emb in embeddings]
    ranked = sorted(zip(chunks, scores), key=lambda x: x[1], reverse=True)
    return [chunk for chunk, score in ranked[:top_k]]