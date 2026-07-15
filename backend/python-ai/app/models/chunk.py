from pydantic import BaseModel,Field


class Chunk(BaseModel):

    id: str

    document_id: str

    index: int

    content: str

    metadata: dict = Field(
        default_factory=dict
    )