from pydantic import BaseModel

from app.models.chunk import Chunk


class Embedding(BaseModel):

    chunk: Chunk

    vector: list[float]