from app.models.embedding import Embedding
from app.rag.similarity import Similarity


class VectorStore:

    _embeddings: list[Embedding] = []

    @classmethod
    def add(
        cls,
        embedding: Embedding
    ):

        cls._embeddings.append(
            embedding
        )

    @classmethod
    def all(
        cls
    ) -> list[Embedding]:

        return cls._embeddings

    @classmethod
    def clear(
        cls
    ):

        cls._embeddings.clear()

    @classmethod
    def search(
        cls,
        query_vector: list[float],
        top_k: int = 3
    ):

        scored = []

        for embedding in cls._embeddings:

            score = Similarity.cosine(
                query_vector,
                embedding.vector
            )

            scored.append(
                (score, embedding)
            )

        scored.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return scored[:top_k]