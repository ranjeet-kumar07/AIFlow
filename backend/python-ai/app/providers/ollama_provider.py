from app.clients.ollama_client import OllamaClient

from app.config.settings import settings
from app.models.provider_request import ProviderRequest
from app.models.chat_response import ChatResponse
from app.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def generate_response(
        self,
       request: ProviderRequest
    ) -> ChatResponse:

        payload = {
            "model": request.model,
            "messages": [
                message.model_dump()
                for message in request.messages
            ],
            "stream": False
        }

        client = OllamaClient()

        data = client.chat(payload)

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