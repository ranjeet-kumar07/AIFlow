import time

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.models.provider_request import ProviderRequest
from app.prompt.prompt_manager import PromptManager
from app.providers.provider_factory import ProviderFactory
from app.services.observability_service import ObservabilityService
from app.tools.tool_executor import ToolExecutor
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
            request.prompt,
            request.variables
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

        # First LLM call
        provider_response = provider.generate_response(
            provider_request
        )

        # Tool execution path
        if provider_response.tool_call:

            ObservabilityService.tool_execution_started(
                provider_response.tool_call.tool_name
            )

            tool_result = ToolExecutor.execute(
                provider_response.tool_call
            )

            ObservabilityService.tool_execution_completed(
                provider_response.tool_call.tool_name,
                tool_result.result
            )

            # Add tool result to conversation
            messages = PromptManager.append_tool_result(
                messages,
                provider_response.tool_call.tool_name,
                tool_result.result
            )

            # Create second provider request
            provider_request = ProviderRequest(
                model=request.model,
                messages=messages,
                temperature=request.temperature,
                max_tokens=request.max_tokens
            )

            ObservabilityService.tool_result_sent_back(
                provider_response.tool_call.tool_name
            )

            # Second LLM call
            provider_response = provider.generate_response(
                provider_request
            )

        # Final response (normal path or after tool execution)
        response = provider_response.chat_response

        latency = (
            time.perf_counter() - start
        ) * 1000

        ObservabilityService.llm_completed(
            response,
            latency
        )

        ObservabilityService.request_completed()

        return response