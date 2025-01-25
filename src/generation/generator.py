from openai import OpenAI

system_prompt = (
            "You are a helpful assistant. "
            "Use the provided context to answer the question. "
            "If the context does not have the answer, say you don't know."
        )

class AnswerGenerator:
    def __init__(self, api_key, model_name="gpt-4o-mini", base_url="https://api.openai.com/v1"):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model_name = model_name

    def generate(self, query, context):
        prompt = f"Answer based on context:\n{context}\n\nQuestion: {query}\nAnswer:"

        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content