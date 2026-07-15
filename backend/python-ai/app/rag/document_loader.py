from pathlib import Path

from app.models.document import Document


class DocumentLoader:

    DOCUMENTS_PATH = Path(
        "knowledge/documents"
    )

    @classmethod
    def load_documents(
        cls
    ) -> list[Document]:

        documents = []

        for file in cls.DOCUMENTS_PATH.glob("*.txt"):

            content = file.read_text(
                encoding="utf-8"
            )

            documents.append(
                Document(
                    id=file.stem,
                    source=str(file),
                    title=file.stem,
                    content=content
                )
            )

        return documents