from .reranker import Reranker

class Retriever:
    def __init__(self, vector_db, text_store, reranker=None):
        self.vector_db = vector_db
        self.text_store = text_store  # Maps indices to text chunks
        self.reranker = reranker

    def get_relevant_chunks(self, query_embedding, k=5, query=None, rerank_top_k=100):
        # Step 1: Initial retrieval
        indices = self.vector_db.search(query_embedding, rerank_top_k)
        return [self.text_store[i] for i in indices]

        # Step 2: Reranking if a reranker is provided
        if self.reranker and query:
            chunks = self.reranker.rerank(query, chunks, top_k=k)
        else:
            chunks = chunks[:k]  # Fallback to top-k

        return chunks