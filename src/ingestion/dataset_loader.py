from datasets import load_dataset

# Load dataset - HotpotQA.
def load_hotpotqa(split: str = "validation"):
    dataset = load_dataset(
        "hotpotqa/hotpot_qa",
        "fullwiki",
        split=split
    )
    return dataset


if __name__ == "__main__":
    dataset = load_hotpotqa()
    print(f"Dataset size: {len(dataset)}")
    print("\nAvailable fields:")
    print(dataset.column_names)