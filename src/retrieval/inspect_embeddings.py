import numpy as np


def inspect():

    embeddings = np.load("data/sentence_embeddings.npy")

    print(f"Shape: {embeddings.shape}")
    print(f"Embedding dimension: {embeddings.shape[1]}")


if __name__ == "__main__":
    print("*" * 50)
    inspect()
    print("x" * 50)