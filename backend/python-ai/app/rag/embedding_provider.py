import hashlib

from app.models.chunk import Chunk
from app.models.embedding import Embedding


class EmbeddingProvider:

    VECTOR_SIZE = 32

    @classmethod
    def embed(
        cls,
        chunk: Chunk
    ) -> Embedding:

        digest = hashlib.sha256(
            chunk.content.encode("utf-8")
        ).digest()

        vector = [
            value / 255.0
            for value in digest[:cls.VECTOR_SIZE]
        ]

        return Embedding(
            chunk=chunk,
            vector=vector
        )