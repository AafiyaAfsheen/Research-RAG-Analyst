from retrieval.chunking import create_chunks
from retrieval.embeddings import EmbeddingModel
from retrieval.vector_store import VectorStore
from retrieval.retriever import AdaptiveRetriever

from retrieval.pdf_loader import load_pdfs

documents = load_pdfs("data")

chunks = create_chunks(documents)

embedder = EmbeddingModel()

texts = [c["text"] for c in chunks]
embeddings = embedder.embed_texts(texts)

vector_store = VectorStore(dim=len(embeddings[0]))
vector_store.add_embeddings(embeddings, chunks)

retriever = AdaptiveRetriever(vector_store)

result = retriever.retrieve_context(
    "Why is self-contempt considered a form of conceit?",
    query_type="analytical"
)

print(result)