from app.clients.ollama_client import OllamaClient
from app.models.provider_request import ProviderRequest
from app.models.chat_response import ChatResponse
from app.models.provider_response import ProviderResponse
from app.models.tool_call import ToolCall
from app.parsers.expression_parser import ExpressionParser
from app.providers.base_provider import BaseProvider
from app.services.observability_service import ObservabilityService


class OllamaProvider(BaseProvider):

    def generate_response(
        self,
        request: ProviderRequest
    ) -> ProviderResponse:

        last_message = request.messages[-1]

        # Simulated Tool Calling
        if (
            last_message.role == "user"
            and "calculate" in last_message.content.lower()
        ):

            expression = ExpressionParser.extract(
                last_message.content
            )

            ObservabilityService.expression_parsed(
                expression
            )

            ObservabilityService.tool_requested(
                "calculator"
            )

            return ProviderResponse(
                tool_call=ToolCall(
                    tool_name="calculator",
                    arguments={
                        "expression": expression
                    }
                )
            )

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

        chat_response = ChatResponse(
            model=data.get("model", request.model),
            content=data["message"]["content"],
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
            finish_reason="stop"
        )

        return ProviderResponse(
            chat_response=chat_response
        )