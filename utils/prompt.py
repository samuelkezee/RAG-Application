def build_prompt(query,context_chunks):
    context= "\n\n".join(context_chunks)
    return f"""use contexte belowto answer the question.

context: {context}
question: {query}
answer:"""
#mutiline string is used here to format the prompt nicely