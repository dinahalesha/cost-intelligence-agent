def generate_follow_up_questions(row, question):
    month = row["month"]
    variance = row["variance"]

    followups = []

    if variance > 0:
        followups.append("Do you want to know why the cost overrun happened")
        followups.append("Should I compare this month with the previous one")
    else:
        followups.append("Would you like to see how this savings trend continues")
        followups.append("Should I compare this month with the yearly average")

    followups.append("Would you like a chart for this trend")
    followups.append("Do you want a summary for the entire quarter")

    return followups
