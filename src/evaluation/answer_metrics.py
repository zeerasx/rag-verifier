import re


def normalize(text):
    text = text.lower()

    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )

    return text.strip()

def exact_match(prediction,reference):

    return int(
        normalize(prediction)
        ==
        normalize(reference)
    )


def f1_score(prediction,reference):

    pred_tokens = (normalize(prediction).split())
    ref_tokens = (normalize(reference).split())

    common = (
        set(pred_tokens)
        &
        set(ref_tokens)
    )

    if len(common) == 0:
        return 0

    precision = (
        len(common)
        / len(pred_tokens)
    )

    recall = (
        len(common)
        / len(ref_tokens)
    )

    return ((2 * precision * recall) 
            / (precision + recall))