from sklearn.feature_extraction.text import TfidfVectorizer

def query_agent(question):
    df = load_curated_data()
    embeddings, df = embed_cost_data(df)

    # Recreate vectorizer for question
    vectorizer = TfidfVectorizer()
    vectorizer.fit(df["text"].tolist())

    q_emb = vectorizer.transform([question]).toarray()

    sims = cosine_similarity(q_emb, embeddings)[0]
    top_idx = np.argmax(sims)

    result_row = df.iloc[top_idx]

    answer = generate_nl_response(result_row, question)
    followups = generate_follow_up_questions(result_row, question)

    return answer, followups
