from src.retrieval.retriever import Retriever


def run_demo():

    retriever = Retriever()

    query = ("Who developed BERT?")

    results = retriever.retrieve(query=query,top_k=5)

    print("\nQUERY")
    print("-" * 50)
    print(query)

    print("\nRESULTS")
    print("-" * 50)

    for i, result in enumerate(results,start=1):
        print(f"\n[{i}] {result['document_title']}")
        print(result["text"])


if __name__ == "__main__":
    run_demo()