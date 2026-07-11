from app.middleware.request_context import request_id
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.utils.logger import logger


class ObservabilityService:

    @staticmethod
    def request_started(request: ChatRequest):

        logger.info(
            f"[{request_id.get()}] "
            f"EVENT=RequestStarted "
            f"Model={request.model}"
        )

    @staticmethod
    def provider_selected(provider_name: str):

        logger.info(
            f"[{request_id.get()}] "
            f"EVENT=ProviderSelected "
            f"Provider={provider_name}"
        )

    @staticmethod
    def llm_completed(
        response: ChatResponse,
        latency_ms: float
    ):

        logger.info(
            f"[{request_id.get()}] "
            f"EVENT=LLMCompleted "
            f"Model={response.model} "
            f"PromptTokens={response.prompt_tokens} "
            f"CompletionTokens={response.completion_tokens} "
            f"TotalTokens={response.total_tokens} "
            f"Latency={latency_ms:.2f}ms "
            f"FinishReason={response.finish_reason}"
        )

    @staticmethod
    def request_completed():

        logger.info(
            f"[{request_id.get()}] "
            f"EVENT=RequestCompleted"
        )