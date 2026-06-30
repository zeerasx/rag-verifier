from src.verification.support_score import SupportScorer


def test_empty_answer():
    scorer = SupportScorer()

    score = scorer.compute(
        contexts=["Google developed BERT."],
        answer=""
    )
    assert score == 0.0


def test_empty_context():

    scorer = SupportScorer()
    score = scorer.compute(
        contexts=[],
        answer="Google developed BERT."
    )
    assert score == 0.0