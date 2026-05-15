from InstructorEmbedding import INSTRUCTOR
import pandas as pd

def embed_cost_data(df):
    # Load local model (no internet needed)
    model = INSTRUCTOR("hkunlp/instructor-base")

    # Convert each row into a text string
    df["text"] = df.apply(
        lambda row: f"Month: {row['month']}, Planned: {row['planned_cost']}, Actual: {row['actual_cost']}, Variance: {row['variance']}",
        axis=1
    )

    # Instructor models require an instruction + text
    instruction = "Represent the financial cost data for semantic search:"

    embeddings = model.encode(
        [[instruction, t] for t in df["text"].tolist()]
    )

    return embeddings, df
