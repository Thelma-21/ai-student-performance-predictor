# 🎓 AI Student Performance Predictor

## Problem Statement
Predicting whether a student will pass or fail based on their reading and writing scores using machine learning. This tool helps educators identify at-risk students early and take proactive steps to support them.

## Tech Stack
- **Python 3.9**
- **Pandas** — data loading and preprocessing
- **Scikit-learn** — Logistic Regression model
- **Streamlit** — interactive web UI

## Features
- 📊 Scatter chart of training data (pass/fail distribution)
- 🎯 Model accuracy displayed on the app
- 🔍 Predict pass/fail from reading & writing scores
- 📈 Confidence percentage with progress bar

## Screenshots
![App Overview](screenshots/Screenshot%201.png)
![Pass Prediction](screenshots/Screenshot%20-%20Pass%20prediction.png)
![Fail Prediction](screenshots/Screenshot%20-Fail%20prediction.png)

## How to Run

1. Clone the repo:
git clone https://github.com/YOUR_USERNAME/ai-student-performance-predictor.git
cd ai-student-performance-predictor

2. Install dependencies:
pip install streamlit pandas scikit-learn

3. Run the app:
python3 -m streamlit run app.py
