from pydantic import BaseModel, Field
from app.models.chat_message import ChatMessage


class ChatRequest(BaseModel):

    model: str = Field(
        ...,
        description="Target LLM model"
    )

    messages: list[ChatMessage]

    temperature: float = Field(
        default=0.2,
        ge=0,
        le=2
    )

    max_tokens: int = Field(
        default=512,
        gt=0
    )