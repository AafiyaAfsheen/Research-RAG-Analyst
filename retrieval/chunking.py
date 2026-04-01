from langchain_text_splitters import RecursiveCharacterTextSplitter
from retrieval.config import CHUNK_SIZE, CHUNK_OVERLAP


def create_chunks(documents):
    """
    documents: list of dict
    [{ "text": "...", "metadata": {...}}]
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []

    for doc in documents:
        split_texts = splitter.split_text(doc["text"])

        for i, text in enumerate(split_texts):
            chunks.append({
                "text": text,
                "metadata": {
                    **doc["metadata"],
                    "chunk_id": i
                }
            })

    return chunks