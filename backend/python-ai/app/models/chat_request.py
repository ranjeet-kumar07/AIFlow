from pydantic import BaseModel, Field


class Message(BaseModel):
    role: str = Field(
        ...,
        description="Role of the sender (system, user, assistant)"
    )

    content: str = Field(
        ...,
        description="Message content"
    )


class ChatRequest(BaseModel):
    model: str = Field(
        ...,
        description="Target LLM model"
    )

    messages: list[Message]

    temperature: float = Field(
        default=0.2,
        ge=0,
        le=2
    )

    max_tokens: int = Field(
        default=512,
        gt=0
    )