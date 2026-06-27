from pprint import pprint

from src.ingestion.dataset_loader import load_hotpotqa

def inspect_example(index: int = 0):

    dataset = load_hotpotqa()
    sample = dataset[index]

    print("\nQUESTION")
    print("-" * 50)
    print(sample["question"])

    print("\nANSWER")
    print("-" * 50)
    print(sample["answer"])

    print("\nTYPE")
    print("-" * 50)
    print(sample["type"])

    print("\nSUPPORTING FACTS")
    print("-" * 50)

    pprint(sample["supporting_facts"])


if __name__ == "__main__":
    inspect_example()