This repository contains the code and dataset for the **Question Answering (QA) system**. The system leverages a Retrieval-Augmented Generation (RAG) and Reranking framework paired with LLMs to generate answers to medical queries, tailoring responses based on the level of risk associated with each query. It is designed to be relevant for both research and real-world applications.

Code Architecture:

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