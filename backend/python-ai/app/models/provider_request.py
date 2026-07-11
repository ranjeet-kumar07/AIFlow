from pydantic import BaseModel

from app.models.chat_message import ChatMessage


class ProviderRequest(BaseModel):
    """
    Internal request passed from the Gateway
    to an LLM Provider.

    This model is provider-independent.
    """

    model: str

    messages: list[ChatMessage]

    temperature: float

    max_tokens: int