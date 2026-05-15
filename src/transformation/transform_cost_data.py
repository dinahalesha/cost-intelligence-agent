import pandas as pd
import os

def transform_cost_data(
    input_path="data/clean/cleaned_cost_data.csv",
    output_path="data/curated/monthly_cost_summary.csv"
):
    df = pd.read_csv(input_path)

    # Convert month column to datetime
    df["month"] = pd.to_datetime(df["month"])

    # Monthly aggregation
    monthly_summary = df.groupby("month").agg({
        "planned_cost": "sum",
        "actual_cost": "sum",
        "variance": "sum"
    }).reset_index()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save transformed data
    monthly_summary.to_csv(output_path, index=False)

    print("Transformed data saved to:", output_path)
    return monthly_summary

if __name__ == "__main__":
    transform_cost_data()

