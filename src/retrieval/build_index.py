from pathlib import Path

import numpy as np

from src.retrieval.faiss_index import FaissIndex


EMBEDDINGS_FILE = Path("data/sentence_embeddings.npy")


def build_index():
    embeddings = np.load(EMBEDDINGS_FILE)

    print(f"Loaded embeddings: {embeddings.shape}")

    index = FaissIndex()

    index.build(embeddings)

    index.save()

    print("FAISS index saved")


if __name__ == "__main__":
    print("*" * 50)
    build_index()
    print("x" * 50)