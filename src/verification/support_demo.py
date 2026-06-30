from src.verification.support_score import SupportScorer

contexts = [
    "Google developed BERT.",
    "BERT was introduced in 2018."
]

answer = "Google developed BERT."
scorer = SupportScorer()
score = scorer.compute(contexts, answer)

print(f"Support Score: {score}")