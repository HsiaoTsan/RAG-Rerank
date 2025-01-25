class Retriever:
    def __init__(self, vector_db, text_store):
        self.vector_db = vector_db
        self.text_store = text_store  # Maps indices to text chunks

    def get_relevant_chunks(self, query_embedding, k=5):
        indices = self.vector_db.search(query_embedding, k)
        return [self.text_store[i] for i in indices]