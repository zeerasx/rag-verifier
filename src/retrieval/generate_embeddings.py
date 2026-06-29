import json
from pathlib import Path

import numpy as np

from src.retrieval.embedder import SentenceEmbedder


CORPUS_FILE = Path("data/sentence_corpus.jsonl")
EMBEDDING_FILE = Path("data/sentence_embeddings.npy")

def load_sentences():

    texts = []
    with open(CORPUS_FILE,"r",encoding="utf-8") as f:

        for line in f:

            record = json.loads(line)
            texts.append(record["text"])

    return texts


def generate_embeddings():

    texts = load_sentences()

    print(f"Loaded {len(texts)} sentences")

    embedder = SentenceEmbedder()

    embeddings = embedder.encode(texts)

    np.save(EMBEDDING_FILE,embeddings)

    print(f"Saved embeddings to {EMBEDDING_FILE}")

    print(f"Shape: {embeddings.shape}")


if __name__ == "__main__":
    print("*" * 50)
    generate_embeddings()
    print("x" * 50)