import requests

from app.config.settings import settings
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def generate_response(
        self,
        request: ChatRequest
    ) -> ChatResponse:

        payload = {
            "model": request.model,
            "messages": [
                message.model_dump()
                for message in request.messages
            ],
            "stream": False
        }

        response = requests.post(
            f"{settings.OLLAMA_BASE_URL}/api/chat",
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        prompt_tokens = data.get("prompt_eval_count", 0)
        completion_tokens = data.get("eval_count", 0)

        return ChatResponse(
            model=data.get("model", request.model),
            content=data["message"]["content"],
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
            finish_reason="stop"
        )