# 😴 SleepWell — Machine Learning–Based Sleep Quality & Lifestyle Insights

**SleepWell** is a machine learning–powered health analytics project designed to analyze sleep patterns, identify lifestyle behaviors that affect sleep quality, and generate personalized, rule-based recommendations for healthier daily routines.

The project combines exploratory data analysis, sleep-quality prediction models, and interpretable visualizations to help users understand and improve their sleep habits.

---

## 🧠 Project Overview

Sleep quality is influenced by multiple behavioral and lifestyle factors such as screen time, bedtime consistency, daily caffeine intake, and total sleep duration.

SleepWell models these factors using data-driven techniques to uncover relationships, predict sleep quality, and provide actionable lifestyle insights in a clear and interpretable way.

---

## 🎯 Project Objectives

- Predict sleep quality using machine learning models  
- Analyze lifestyle patterns associated with poor sleep  
- Identify key behavioral factors impacting sleep health  
- Provide personalized, rule-based lifestyle recommendations  
- Visualize relationships and trends for easy interpretation  

---

## ⚙️ System Components

The project is organized into the following modules:

- **`main.py`**  
  Orchestrates the full pipeline: data loading, modeling, recommendations, and visualization.

- **`model.py`**  
  Trains a machine learning model to predict sleep quality based on lifestyle features.

- **`recommender.py`**  
  Implements a rule-based recommendation engine that converts insights into actionable suggestions.

- **`visualize.py`**  
  Generates visual analytics such as correlation heatmaps and feature vs sleep-quality plots.

- **`data.csv`**  
  Structured dataset containing sleep metrics and lifestyle attributes.

- **`Assets/`**  
  Stores generated visualizations (e.g., heatmaps, trend plots).

---

## 📊 Data & Features

The dataset includes behavioral and sleep-related variables such as:

- Total sleep duration  
- Sleep quality score  
- Screen time before bed  
- Bedtime patterns  
- Daily caffeine intake  
- Lifestyle indicators  

Feature engineering is applied to capture meaningful patterns affecting sleep quality.

---

## 🤖 Machine Learning & Recommendations

- **Prediction Task**: Sleep quality prediction (regression or classification)  
- **Model Type**: Supervised machine learning model  
- **Inputs**:
  - Lifestyle and behavioral features  
- **Recommendation Logic**:
  - Rule-based system that generates personalized suggestions  
  - Examples: reducing screen time, adjusting bedtime, limiting caffeine intake  

The focus is on **interpretability and real-world applicability** rather than black-box predictions.

---

## 📈 Visualizations

SleepWell includes visual analytics such as:

- Correlation heatmaps between lifestyle factors and sleep quality  
- Feature vs sleep-quality plots (e.g., screen time vs sleep quality)  
- Trend-based visual insights for behavioral analysis  

All generated plots are saved in the `Assets/` directory.

---

## 🛠 Tech Stack

- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **Matplotlib / Seaborn**
