from transformers import pipeline

class NLIVerifier:

    def __init__(
        self,
        model_name="MoritzLaurer/deberta-v3-base-zeroshot-v2.0"
    ):

        self.classifier = pipeline(
            "zero-shot-classification",
            model=model_name
        )

    def verify(self,context,answer):

        labels = ["supported","contradicted"]

        result = self.classifier(
            answer,
            candidate_labels=labels,
            hypothesis_template=
            "The context {} this statement."
        )

        return {
            "label":result["labels"][0],
            "score":float(result["scores"][0])
        }