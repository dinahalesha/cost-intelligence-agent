from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def embed_cost_data(df):
    # Convert each row into a text string
    df["text"] = df.apply(
        lambda row: f"Month {row['month']} planned {row['planned_cost']} actual {row['actual_cost']} variance {row['variance']}",
        axis=1
    )

    vectorizer = TfidfVectorizer()
    embeddings = vectorizer.fit_transform(df["text"].tolist()).toarray()

    return embeddings, df
