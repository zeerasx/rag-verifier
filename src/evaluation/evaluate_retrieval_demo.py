from datasets import load_dataset

from src.ingestion.dataset_loader import load_hotpotqa
from src.evaluation.retrieval_evaluator import RetrievalEvaluator

dataset = load_hotpotqa()
# dataset = load_dataset(
#     "hotpot_qa",
#     "fullwiki",
#     split="validation"
# )

sample = dataset[0]

evaluator = RetrievalEvaluator()

results = evaluator.evaluate_sample(sample)



print(results)