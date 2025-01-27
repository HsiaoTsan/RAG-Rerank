from sentence_transformers import CrossEncoder


class Reranker:
    def __init__(self, model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name, max_length=512)

    def rerank(self, query, chunks, top_k=5):
        # Format (query, chunk) pairs for cross-encoder
        pairs = [(query, chunk) for chunk in chunks]
        # Get similarity scores
        scores = self.model.predict(pairs)
        # Sort chunks by descending scores
        sorted_chunks = [chunk for _, chunk in sorted(zip(scores, chunks), reverse=True)]
        return sorted_chunks[:top_k]