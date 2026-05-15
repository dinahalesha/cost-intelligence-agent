from sentence_transformers import SentenceTransformer
import pandas as pd

def embed_cost_data(df):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    df["text"] = df.apply(
        lambda row: f"Month: {row['month']}, Planned: {row['planned_cost']}, Actual: {row['actual_cost']}, Variance: {row['variance']}",
        axis=1
    )

    embeddings = model.encode(df["text"].tolist())
    return embeddings, df
