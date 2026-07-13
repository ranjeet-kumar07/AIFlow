from app.models.chat_message import ChatMessage
from app.prompt.prompt_repository import PromptRepository
from app.services.observability_service import ObservabilityService
from app.template.template_renderer import TemplateRenderer
from app.template.template_validator import TemplateValidator


class PromptManager:

    @staticmethod
    def build_messages(
        workflow: str,
        user_prompt: str,
        variables: dict[str, str]
    ) -> list[ChatMessage]:

        system_prompt = PromptRepository.load(
            workflow,
            "system.txt"
        )

        ObservabilityService.prompt_loaded(
            workflow,
            "system.txt"
        )

        chat_template = PromptRepository.load(
            workflow,
            "chat.txt"
        )

        ObservabilityService.prompt_loaded(
            workflow,
            "chat.txt"
        )

        render_variables = dict(variables)
        render_variables["user_prompt"] = user_prompt

        TemplateValidator.validate(
            chat_template,
            render_variables
        )

        user_message = TemplateRenderer.render(
            chat_template,
            render_variables
        )

        return [
            ChatMessage(
                role="system",
                content=system_prompt.strip()
            ),
            ChatMessage(
                role="user",
                content=user_message
            )
        ]

    @staticmethod
    def append_tool_result(
        messages: list[ChatMessage],
        tool_name: str,
        result: str
    ) -> list[ChatMessage]:

        updated_messages = list(messages)

        updated_messages.append(
            ChatMessage(
                role="assistant",
                content=f"Tool Requested: {tool_name}"
            )
        )

        updated_messages.append(
            ChatMessage(
                role="tool",
                content=result
            )
        )

        return updated_messages