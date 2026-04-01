from sentence_transformers import SentenceTransformer
from retrieval.config import EMBEDDING_MODEL


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed_texts(self, texts):
        return self.model.encode(texts)

    def embed_query(self, query):
        return self.model.encode([query])[0]