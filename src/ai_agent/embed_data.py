from InstructorEmbedding import INSTRUCTOR
import pandas as pd

def embed_cost_data(df):
    # Load local model
    model = INSTRUCTOR("hkunlp/instructor-base")

    # Convert each row into a text string
    df["text"] = df.apply(
        lambda row: f"Month: {row['month']}, Planned: {row['planned_cost']}, Actual: {row['actual_cost']}, Variance: {row['variance']}",
        axis=1
    )

    instruction = "Represent the financial cost data for semantic search."

    # InstructorEmbedding requires dict format
    inputs = [
        {"instruction": instruction, "input": t}
        for t in df["text"].tolist()
    ]

    embeddings = model.encode(inputs)

    return embeddings, df
