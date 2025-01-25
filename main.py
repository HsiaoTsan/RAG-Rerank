import os
from config import llm_config
from src.ingestion.doc_loader import load_documents
from src.ingestion.chunking import chunk_document
from src.ingestion.db_handler import VectorDB
from src.ingestion.embedding import Embedder
from src.retrieval.retriever import Retriever
from src.generation.generator import AnswerGenerator


def main(query: str, llm: str = 'DeepSeek'):
    # 1. Ingest documents (preprocess once)
    text = load_documents("data/raw_documents/")
    chunks = chunk_document(text)

    # 2. Embed and index
    embedder = Embedder()
    embeddings = embedder.embed(chunks)
    vector_db = VectorDB()
    vector_db.add_embeddings(embeddings)

    # 3. Retrieve and generate
    retriever = Retriever(vector_db, chunks)
    query_embedding = embedder.embed([query])[0]
    context = retriever.get_relevant_chunks(query_embedding)

    generator = AnswerGenerator(**llm_config[llm])
    answer = generator.generate(query, context)
    return answer


if __name__ == "__main__":
    query = "How to generate text with REST API?"
    print(main(query))