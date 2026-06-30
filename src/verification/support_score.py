from src.verification.nli_verifier import NLIVerifier

class SupportScorer:
    def __init__(self):
        self.verifier = NLIVerifier()

    def compute(self, contexts, answer):

        scores = []
        for context in contexts:
            result = (self.verifier.verify(context, answer))

            if (result["label"]=="supported"):
                scores.append(result["score"])

        if len(scores) == 0:
            return 0.0

        return sum(scores) / len(scores)