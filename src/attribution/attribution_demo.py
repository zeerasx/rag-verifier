from src.attribution.evidence_attribution import EvidenceAttribution

contexts = [
    "Google developed BERT.",
    "BERT was introduced in 2018.",
    "Paris is the capital of France."
]

answer = "Google developed BERT."

attributor = EvidenceAttribution()

results = (
    attributor.attribute(
        contexts,
        answer
    )
)

for result in results:
    print()
    print(result["score"])
    print(result["context"])