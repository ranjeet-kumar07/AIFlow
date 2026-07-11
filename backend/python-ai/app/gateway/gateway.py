import time

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.models.provider_request import ProviderRequest
from app.prompt.prompt_manager import PromptManager
from app.providers.provider_factory import ProviderFactory
from app.services.observability_service import ObservabilityService
from app.workflow.workflow_resolver import WorkflowResolver


class LLMGateway:

    def generate_response(
        self,
        request: ChatRequest
    ) -> ChatResponse:

        ObservabilityService.request_started(request)

        start = time.perf_counter()

        # Resolve workflow
        workflow = WorkflowResolver.resolve(
            request
        )

        ObservabilityService.workflow_resolved(
            request.workflow
        )

        # Build AIFlow messages
        messages = PromptManager.build_messages(
            workflow["prompt_directory"],
            request.prompt
        )

        # Convert API request into internal provider request
        provider_request = ProviderRequest(
            model=request.model,
            messages=messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )

        provider = ProviderFactory.get_provider(
            request.model
        )

        ObservabilityService.provider_selected(
            provider.__class__.__name__,
            provider_request.model
        )

        response = provider.generate_response(
            provider_request
        )

        latency = (
            time.perf_counter() - start
        ) * 1000

        ObservabilityService.llm_completed(
            response,
            latency
        )

        ObservabilityService.request_completed()

        return response