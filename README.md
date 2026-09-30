# University RAG AI Assistant

A Retrieval-Augmented Generation (RAG) application that answers university-related questions using a custom knowledge base.

## Features

- University document loading
- Text chunking
- Hugging Face embeddings
- Chroma vector database
- Semantic retrieval
- Groq LLM integration
- FastAPI backend
- Streamlit frontend
- Source document display
- Handles questions outside the knowledge base

## Architecture
User → Streamlit → FastAPI → Retriever → Chroma → Groq LLM → Answer + Sources

## Technologies

- Python
- LangChain
- Hugging Face
- ChromaDB
- Groq
- FastAPI
- Streamlit

## Project Structure

```text
university-rag/
├── documents/
│   ├── admission.txt
│   ├── fees.txt
│   ├── courses.txt
│   └── scholarship.txt
├── ragservice.py
├── api.py
├── app.py
├── README.md
└── .gitignore

**How It Works 
University documents are loaded from the documents folder.
Documents are split into smaller chunks.
Each chunk is converted into an embedding.
Embeddings are stored in ChromaDB.
The retriever finds relevant chunks for a user question.
The retrieved context is sent to the Groq LLM.
The generated answer and source documents are returned.
FastAPI provides the backend API.
Streamlit provides the user interface.
