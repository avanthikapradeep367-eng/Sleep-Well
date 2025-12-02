import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train_models(csv_path="data.csv"):

    df = pd.read_csv(csv_path)

    feature_cols = [
        "sleep_duration_hours",
        "bedtime_hour",
        "wake_hour",
        "caffeine_cups",
        "screen_time_hours"
    ]

    X = df[feature_cols]
    y = df["sleep_quality"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Decision Tree
    dt = DecisionTreeClassifier(max_depth=4, random_state=42)
    dt.fit(X_train, y_train)
    pred_dt = dt.predict(X_test)
    print("\nDecision Tree Accuracy:", accuracy_score(y_test, pred_dt))

    # Logistic Regression
    log = LogisticRegression(max_iter=1000)
    log.fit(X_train, y_train)
    pred_log = log.predict(X_test)
    print("Logistic Regression Accuracy:", accuracy_score(y_test, pred_log))

    return dt, log
