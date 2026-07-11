from app.models.chat_message import ChatMessage
from app.prompt.prompt_repository import PromptRepository


class PromptManager:

    @staticmethod
    def build_messages(
        workflow: str,
        user_prompt: str
    ) -> list[ChatMessage]:

        system_prompt = PromptRepository.load(
            workflow,
            "system.txt"
        )

        chat_template = PromptRepository.load(
            workflow,
            "chat.txt"
        )

        user_message = chat_template.replace(
            "{{user_prompt}}",
            user_prompt
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