def recommend_lifestyle(row):
    recommendations = []

    if row["sleep_duration_hours"] < 7:
        recommendations.append("Increase sleep to at least 7–8 hours per night.")

    if row["bedtime_hour"] >= 24 or row["bedtime_hour"] <= 1:
        recommendations.append("Try sleeping earlier (before 11:30 PM).")

    if row["screen_time_hours"] > 2:
        recommendations.append("Reduce screen time to under 2 hours before bedtime.")

    if row["caffeine_cups"] >= 3:
        recommendations.append("Limit caffeine to 1–2 cups and avoid it after 4 PM.")

    sleep_window = (row["wake_hour"] - row["bedtime_hour"]) % 24
    if sleep_window > 9:
        recommendations.append("Maintain a 7–9 hour sleeping window consistently.")

    if not recommendations:
        recommendations.append("Great routine! Keep going.")

    return recommendations
