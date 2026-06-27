from pathlib import Path
from datasets import load_dataset
from src.ingestion.dataset_loader import load_hotpotqa

# create a directory to store the output file
OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "hotpotqa_subset.json"

def create_subset(
    sample_size: int = 200,
    split: str = "validation",
    seed: int = 42,
):
    dataset = load_hotpotqa(split=split)

    subset = dataset.shuffle(seed=seed).select(
        range(sample_size)
    )

    subset.to_json(str(OUTPUT_FILE))
    print(f"Saved {sample_size} samples to {OUTPUT_FILE}")


if __name__ == "__main__":
    create_subset()