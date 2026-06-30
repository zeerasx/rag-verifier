from datasets import load_dataset

from src.retrieval.retriever import Retriever

from src.evaluation.retrieval_metrics import (
    recall_at_k,
    hit_rate,
    mean_reciprocal_rank
)


class RetrievalEvaluator:

    def __init__(self):
        self.retriever = Retriever()

    def evaluate_sample(self,sample):

        question = sample["question"]
        relevant_titles = (sample["supporting_facts"]["title"])
        retrieved = (self.retriever.retrieve(question,top_k=5))

        

        retrieved_titles = [
            r.document_title
            for r in retrieved
        ]
        # For debugging
        print("Question:", question)
        print("Relevant titles:", relevant_titles)
        print("Retrieved titles:", retrieved_titles)

        return {
            "recall@5":recall_at_k(retrieved_titles,relevant_titles),
            "hit_rate":hit_rate(retrieved_titles,relevant_titles),
            "mrr":mean_reciprocal_rank(retrieved_titles,relevant_titles)
        }