# 📊 Employee Satisfaction Analytics

A complete Human Resources Analytics project built using Python, Machine Learning, Natural Language Processing, and Streamlit.

The project analyzes synthetic employee survey responses to identify the key drivers of employee satisfaction and presents interactive insights through a professional dashboard.

---

# Project Overview

This project demonstrates a complete end-to-end data science workflow including:

- Synthetic HR data generation
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Statistical hypothesis testing
- Natural Language Processing (NLP)
- Machine Learning classification
- Feature importance analysis
- Interactive Streamlit dashboard
- Executive HR recommendations

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- NLTK
- Streamlit
- Plotly
- Matplotlib
- Joblib

---

# Project Structure

```
SatisfyAI

│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│
├── src
│   ├── data_generator.py
│   ├── data_cleaning.py
│   ├── nlp_processing.py
│   └── model_training.py
│
├── dashboard.py
├── requirements.txt
├── README.md
├── hr_recommendations.md
├── evaluation_metrics.json
├── feature_importance.json
├── statistical_results.json
└── satisfaction_model.pkl
```

---
## 🌐 Live Dashboard

Explore the deployed dashboard here:

**https://satisfyai-shahid.streamlit.app**

# Dataset

The project uses synthetically generated employee survey data.

The dataset contains:

- Employee ID
- Department
- Role
- Tenure
- Work-Life Balance
- Manager Effectiveness
- Career Growth
- Satisfaction Category
- Employee Comments

---

# Machine Learning Pipeline

1. Generate synthetic employee survey data

2. Clean and merge datasets

3. Handle missing values

4. Perform statistical hypothesis testing

5. Process employee comments using NLP

6. Generate TF-IDF features

7. Train a Random Forest classifier

8. Evaluate model performance

9. Extract feature importance

10. Build an interactive Streamlit dashboard

---

# Output Files

The project automatically generates:

- clean_survey_data.csv
- statistical_results.json
- evaluation_metrics.json
- feature_importance.json
- satisfaction_model.pkl

---

# Installation

Clone the repository

```bash
git clone https://github.com/shahid200620/SatisfyAI.git
```

Move into the project

```bash
cd SatisfyAI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Generate data

```bash
python src\data_generator.py
```

Clean data

```bash
python src\data_cleaning.py
```

Run NLP pipeline

```bash
python src\nlp_processing.py
```

Train model

```bash
python src\model_training.py
```

Launch dashboard

```bash
streamlit run dashboard.py
```

---

# Dashboard Features

- Executive HR Dashboard
- Department Analytics
- Role Analytics
- Sentiment Analysis
- Feature Importance
- Machine Learning Insights
- Data Explorer

---

# Business Value

The project enables HR teams to:

- Monitor employee satisfaction
- Detect engagement trends
- Understand employee feedback
- Identify important satisfaction drivers
- Support data-driven HR decisions

---

# Future Improvements

- Real-time dashboard updates
- Database integration
- Employee attrition prediction
- Deep Learning sentiment analysis
- Cloud deployment

---

# Author

Mohammed Shahid Ali Khan

B.Tech Computer Science Engineering

Employee Satisfaction Analytics Project
