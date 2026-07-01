from src.diagnosis.failure_classifier import FailureClassifier


def test_supported():
    classifier = FailureClassifier()

    result = classifier.classify(
        retrieval_hit=True,
        support_score=0.8
    )

    assert result == "supported"


def test_retrieval_failure():
    classifier = FailureClassifier()

    result = classifier.classify(
        retrieval_hit=False,
        support_score=0.0
    )

    assert result == "retrieval_failure"