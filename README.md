# Customer Churn Prediction — End-to-End ML Web App

> Predict telecom customer churn before it happens — with 82% accuracy.
> Full pipeline from raw data to a live deployed Streamlit web application.

---

## What This Does

Telecom companies lose significant revenue when customers leave. This project builds an intelligent churn detection system that:

- Identifies **which customers are at risk** before they churn
- Outputs a **real-time churn probability with confidence score**
- Enables companies to act **proactively** instead of reactively

Built on 7,043 real customer records from the IBM Telco Churn dataset.

---

## Live App

Deployed on Streamlit Cloud — [**raghav010-churn-prediction.streamlit.app**](https://raghav010-churn-prediction.streamlit.app)

---

## Pipeline Overview

| Stage | What Was Done |
|---|---|
| Data | 7,043 telecom customer records, 21 features |
| EDA | Missing value analysis, distributions, correlation heatmaps, KDE plots |
| Feature Engineering | Categorical encoding, null handling, churn driver identification |
| Class Balancing | SMOTE applied to fix ~73/27 class imbalance |
| Modelling | Decision Tree (79%) → Decision Tree + SMOTE (**82%**) → Random Forest |
| Deployment | Model saved as `model.sav`, served via Streamlit web app |

---

## Model Performance

| Model | Accuracy | Notes |
|---|---|---|
| Decision Tree | 79% | Baseline, no balancing |
| **Decision Tree + SMOTE** | **82%** | Deployed model |
| Random Forest | Evaluated | Ensemble comparison |

**Why 82% matters here:** A naive model that always predicts "No Churn" scores ~73% — because that's the majority class. At 82%, this model actually learns churn patterns. With SMOTE balancing, it no longer ignores the minority class. In business terms: out of 100 at-risk customers, this model correctly flags ~82 of them.

---

## Dataset

**Telco Customer Churn — IBM Watson / Kaggle**
`WA_Fn-UseC_-Telco-Customer-Churn.csv`

| Attribute | Value |
|---|---|
| Records | 7,043 customers |
| Features | 21 columns |
| Target | `Churn` — Yes / No |
| Imbalance | ~73% No / ~27% Yes → Fixed with SMOTE |

Key predictive features: `tenure`, `Contract`, `MonthlyCharges`, `InternetService`, `TechSupport`, `OnlineSecurity`, `PaymentMethod`

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3 |
| Data | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| ML | Scikit-learn — Decision Tree, Random Forest |
| Balancing | SMOTE (imbalanced-learn) |
| Deployment | Streamlit |
| Environment | Jupyter Notebook, Anaconda |
| Model Saving | Pickle (`.sav`) |

---

## Project Structure

```
customer-churn-prediction/
│
├── Churn Analysis - EDA.ipynb           # Full EDA notebook
├── Churn Prediction Model.ipynb         # Model building and evaluation
├── app.py                               # Streamlit web app
├── model.sav                            # Trained model (pickle)
├── tel_churn.csv                        # Cleaned dataset
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Raw dataset
├── requirements.txt                     # Dependencies
└── README.md
```

---

## EDA Findings

- Month-to-month contract customers churn at significantly higher rates
- Fiber Optic users churn more despite higher speeds — likely due to pricing
- Senior citizens show elevated churn tendency
- Absence of tech support and online security strongly correlates with churn
- Custom `uniplot()` function written for clean univariate visualisation across features

---

## How to Run Locally

```bash
git clone https://github.com/raghav-010/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt
streamlit run app.py
```

App opens at `http://localhost:8501`

---

## App Features

- Interactive form — input contract type, tenure, charges, services
- Real-time churn probability output
- Clear Stay / Churn result with confidence score
- Pre-loaded model — no retraining required

---

## Author

**Raghav Balaji V**
📧 raghav.vrb010@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/raghavbalaji010) · [GitHub](https://github.com/raghav-010)

---

*Built while working full-time — part of an ongoing transition into data science and ML engineering.*
