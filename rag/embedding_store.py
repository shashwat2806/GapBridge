import json
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer

from rag.document_chunker import chunk_document
from config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

CHUNKS_PATH = Path("data/knowledge_base/nist_chunks.json")
EMBEDDINGS_PATH = Path("data/knowledge_base/nist_embeddings.npy")


def build_store(source_text):
    CHUNKS_PATH.parent.mkdir(parents=True, exist_ok=True)

    chunks = chunk_document(source_text)
    embeddings = model.encode(chunks)

    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f)
    np.save(EMBEDDINGS_PATH, embeddings)


def load_store():
    if not CHUNKS_PATH.exists() or not EMBEDDINGS_PATH.exists():
        raise FileNotFoundError("Knowledge base not built yet. Run build_knowledge_base.py first.")

    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    embeddings = np.load(EMBEDDINGS_PATH)
    return chunks, embeddings