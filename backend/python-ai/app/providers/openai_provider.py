from app.clients.openai_client import OpenAIClient
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def generate_response(
        self,
        request: ChatRequest
    ) -> ChatResponse:

        client = OpenAIClient()

        response = client.chat(
            model=request.model,
            messages=[
                message.model_dump()
                for message in request.messages
            ],
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )

        choice = response.choices[0]

        usage = response.usage

        return ChatResponse(
            model=response.model,
            content=choice.message.content,
            prompt_tokens=usage.prompt_tokens,
            completion_tokens=usage.completion_tokens,
            total_tokens=usage.total_tokens,
            finish_reason=choice.finish_reason
        )