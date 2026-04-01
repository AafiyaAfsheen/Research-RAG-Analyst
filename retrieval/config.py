CHUNK_SIZE = 800
CHUNK_OVERLAP = 120

TOP_K = {
    "definition": 3,
    "comparison": 6,
    "analytical": 8,
    "citation": 2
}

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

CONFIDENCE_THRESHOLDS = {
    "high": 0.75,
    "medium": 0.55
}