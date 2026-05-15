import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from load_data import load_curated_data
from embed_data import embed_cost_data

def query_agent(question):
    df = load_curated_data()
    embeddings, df = embed_cost_data(df)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    q_emb = model.encode([question])

    sims = cosine_similarity(q_emb, embeddings)[0]
    top_idx = np.argmax(sims)

    result = df.iloc[top_idx]
    return result

