from pathlib import Path

def test_subset_exists():
    subset_file = Path("data/hotpotqa_subset.json")
    assert subset_file.exists()


def test_processed_csv_exists():
    processed_file = Path("data/hotpotqa_processed.csv")
    assert processed_file.exists()


def test_processed_csv_not_empty():
    processed_file = Path("data/hotpotqa_processed.csv")
    assert processed_file.stat().st_size > 0