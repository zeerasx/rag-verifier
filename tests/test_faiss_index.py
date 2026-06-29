from pathlib import Path

def test_faiss_index_exists():
    index_file = Path("data/faiss_index.bin")
    assert index_file.exists()


def test_faiss_index_not_empty():
    index_file = Path("data/faiss_index.bin")
    assert index_file.stat().st_size > 0