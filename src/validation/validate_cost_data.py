import pandas as pd

def validate_cost_data(path="data/clean/cleaned_cost_data.csv"):
    df = pd.read_csv(path)

    print("\n===== DATA VALIDATION REPORT =====\n")

    # 1. Missing values
    missing = df.isnull().sum()
    print("Missing values per column:")
    print(missing, "\n")

    # 2. Negative costs
    negative_costs = df[(df["planned_cost"] < 0) | (df["actual_cost"] < 0)]
    print("Rows with negative planned or actual cost:")
    print(negative_costs if not negative_costs.empty else "None", "\n")

    # 3. Variance mismatch
    df["expected_variance"] = df["actual_cost"] - df["planned_cost"]
    variance_mismatch = df[df["variance"] != df["expected_variance"]]
    print("Rows with incorrect variance values:")
    print(variance_mismatch if not variance_mismatch.empty else "None", "\n")

    # 4. Invalid dates
    try:
        df["month"] = pd.to_datetime(df["month"], errors="coerce")
        invalid_dates = df[df["month"].isnull()]
        print("Rows with invalid month format:")
        print(invalid_dates if not invalid_dates.empty else "None", "\n")
    except Exception as e:
        print("Date validation error:", e)

    # 5. Duplicate rows
    duplicates = df[df.duplicated()]
    print("Duplicate rows:")
    print(duplicates if not duplicates.empty else "None", "\n")

    # 6. Unexpected suppliers
    allowed_suppliers = ["Bosch", "Siemens", "Continental", "Magna", "ZF"]
    unexpected_suppliers = df[~df["supplier"].isin(allowed_suppliers)]
    print("Unexpected suppliers:")
    print(unexpected_suppliers if not unexpected_suppliers.empty else "None", "\n")

    print("===== VALIDATION COMPLETE =====\n")

    return df

if __name__ == "__main__":
    validate_cost_data()
