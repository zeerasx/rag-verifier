# from src.verification.nli_verifier import NLIVerifier
from src.attribution.attribution_verifier import AttributionVerifier 
class EvidenceAttribution:

    def __init__(self):
        self.verifier = AttributionVerifier()

    def attribute(self,contexts,answer):
        attributions = []
        for idx, context in enumerate(
            contexts,
            start=1
        ):

            result = self.verifier.verify(context,answer)

            attributions.append(
                {
                    "context_id": idx,
                    "context": context,
                    "label": result["label"],
                    "score": result["score"]
                }
            )

        attributions.sort(key=lambda x: x["score"],reverse=True)
        return attributions