import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def create_plots(csv_path="data.csv"):
    df = pd.read_csv(csv_path)

    # Correlation Heatmap
    plt.figure(figsize=(7, 5))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Sleep & Lifestyle Correlation Heatmap")
    plt.savefig("heatmap.png")

    # Screen time vs sleep quality
    plt.figure(figsize=(7, 5))
    sns.boxplot(x="sleep_quality", y="screen_time_hours", data=df)
    plt.title("Screen Time vs Sleep Quality")
    plt.savefig("screen_vs_quality.png")

    print("Saved: heatmap.png, screen_vs_quality.png")
