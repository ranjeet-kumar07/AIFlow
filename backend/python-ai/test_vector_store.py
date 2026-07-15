from app.rag.document_loader import DocumentLoader
from app.rag.chunker import Chunker
from app.rag.embedding_provider import EmbeddingProvider
from app.rag.vector_store import VectorStore

VectorStore.clear()

documents = DocumentLoader.load_documents()

for document in documents:

    chunks = Chunker.split(document)

    for chunk in chunks:

        embedding = EmbeddingProvider.embed(chunk)

        VectorStore.add(
            embedding
        )

print(len(VectorStore.all()))