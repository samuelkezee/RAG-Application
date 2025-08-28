🧠 RAG Application (FAISS + OpenAI)
------------------------------------

A simple Retrieval-Augmented Generation (RAG) application built with:

Streamlit
 for the frontend

FAISS
 for vector search

OpenAI API
 (via Euron proxy) for embeddings & completions

This app allows you to ask questions, retrieves the most relevant chunks from a knowledge base, and generates AI-powered answers.

✨ Features
-------------------------------------

✅ Chunk large documents into smaller sections

✅ Store and search chunks using FAISS vector database

✅ Build prompts with retrieved context

✅ Generate answers using OpenAI completions API

✅ Simple Streamlit UI


⚙️ Installation
------------------------

Clone the repository

git clone <your-repo-url>
cd <your-repo-name>


Create a virtual environment & activate it

python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows


Install dependencies

pip install -r requirements.txt


Set up environment variables
Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

▶️ Usage
----------------

Run the Streamlit app:

streamlit run App.py

Example:

Enter query:

Who is the main character in the story?


The app will:

Retrieve relevant chunks from data/story.txt

Build a context-aware prompt

Generate an AI-powered answer

**📖 How It Works**
-------------------------------

Chunking → chunking.py splits documents into small text chunks.

Embeddings → embedding.py converts chunks & queries into vectors.

Vector Store → retrieval.py indexes embeddings with FAISS & retrieves top matches.

Prompting → prompt.py builds a context + query prompt.

Completion → completion.py queries OpenAI API and returns a response.

**🚀 Future Improvements**
------------------------------------------

Add support for multiple documents

Semantic-based text splitting (instead of word count)

Persistent FAISS index updates

Multi-turn chat with conversation memory
