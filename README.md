  
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