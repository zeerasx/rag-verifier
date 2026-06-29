from pathlib import Path

def test_embedding_file_exists():

    path = Path("data/sentence_embeddings.npy")
    assert path.exists()


def test_embedding_file_not_empty():

    path = Path("data/sentence_embeddings.npy")
    assert path.stat().st_size > 0