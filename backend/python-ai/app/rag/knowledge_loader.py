from app.rag.chunker import Chunker
from app.rag.document_loader import DocumentLoader
from app.rag.embedding_provider import EmbeddingProvider
from app.rag.vector_store import VectorStore
from app.services.observability_service import ObservabilityService


class KnowledgeLoader:

    @staticmethod
    def initialize():

        VectorStore.clear()

        documents = DocumentLoader.load_documents()

        for document in documents:

            chunks = Chunker.split(
                document
            )

            for chunk in chunks:

                embedding = EmbeddingProvider.embed(
                    chunk
                )

                VectorStore.add(
                    embedding
                )

        ObservabilityService.info(
            f"Knowledge Base Loaded: {len(VectorStore.all())} embeddings"
        )