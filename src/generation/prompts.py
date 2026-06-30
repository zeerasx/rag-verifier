def build_rag_prompt(question,contexts):

    # context_block = "\n\n".join(contexts)
    formatted_contexts = []

    for idx, context in enumerate(contexts,start=1):
        formatted_contexts.append(f"[Context {idx}]\n{context}")

    context_block = "\n\n".join(formatted_contexts)

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