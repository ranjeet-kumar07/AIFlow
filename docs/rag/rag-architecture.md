# AIFlow RAG Architecture

## Goal

Enable AIFlow to answer questions using external knowledge instead of relying only on the LLM's training data.

## Components

- Document Loader
- Chunker
- Embedding Provider
- Vector Store
- Retriever
- Prompt Manager

## Flow

Documents
    ↓
Chunks
    ↓
Embeddings
    ↓
Vector Store
    ↓
Similarity Search
    ↓
Relevant Context
    ↓
Prompt
    ↓
LLM