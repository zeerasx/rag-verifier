def build_rag_prompt(question,contexts):

    context_block = "\n\n".join(contexts)

    prompt = f"""
        You are a question answering assistant.Answer the question using only the provided context.
        If the answer cannot be found in the context, say: "I cannot determine the answer from the provided context."
        Context:
        {context_block}
        Question:
        {question}
        Answer:
        """

    return prompt