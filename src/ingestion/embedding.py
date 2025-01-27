from openai import OpenAI
from config.llm_config import llm_config
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        if model_name == "ChatGPT":
            self.model = OpenAI(api_key=llm_config['ChatGPT']['api_key'],
                                base_url=llm_config['ChatGPT']['base_url'])
        else:
            self.model = SentenceTransformer(model_name)





    def embed(self, texts):
        if isinstance(self.model, OpenAI):
            return self.model.embeddings.create(
                            input="texts",
                            model="text-embedding-3-small"
                        ).data[0].embedding
        else:
            return self.model.encode(texts)

