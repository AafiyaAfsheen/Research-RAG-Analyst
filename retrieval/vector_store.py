import faiss
import numpy as np


class VectorStore:

    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata_store = []
        self.text_store = []

    def add_embeddings(self, embeddings, chunks):

        self.index.add(np.array(embeddings))

        for chunk in chunks:
            self.text_store.append(chunk["text"])
            self.metadata_store.append(chunk["metadata"])

    def search(self, query_embedding, top_k):

        distances, indices = self.index.search(
            np.array([query_embedding]), top_k
        )

        results = []

        for i, idx in enumerate(indices[0]):

            results.append({
                "text": self.text_store[idx],
                "metadata": self.metadata_store[idx],
                "score": float(distances[0][i])
            })

        return results