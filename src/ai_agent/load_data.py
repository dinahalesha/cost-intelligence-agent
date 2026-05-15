import pandas as pd

def load_curated_data(path="data/curated/monthly_cost_summary.csv"):
    df = pd.read_csv(path)
    return df
