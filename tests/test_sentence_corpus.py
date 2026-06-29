from pathlib import Path


def test_sentence_corpus_exists():

    corpus = Path("data/sentence_corpus.jsonl")
    assert corpus.exists()


def test_sentence_corpus_not_empty():

    corpus = Path("data/sentence_corpus.jsonl")
    assert corpus.stat().st_size > 0