from src.retrieval.retriever import Retriever
from src.generation.generator import Generator
from src.generation.prompts import build_rag_prompt


class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever()
        self.generator = Generator()

    def answer(self,question,top_k=5):

        retrieved = (self.retriever.retrieve(question,top_k))
        contexts = [
            r.text
            for r in retrieved
        ]

        prompt = build_rag_prompt(question,contexts)

        answer = (self.generator.generate(prompt))

        return {
            "question": question,
            "contexts": contexts,
            "answer": answer
        }