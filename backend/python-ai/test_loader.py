from app.rag.document_loader import DocumentLoader

documents = DocumentLoader.load_documents()

for document in documents:
    print(document)