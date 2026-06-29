from pathlib import Path

import faiss
import numpy as np

INDEX_FILE = Path("data/faiss_index.bin")

class FaissIndex:

    def __init__(self):
        self.index = None

    def build(self, embeddings):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings.astype("float32"))

    def save(self):
        faiss.write_index(self.index,str(INDEX_FILE))

    def load(self):
        self.index = faiss.read_index(str(INDEX_FILE))

    def search(self,query_embedding,top_k=5):

        distances, indices = self.index.search(
            query_embedding.astype("float32"),
            top_k
        )

        return distances, indices