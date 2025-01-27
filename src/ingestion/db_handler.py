import faiss
import numpy as np
import json
import os
from src.ingestion.doc_loader import load_documents
from src.ingestion.document_manager import DocumentManager
from src.ingestion.chunking import chunk_document
from src.ingestion.embedding import Embedder

class VectorDB:
    def __init__(self,
                 dimension=384,
                 index_path="data/processed/faiss_index",
                 chunks_path="data/processed/chunks.json"):

        self.index_path = index_path
        self.chunks_path = chunks_path
        self.dimension = dimension

        # Load existing index/chunks or create new
        if os.path.exists(index_path) and os.path.exists(chunks_path):
            self.index = faiss.read_index(index_path)
            with open(chunks_path, "r") as f:
                self.chunks = json.load(f)
        else:
            self.index = faiss.IndexFlatL2(dimension)
            self.chunks = []

    def add_embeddings(self, chunks, embeddings):
        """Add new embeddings and chunks to the index"""
        self.index.add(np.array(embeddings).astype('float32'))
        self.chunks.extend(chunks)

    def save(self):
        """Persist index and chunks to disk"""
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)

        # Save FAISS index
        faiss.write_index(self.index, self.index_path)

        # Save chunks as JSON
        with open(self.chunks_path, "w") as f:
            json.dump(self.chunks, f, indent=2)

        print(f"Saved FAISS index to {self.index_path} and chunks to {self.chunks_path}")

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(np.array([query_embedding]).astype('float32'), k)
        return indices[0]


def load_vector_db() -> VectorDB:
    '''
    If the documents are not processed or they are changed, process them and store the embeddings in a VectorDB.
    Else, load the existing embeddings from the VectorDB.
    :return: instance of VectorDB
    '''


    raw_dir = "data/raw_documents"
    processed_dir = "data/processed"

    if DocumentManager.needs_processing(raw_dir, processed_dir):
        print("Processing documents...")

        # 1. Load and process documents
        text = load_documents(raw_dir)
        chunks = chunk_document(text)

        # 2. Create and store embeddings
        embedder = Embedder()
        embeddings = embedder.embed(chunks)

        vector_db = VectorDB()
        vector_db.add_embeddings(chunks, embeddings)
        vector_db.save()

        # 3. Save processing state
        DocumentManager.save_processing_state(raw_dir, processed_dir)
        print("Processed and saved new embeddings!")
    else:
        print("Loading existing embeddings...")
        vector_db = VectorDB()
        print("Loaded existing embeddings!")

    return vector_db
