from openai import OpenAI

from app.config.settings import settings


class OpenAIClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def chat(
        self,
        model: str,
        messages: list[dict],
        temperature: float,
        max_tokens: int,
    ):

        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return response