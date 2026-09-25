<div align="center">

# 📉 Customer Churn Prediction
### End-to-End Machine Learning Web Application

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)

**Predict which telecom customers will leave — before they do.**
Built as a complete ML pipeline: raw data → EDA → feature engineering → model training → live deployed web app.

[![Live App](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit%20Cloud-FF4B4B?style=for-the-badge)](https://raghav010-churn-prediction.streamlit.app)

</div>

---

## 🧩 Problem Statement

In the telecom industry, **customer churn is one of the most expensive problems** a business can face.

> Acquiring a new customer costs **5–25× more** than retaining an existing one.
> A **5% reduction in churn** can increase profits by **25–95%**.

Yet most telecom companies only react *after* a customer has already left. This project flips that model — building a system that **identifies at-risk customers in advance**, giving retention teams the window they need to act.

---

## 🎯 Project Objectives

- ✅ Perform deep **Exploratory Data Analysis** to understand churn drivers
- ✅ Build and compare **multiple ML classification models**
- ✅ Handle **class imbalance** using SMOTE oversampling
- ✅ Deploy a **live interactive web app** for real-time churn prediction
- ✅ Deliver **business-ready insights** — not just model accuracy numbers

---

## 🚀 Live Application

> **Deployed on Streamlit Cloud — accessible from any browser, no setup needed.**

🔗 **[raghav010-churn-prediction.streamlit.app](https://raghav010-churn-prediction.streamlit.app)**

**What the app does:**
- Takes customer details as input (contract type, tenure, monthly charges, subscribed services)
- Runs prediction through the trained model in real time
- Returns a clear **Stay / Churn** verdict with a **confidence probability score**
- No retraining required — pre-saved model loads instantly

---

## 📊 Dataset

**Source:** IBM Watson Telco Customer Churn Dataset (via Kaggle)
**File:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`

| Attribute | Detail |
|---|---|
| 📦 Total Records | 7,043 customer entries |
| 📋 Total Features | 21 columns |
| 🎯 Target Variable | `Churn` — Yes (churned) / No (retained) |
| ⚠️ Class Imbalance | ~73% No Churn / ~27% Churn → addressed with SMOTE |

**Key predictive features used:**

| Feature | Description |
|---|---|
| `tenure` | How long the customer has been with the company (months) |
| `Contract` | Month-to-month, one year, or two year contract type |
| `MonthlyCharges` | Customer's monthly billing amount |
| `InternetService` | DSL, Fiber Optic, or None |
| `TechSupport` | Whether the customer has tech support add-on |
| `OnlineSecurity` | Whether the customer has online security add-on |
| `PaymentMethod` | Electronic check, mailed check, credit card, bank transfer |

---

## 🔍 Exploratory Data Analysis

Full EDA performed in `Churn Analysis - EDA.ipynb`.

**Key findings:**

| Insight | Finding |
|---|---|
| 📃 Contract Type | Month-to-month customers churn at **significantly higher rates** than annual/biannual subscribers |
| 🌐 Internet Service | Fiber Optic users churn more despite faster speeds — strong indicator of **pricing dissatisfaction** |
| 👴 Senior Citizens | Senior customers show **elevated churn tendency** compared to non-senior segment |
| 🔒 Add-on Services | Customers **without tech support or online security** churn at disproportionately high rates |
| 💳 Payment Method | Electronic check users show higher churn — may indicate **lower commitment** to the service |
| ⏱️ Tenure | Customers in their **first 12 months** are most at risk — early churn window is critical |

**Techniques used:**
- Univariate, bivariate, and multivariate analysis
- KDE plots and distribution analysis across churn segments
- Correlation heatmap for feature relationship mapping
- Custom `uniplot()` function built for efficient single-variable visualisation across all features
- Missing value analysis and outlier detection

---

## ⚙️ Feature Engineering & Preprocessing

- **Missing value handling** — `TotalCharges` converted from object to numeric, nulls filled appropriately
- **Categorical encoding** — Label encoding and binary mapping applied across all categorical features
- **Feature selection** — Irrelevant columns (`customerID`) dropped; key churn drivers retained
- **Train/test split** — 80/20 stratified split to preserve class distribution
- **SMOTE (Synthetic Minority Oversampling Technique)** — Applied to training data to address the 73/27 class imbalance without losing data

---

## 🤖 Model Building & Results

Full modelling in `Churn Prediction Model.ipynb`.

| Model | Accuracy | Notes |
|---|---|---|
| Decision Tree (baseline) | 79% | No class balancing applied |
| **Decision Tree + SMOTE** | **82%** ✅ | **Deployed production model** |
| Random Forest | Evaluated | Ensemble comparison for benchmarking |

### 💡 Why 82% Is Meaningful Here

A naive model that always predicts "No Churn" would score **~73% accuracy** — simply by exploiting the class imbalance and never detecting a single churner. That's a useless model with a deceptively high score.

At **82% with SMOTE balancing**, this model:
- Actually **learns churn patterns** instead of defaulting to the majority class
- Correctly identifies **~82 out of every 100 at-risk customers**
- Gives retention teams a **real, actionable signal** — not noise

---

## 🛠️ Tech Stack

| Category | Tools & Libraries |
|---|---|
| 🐍 Language | Python 3.x |
| 📊 Data Manipulation | Pandas, NumPy |
| 📈 Visualisation | Matplotlib, Seaborn |
| 🤖 Machine Learning | Scikit-learn — Decision Tree Classifier, Random Forest Classifier |
| ⚖️ Class Balancing | SMOTE — imbalanced-learn |
| 🚀 Deployment | Streamlit |
| 💻 Environment | Jupyter Notebook, Anaconda |
| 💾 Model Persistence | Pickle (`.sav`) |

---

## 📁 Repository Structure

```
customer-churn-prediction/
│
├── 📓 Churn Analysis - EDA.ipynb           # Full exploratory data analysis
├── 📓 Churn Prediction Model.ipynb         # Model training, SMOTE, evaluation
├── 🚀 app.py                               # Streamlit web application
├── 💾 model.sav                            # Saved trained model (pickle)
├── 📄 tel_churn.csv                        # Cleaned & processed dataset
├── 📄 WA_Fn-UseC_-Telco-Customer-Churn.csv # Raw Kaggle dataset
├── 📋 requirements.txt                     # Python dependencies
└── 📖 README.md
```

---

## ▶️ Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/raghav-010/customer-churn-prediction.git
cd customer-churn-prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit app
streamlit run app.py
```

App will open at `http://localhost:8501`

---

## 📌 Business Impact Summary

| Metric | Value |
|---|---|
| 🎯 Model Accuracy | 82% (vs 73% naive baseline) |
| 📦 Dataset Size | 7,043 customers, 21 features |
| ⚖️ Imbalance Fix | SMOTE oversampling on training data |
| 🌐 Deployment | Live web app — Streamlit Cloud |
| 💼 Business Use Case | Proactive churn prevention, retention targeting |

---

## 👤 Author

<div align="center">

**Raghav Balaji V**

Data Science & ML Enthusiast | Python · SQL · Power BI · Scikit-learn

[![Email](https://img.shields.io/badge/Email-raghav.vrb010%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:raghav.vrb010@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-raghavbalaji010-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/raghavbalaji010)
[![GitHub](https://img.shields.io/badge/GitHub-raghav--010-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/raghav-010)

</div>

---

<div align="center">
<i>Part of an ongoing portfolio built during a self-driven transition into data science and ML engineering — working full-time while upskilling every evening.</i>
</div>
