import json

import numpy as np

from src.retrieval.embedder import SentenceEmbedder
from src.retrieval.faiss_index import FaissIndex


CORPUS_FILE = ("data/sentence_corpus.jsonl")


class Retriever:

    def __init__(self):
        self.embedder = (SentenceEmbedder())

        self.index = FaissIndex()

        self.index.load()

        self.records = []

        with open(
            CORPUS_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:
                self.records.append(json.loads(line))

    def retrieve(self,query,top_k=5):

        query_embedding = (self.embedder.encode([query]))

        distances, indices = (self.index.search(query_embedding,top_k))

        results = []
        for idx in indices[0]:
            results.append(self.records[idx])

        return results