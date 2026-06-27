import json
from pathlib import Path

import pandas as pd

INPUT_FILE = Path("data/hotpotqa_subset.json")
OUTPUT_FILE = Path("data/hotpotqa_processed.csv")

def preprocess():

    rows = []
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            sample = json.loads(line)
            rows.append(
                {
                    "id": sample["id"],
                    "question": sample["question"],
                    "answer": sample["answer"],
                    "type": sample["type"],
                }
            )

    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_FILE,index=False)
    print(f"Saved processed dataset to {OUTPUT_FILE}")

    print(df.head())


if __name__ == "__main__":
    preprocess()