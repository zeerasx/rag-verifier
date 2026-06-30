def recall_at_k(retrieved_titles,relevant_titles,):

    relevant = set(relevant_titles)
    retrieved = set(retrieved_titles)
    if not relevant: 
        return 0.0

    hits = len(relevant.intersection(retrieved))

    return hits / len(relevant)


def hit_rate(retrieved_titles,relevant_titles):

    relevant = set(relevant_titles)
    retrieved = set(retrieved_titles)

    return int(len(relevant.intersection(retrieved)) > 0)


def mean_reciprocal_rank(retrieved_titles,relevant_titles):

    relevant = set(relevant_titles)

    for rank, title in enumerate(retrieved_titles,start=1):
        if title in relevant:
            return 1 / rank

    return 0.0