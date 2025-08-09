import streamlit as st
from utils.embedding import generate_embeddings
from utils.chunking import chunk_text
from utils.retrieval import load_faiss_index, retrieve_chunks
from utils.prompt import build_prompt
from utils.completion import generate_completion

st.title("RAG Application")
st.write("This is a simple RAG application using FAISS and OpenAI embeddings.")

query = st.text_input("Enter your query:")
if query:
    index, chunks_mapping=load_faiss_index()
    top_chunks= retrieve_chunks(query, index, chunks_mapping, k=5)
    prompt= build_prompt(query, top_chunks)
    response= generate_completion(prompt)

    st.subheader("Anwser:")
    st.write(response)

    with st.expander("see the context used to answer the question"):
        for chunk in top_chunks:
            st.markdown(f"-{chunk}")



