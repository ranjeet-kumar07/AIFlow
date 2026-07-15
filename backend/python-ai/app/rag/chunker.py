from app.models.chunk import Chunk
from app.models.document import Document


class Chunker:

    CHUNK_SIZE = 250

    @classmethod
    def split(
        cls,
        document: Document
    ) -> list[Chunk]:

        chunks = []

        content = document.content

        start = 0
        index = 0

        while start < len(content):

            end = start + cls.CHUNK_SIZE

            chunk_text = content[start:end]

            chunks.append(
                Chunk(
                    id=f"{document.id}-{index}",
                    document_id=document.id,
                    index=index,
                    content=chunk_text,
                    metadata=document.metadata
                )
            )

            start = end
            index += 1

        return chunks