from transformers import pipeline



class AttributionVerifier:
    def __init__(self, model_name="facebook/bart-large-mnli"):
        # Use MNLI-trained model for NLI
        self.classifier = pipeline("text-classification", model=model_name)

    def verify(self, context, answer):
        if not answer or not context:
            return {"label": "unsupported", "score": 0.0}

        # Concatenate premise (context) and hypothesis (answer)
        text = f"{context} </s> {answer}"
        result = self.classifier(text)[0]

        return {
            "label": result["label"],   # ENTAILMENT / CONTRADICTION / NEUTRAL
            "score": round(float(result["score"]),2)
        }