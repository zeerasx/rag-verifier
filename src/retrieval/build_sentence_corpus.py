
import json
from pathlib import Path

from datasets import load_dataset

from src.ingestion.dataset_loader import load_hotpotqa


OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "sentence_corpus.jsonl"

def build_sentence_corpus(
    split: str = "validation",
    sample_size: int = 200
):

    dataset = load_hotpotqa(split=split)

    dataset = dataset.select(range(sample_size))

    sentence_count = 0

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        for sample in dataset:
            question_id = sample["id"]

            titles = sample["context"]["title"]
            sentences = sample["context"]["sentences"]

            for doc_title, doc_sentences in zip(titles,sentences):

                for idx, sentence in enumerate(
                    doc_sentences
                ):

                    record = {
                        "question_id": question_id,
                        "document_title": doc_title,
                        "sentence_id": idx,
                        "text": sentence
                    }

                    f.write(
                        json.dumps(record)
                        + "\n"
                    )

                    sentence_count += 1
    
    print("\n------")
    print(f"Extracted {sentence_count} sentences")
    print(f"Saved corpus to {OUTPUT_FILE}")
    print("------")

if __name__ == "__main__":
    print("*" * 50)
    build_sentence_corpus()
    print("x" * 50)