import json

def inspect_corpus(
    path="data/sentence_corpus.jsonl",n=5):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        for i, line in enumerate(f):

            if i >= n:
                break

            record = json.loads(line)

            print("\n---------")
            print(f"Title: {record['document_title']}")
            print(f"Sentence: {record['text']}")


if __name__ == "__main__":
    print("*" * 50)
    inspect_corpus()
    print("x" * 50)