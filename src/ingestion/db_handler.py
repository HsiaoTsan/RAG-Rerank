import faiss
import numpy as np

class VectorDB:
    def __init__(self, dimension=384):
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings):
        self.index.add(np.array(embeddings).astype('float32'))

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(np.array([query_embedding]).astype('float32'), k)
        return indices[0]