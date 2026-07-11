from pydantic import BaseModel, Field


class ChatResponse(BaseModel):
    model: str = Field(
        ...,
        description="Model that generated the response"
    )

    content: str = Field(
        ...,
        description="Generated text"
    )

    prompt_tokens: int = Field(
        default=0
    )

    completion_tokens: int = Field(
        default=0
    )

    total_tokens: int = Field(
        default=0
    )

    finish_reason: str = Field(
        default="stop"
    )