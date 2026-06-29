from src.retrieval.retriever import Retriever

def main():

    retriever = Retriever()

    query = input("Enter query: ")

    results = retriever.retrieve(query=query,top_k=5)

    print("\nResults")

    for result in results:
        print(f"\nRank: {result.rank}")
        print(f"Score: {result.score:.4f}")
        print(f"Title: {result.document_title}")
        print(f"Text: {result.text}")

if __name__ == "__main__":
    print("*" * 50)
    main()
    print("x" * 50)