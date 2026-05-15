import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from load_data import load_curated_data
from embed_data import embed_cost_data
from nl_response import generate_nl_response
from follow_up import generate_follow_up_questions


def query_agent(question):
    # 1. Load curated dataset
    df = load_curated_data()

    # 2. Embed dataset using TF‑IDF (offline)
    embeddings, df = embed_cost_data(df)

    # 3. Recreate TF‑IDF vectorizer for the question
    vectorizer = TfidfVectorizer()
    vectorizer.fit(df["text"].tolist())

    q_emb = vectorizer.transform([question]).toarray()

    # 4. Compute similarity
    sims = cosine_similarity(q_emb, embeddings)[0]
    top_idx = np.argmax(sims)

    # 5. Retrieve best matching row
    result_row = df.iloc[top_idx]

    # 6. Generate natural‑language answer
    answer = generate_nl_response(result_row, question)

    # 7. Generate follow‑up questions
    followups = generate_follow_up_questions(result_row, question)

    return answer, followups


if __name__ == "__main__":
    ans, fups = query_agent("Which month had the highest variance")
    print(ans)
    print("\nFOLLOW‑UP QUESTIONS:")
    for q in fups:
        print("-", q)
