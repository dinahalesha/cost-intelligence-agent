import pandas as pd

def load_raw_cost_data(path="data/raw/cost_data.csv"):
    df = pd.read_csv(path)
    print("Raw data loaded successfully.")
    print(df.head())
    return df

if __name__ == "__main__":
    load_raw_cost_data()

