from sentence_transformers import SentenceTransformer
import numpy as np


MODEL_NAME = "all-MiniLM-L6-v2"
THRESHOLD = 0.45

model = SentenceTransformer(MODEL_NAME)


def cosine_similarity(vec1, vec2) -> float:
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

def chunk_policy(text: str, chunk_size: int = 100) -> list:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def detect_gaps(policy_text: str, controls: list) -> list:
    results = []

    chunks = chunk_policy(policy_text)
    chunk_embeddings = model.encode(chunks)

    control_texts = [c["description"] for c in controls]
    control_embeddings = model.encode(control_texts)

    for control, control_embedding in zip(controls, control_embeddings):
        chunk_scores = [
            cosine_similarity(chunk_emb, control_embedding)
            for chunk_emb in chunk_embeddings
        ]
        best_score = max(chunk_scores) if chunk_scores else 0.0
        gap_found = best_score < THRESHOLD

        results.append({
            "id": control["id"],
            "function": control["function"],
            "description": control["description"],
            "related_policies": control.get("related_policies", []),
            "score": round(float(best_score), 2),
            "gap_found": gap_found
        })

    return results