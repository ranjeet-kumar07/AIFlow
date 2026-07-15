from app.rag.document_loader import DocumentLoader
from app.rag.chunker import Chunker

documents = DocumentLoader.load_documents()

for document in documents:

    chunks = Chunker.split(document)

    print(document.title)

    for chunk in chunks:
        print(chunk)