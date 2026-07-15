from app.rag.document_loader import DocumentLoader
from app.rag.chunker import Chunker
from app.rag.embedding_provider import EmbeddingProvider

documents = DocumentLoader.load_documents()

for document in documents:

    chunks = Chunker.split(document)

    for chunk in chunks:

        embedding = EmbeddingProvider.embed(chunk)

        print(chunk.id)

        print(embedding.vector[:5])