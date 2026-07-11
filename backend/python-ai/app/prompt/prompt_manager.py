from app.models.chat_message import ChatMessage
from app.prompt.system_prompt import DEFAULT_SYSTEM_PROMPT


class PromptManager:

    @staticmethod
    def build_messages(user_prompt: str) -> list[ChatMessage]:

        return [
            ChatMessage(
                role="system",
                content=DEFAULT_SYSTEM_PROMPT.strip()
            ),
            ChatMessage(
                role="user",
                content=user_prompt
            )
        ]