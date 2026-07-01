from src.diagnosis.failure_classifier import FailureClassifier

classifier = FailureClassifier()

print(
    classifier.classify(
        retrieval_hit=False,
        support_score=0.0
    )
)

print(
    classifier.classify(
        retrieval_hit=True,
        support_score=0.2
    )
)

print(
    classifier.classify(
        retrieval_hit=True,
        support_score=0.8
    )
)