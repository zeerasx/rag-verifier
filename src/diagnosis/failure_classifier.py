class FailureClassifier:

    def classify(
        self,
        retrieval_hit,
        support_score,
        contradiction_score=0.0
    ):

        if not retrieval_hit:
            return "retrieval_failure"

        if contradiction_score > 0.5:
            return "context_conflict"

        if support_score < 0.3:
            return "hallucination"

        if support_score < 0.6:
            return "insufficient_evidence"

        return "supported"