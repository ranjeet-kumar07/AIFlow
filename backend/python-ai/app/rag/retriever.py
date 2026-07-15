from app.models.chunk import Chunk
from app.models.document import Document
from app.rag.chunker import Chunker
from app.rag.embedding_provider import EmbeddingProvider
from app.rag.vector_store import VectorStore


class Retriever:

    @classmethod
    def retrieve(
        cls,
        question: str,
        top_k: int = 3
    ) -> list[Chunk]:

        query_document = Document(
            id="query",
            source="query",
            title="query",
            content=question
        )

        query_chunk = Chunker.split(
            query_document
        )[0]

        query_embedding = EmbeddingProvider.embed(
            query_chunk
        )

        results = VectorStore.search(
            query_embedding.vector,
            top_k
        )

        return [
            embedding.chunk
            for score, embedding in results
        ]