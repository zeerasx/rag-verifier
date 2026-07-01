from src.attribution.evidence_attribution import EvidenceAttribution

def test_attribution_returns_results():

    contexts = [
        "Google developed BERT.",
        "BERT was introduced in 2018."
    ]

    answer = "Google developed BERT."

    attributor = EvidenceAttribution()

    results = (attributor.attribute(contexts,answer))

    assert len(results) == 2