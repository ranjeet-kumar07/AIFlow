import time

from app.gateway.provider_factory import ProviderFactory
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.services.observability_service import ObservabilityService


class LLMGateway:

    def generate_response(
        self,
        request: ChatRequest
    ) -> ChatResponse:

        ObservabilityService.request_started(request)

        start = time.perf_counter()

        provider = ProviderFactory.get_provider(
            request.model
        )

        ObservabilityService.provider_selected(
            provider.__class__.__name__
        )

        response = provider.generate_response(request)

        latency = (
            time.perf_counter() - start
        ) * 1000

        ObservabilityService.llm_completed(
            response,
            latency
        )

        ObservabilityService.request_completed()

        return response