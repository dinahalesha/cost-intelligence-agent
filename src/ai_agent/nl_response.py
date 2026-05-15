def generate_nl_response(row, question):
    month = row["month"]
    planned = row["planned_cost"]
    actual = row["actual_cost"]
    variance = row["variance"]

    direction = "overrun" if variance > 0 else "savings"

    return (
        f"For your question: '{question}', here's what I found.\n\n"
        f"In {month}, the planned cost was {planned:,} and the actual cost was {actual:,}.\n"
        f"This resulted in a variance of {variance:,}, indicating a cost {direction}.\n"
        f"Let me know if you want a deeper breakdown or a comparison with other months."
    )
