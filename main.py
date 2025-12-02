import pandas as pd
from model import train_models
from recommender import recommend_lifestyle
from visualize import create_plots


# Train machine learning models
dt_model, log_model = train_models("data.csv")


def sleepwell_report(model, sleep_duration, bedtime_hour, wake_hour,
                     caffeine_cups, screen_time_hours):

    data = pd.DataFrame([{
        "sleep_duration_hours": sleep_duration,
        "bedtime_hour": bedtime_hour,
        "wake_hour": wake_hour,
        "caffeine_cups": caffeine_cups,
        "screen_time_hours": screen_time_hours
    }])

    prediction = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]

    print(f"\nPredicted Sleep Quality: {'Good' if prediction == 1 else 'Poor'}")
    print(f"Confidence: {prob:.2f}")

    print("\nLifestyle Recommendations:")
    recommendations = recommend_lifestyle(data.iloc[0])
    for r in recommendations:
        print("- " + r)


if __name__ == "__main__":
    print("\n=== SleepWell System Running ===")

    # Create and save plots
    create_plots("data.csv")

    # Example report
    sleepwell_report(
        log_model,
        sleep_duration=5.5,
        bedtime_hour=1,
        wake_hour=7,
        caffeine_cups=3,
        screen_time_hours=4
    )
