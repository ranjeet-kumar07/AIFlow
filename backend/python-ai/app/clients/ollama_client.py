import requests

from app.config.settings import settings


class OllamaClient:

    def chat(self, payload: dict) -> dict:

        response = requests.post(
            f"{settings.OLLAMA_BASE_URL}/api/chat",
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        return response.json()