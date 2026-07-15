from pydantic import BaseModel,Field


class Document(BaseModel):

    id: str

    source: str

    title: str

    content: str

    metadata: dict = Field(
        default_factory=dict
    )