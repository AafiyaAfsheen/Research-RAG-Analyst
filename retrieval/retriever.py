from retrieval.embeddings import EmbeddingModel
from retrieval.vector_store import VectorStore
from retrieval.context_filter import filter_context
from retrieval.config import TOP_K, CONFIDENCE_THRESHOLDS


class AdaptiveRetriever:

    def __init__(self, vector_store):

        self.vector_store = vector_store
        self.embedding_model = EmbeddingModel()

    def determine_top_k(self, query_type):

        return TOP_K.get(query_type, 4)

    def compute_confidence(self, scores):

        avg_score = sum(scores) / len(scores)

        if avg_score > CONFIDENCE_THRESHOLDS["high"]:
            return "high"

        elif avg_score > CONFIDENCE_THRESHOLDS["medium"]:
            return "medium"

        return "low"

    def retrieve_context(self, query, query_type):

        query_embedding = self.embedding_model.embed_query(query)

        top_k = self.determine_top_k(query_type)

        results = self.vector_store.search(query_embedding, top_k)

        filtered_results = filter_context(results)

        scores = [r["score"] for r in filtered_results]

        confidence = self.compute_confidence(scores)

        return {
            "context": filtered_results,
            "confidence": confidence,
            "scores": scores
        }