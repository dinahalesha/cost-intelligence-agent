import pandas as pd
import os

def clean_cost_data(
    input_path="data/raw/cost_data.csv",
    output_path="data/clean/cleaned_cost_data.csv"
):
    df = pd.read_csv(input_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Ensure numeric columns are correct type
    numeric_cols = ["planned_cost", "actual_cost", "variance"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # Recalculate variance to ensure correctness
    df["variance"] = df["actual_cost"] - df["planned_cost"]

    # Remove rows with missing values
    df = df.dropna()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save cleaned data
    df.to_csv(output_path, index=False)

    print("Cleaned data saved to:", output_path)
    return df

if __name__ == "__main__":
    clean_cost_data()

