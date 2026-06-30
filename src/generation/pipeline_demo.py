from src.generation.rag_pipeline import RAGPipeline

if __name__ == "__main__":
    pipeline = RAGPipeline()
    result = pipeline.answer("What is retrieval-augmented generation?", top_k=3)

    print("\n--------------------------------")
    print("Question:", result["question"])

    print("\n--------------------------------")
    print("Answer:", result["answer"])
