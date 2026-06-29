from dataclasses import dataclass


@dataclass
class RetrievalResult:
    rank: int
    score: float
    document_title: str
    sentence_id: int
    text: str