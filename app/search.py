import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

movies = pd.read_csv("data/processed/processed_movies.csv")

index = faiss.read_index("models/movie_index.faiss")

model = SentenceTransformer("models/sentence_model")


def search_movies(query, k=5):

    query_embedding = model.encode([query]).astype("float32")
    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, k)

    # min semantic similarity required
    threshold = 0.20

    valid_results = scores[0] >= threshold

    if not valid_results.any():
        return None

    results = movies.iloc[indices[0][valid_results]][
        ["title", "year", "genres", "plot outline","plot"]
    ].copy()

    results.rename(columns={"plot outline": "Summary"}, inplace=True)

    results["Score"] = (scores[0][valid_results] * 100).round().astype(int)

    return results