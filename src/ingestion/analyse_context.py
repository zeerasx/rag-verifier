from datasets import load_dataset

from src.ingestion.dataset_loader import load_hotpotqa

def inspect_context(index: int = 0):
    dataset = load_hotpotqa(split="validation")
    sample = dataset[index]

    print("\nQUESTION")
    print("-" * 50)
    print(sample["question"])

    print("\nANSWER")
    print("-" * 50)
    print(sample["answer"])

    print("\nCONTEXT OVERVIEW")
    print("-" * 50)

    context_titles = sample["context"]["title"]

    print(f"Number of documents: {len(context_titles)}" )

    print("-" * 50)
    print("\nDocument titles:")
    print("-" * 25)
    for title in context_titles[:5]:
        print(title)

    print("-" * 50)
    print("\nSUPPORTING FACTS")
    print("-" * 25)
    print(sample["supporting_facts"])
    print("-" * 50)

if __name__ == "__main__":
    inspect_context()