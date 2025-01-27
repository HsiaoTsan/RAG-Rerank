import argparse
from config.llm_config import llm_config
from src.ingestion.db_handler import load_vector_db
from src.ingestion.embedding import Embedder
from src.retrieval.retriever import Retriever, Reranker
from src.generation.generator import AnswerGenerator




def main(query: str, llm: str = 'DeepSeek'):
    # 1. Ingest documents into if they are not in Vector DB, else load Vector DB directly.
    vector_db = load_vector_db()

    # 2. Embed and index
    embedder = Embedder()

    # 3. Retrieve and generate
    reranker = Reranker()
    retriever = Retriever(vector_db, vector_db.chunks, reranker=reranker)
    query_embedding = embedder.embed([query])[0]
    context = retriever.get_relevant_chunks(query_embedding, query=query, k=5, rerank_top_k=100)

    generator = AnswerGenerator(**llm_config[llm])
    answer = generator.generate(query, context)
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='RAG+Rerank',
        description='Retrieve and generate answers using RAG+Rerank based on LLM',
        )

    parser.add_argument("--query", type=str, required=True)
    parser.add_argument("--llm", type=str, default="DeepSeek")
    args = parser.parse_args()

    query = args.query
    llm = args.llm

    print(main(query, llm))
