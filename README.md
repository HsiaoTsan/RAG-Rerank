# Introduction
This repository contains the code for the QA system based on RAG and Reranking for the on-premise deployment of a QA system for the user manual of a traffic simulator named Aimsun. 

# News
- 2025-01-25: Proof of Concept (PoC) for the on-premise deployment of a QA system based on RAG on a minimal text data.

# Usage
Coming soon!

Code Architecture:
```
├── config/               # Configuration files
│   ├── settings.yaml     # Hyperparameters, paths, etc.
├── data/                 # Raw and processed data
│   ├── raw_documents/    # PDFs, text files, etc.
│   └── processed/        # Chunks, embeddings, etc.
├── src/
│   ├── ingestion/        # Data preprocessing and embedding
│   │   ├── chunking.py
│   │   ├── embedding.py
│   │   └── db_handler.py
│   ├── retrieval/        # Vector search logic
│   ├── generation/       # LLM integration
│   ├── evaluation/       # Metrics and testing
│   └── api/              # REST/gRPC endpoints
└── main.py               # Entry point for the pipeline
```