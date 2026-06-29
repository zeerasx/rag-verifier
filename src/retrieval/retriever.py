import json

import numpy as np

from src.retrieval.embedder import SentenceEmbedder
from src.retrieval.faiss_index import FaissIndex
from src.retrieval.retrieval_result import RetrievalResult

CORPUS_FILE = ("data/sentence_corpus.jsonl")


class Retriever:

    def __init__(self):
        self.embedder = (SentenceEmbedder())

        self.index = FaissIndex()

        self.index.load()

        self.records = []

        with open(CORPUS_FILE,"r",encoding="utf-8") as f:
            for line in f:
                self.records.append(json.loads(line))

    def retrieve(self,query,top_k=5):

        query_embedding = (self.embedder.encode([query]))

        distances, indices = (self.index.search(query_embedding,top_k))

        results = []
        seen_titles = set()
        for rank, (idx, distance) in enumerate(
            zip(indices[0], distances[0]),
            start=1
        ):

            record = self.records[idx]
            title = record["document_title"]
            if title in seen_titles:
                continue

            seen_titles.add(title)
            results.append(
                RetrievalResult(
                    rank = len(results) + 1,
                    score = float(distance),
                    document_title = title,
                    sentence_id = record["sentence_id"],
                    text = record["text"]
                )
            )

            if len(results) >= top_k:
                break

            # result = RetrievalResult(
            #     rank=rank,
            #     score=float(distance),
            #     document_title=record["document_title"],
            #     sentence_id=record["sentence_id"],
            #     text=record["text"]
            # )

            # results.append(result)

        return results