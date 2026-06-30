import re

def normalize(title):
    # Lowercase, remove parentheses content, strip spaces
    title = title.lower()
    title = re.sub(r"\(.*?\)", "", title)
    return title.strip()

def recall_at_k(retrieved_titles,relevant_titles,):

    # relevant = set(relevant_titles)
    relevant = {normalize(t) for t in relevant_titles}

    # retrieved = set(retrieved_titles)
    retrieved = {normalize(t) for t in retrieved_titles}
    if not relevant: 
        return 0.0

    hits = len(relevant.intersection(retrieved))

    return hits / len(relevant)


def hit_rate(retrieved_titles,relevant_titles):

    # relevant = set(relevant_titles)
    relevant = {normalize(t) for t in relevant_titles}

    # retrieved = set(retrieved_titles)
    retrieved = {normalize(t) for t in retrieved_titles}

    return int(len(relevant.intersection(retrieved)) > 0)


def mean_reciprocal_rank(retrieved_titles,relevant_titles):

    # relevant = set(relevant_titles)
    relevant = {normalize(t) for t in relevant_titles}
    retrieved = {normalize(t) for t in retrieved_titles}
    # for debugging:
    print("Normalized relevant:", [normalize(t) for t in relevant_titles])
    print("Normalized retrieved:", [normalize(t) for t in retrieved_titles])

    for rank, title in enumerate(retrieved,start=1):
        if title in relevant:
            return 1 / rank

    return 0.0