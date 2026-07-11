from pydantic import BaseModel, Field


class ChatRequest(BaseModel):

    model: str = Field(
        ...,
        description="Target LLM model"
    )

    workflow: str = Field(
        default="general",
        description="AI workflow to execute"
    )

    prompt: str = Field(
        ...,
        min_length=1,
        description="User prompt"
    )

    temperature: float = Field(
        default=0.2,
        ge=0,
        le=2
    )

    max_tokens: int = Field(
        default=512,
        gt=0
    )