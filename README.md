# 📉 Customer Churn Prediction — End-to-End ML Web App

> **Predict telecom customer churn before it happens — with 82% accuracy.**
> Built as a complete pipeline from raw data to a live deployed Streamlit web application.

---

## 🔥 Why This Project Matters

In the telecom industry, **acquiring a new customer costs 5–25x more than retaining an existing one.**
Even a 5% reduction in churn can increase profits by **25–95%.**

This project builds an intelligent churn detection system that:
- ✅ Identifies **which customers are at risk of leaving** — before they do
- ✅ Gives a **real-time churn probability with confidence score**
- ✅ Enables telecom companies to take **proactive retention action**

---

## 🚀 Live App

> Run locally in 3 steps — see [How to Run](#️-how-to-run-locally) below.

---

## 📌 What This Project Does

| Step | What Happened |
|---|---|
| 📥 Data | Loaded 7,043 real telecom customer records (21 features) |
| 🔍 EDA | Deep exploratory analysis — missing values, distributions, correlations |
| ⚙️ Feature Engineering | Encoded categoricals, handled nulls, selected key churn drivers |
| ⚖️ Class Balancing | Applied **SMOTE** to fix imbalanced churn/non-churn ratio |
| 🤖 Model Training | Decision Tree (79%) → Decision Tree + SMOTE (**82%**) → Random Forest |
| 💾 Deployment | Saved model as `model.sav`, deployed as **Streamlit web app** |
| 🖥️ Live UI | Interactive app — input customer info, get churn prediction instantly |

---

## 📊 Dataset

**Telco Customer Churn — IBM Watson / Kaggle**

| Attribute | Value |
|---|---|
| Total Records | **7,043 customers** |
| Total Features | **21 columns** |
| Target Variable | `Churn` — Yes / No |
| Class Imbalance | ~73% No Churn / ~27% Churn → Fixed with SMOTE |

**Key features used for prediction:**
- `tenure` — how long the customer has been with the company
- `Contract` — month-to-month, one year, two year
- `MonthlyCharges` — monthly billing amount
- `InternetService` — DSL, Fiber Optic, None
- `TechSupport`, `OnlineSecurity` — value-added services
- `PaymentMethod` — electronic check, credit card, etc.

---

## 🤖 Model Performance

| Model | Accuracy | Notes |
|---|---|---|
| Decision Tree (baseline) | 79% | Without balancing |
| **Decision Tree + SMOTE** | **82%** | ✅ Best deployed model |
| Random Forest | Evaluated | Ensemble comparison |

### 💡 Why is 82% Accuracy Good Here?

- The dataset has **class imbalance** — most customers don't churn
- A dummy model that always predicts "No Churn" gets ~73% — that's useless
- Our model at **82% learns actual churn patterns**, not just the majority class
- **SMOTE** synthetically balances training data so the model doesn't ignore minority churners
- In business terms: out of **100 at-risk customers**, this model correctly flags **~82** — enabling proactive retention before revenue is lost

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.x |
| Data Handling | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| ML Models | Scikit-learn — Decision Tree, Random Forest |
| Class Balancing | SMOTE (imbalanced-learn) |
| Deployment | **Streamlit** (upgraded from Flask) |
| Environment | Jupyter Notebook, Anaconda |
| Model Saving | Pickle (`.sav`) |

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── Churn Analysis - EDA.ipynb             # Full EDA notebook
├── Churn Prediction Model.ipynb           # Model building + evaluation
├── app.py                                 # Streamlit web app
├── model.sav                              # Saved trained model (pickle)
├── tel_churn.csv                          # Processed/cleaned dataset
├── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Raw dataset (Kaggle)
├── requirements.txt                       # Dependencies
└── README.md
```

---

## 🔍 EDA Highlights

- Identified **high churn rate** among month-to-month contract customers
- Customers on **Fiber Optic** internet churned more despite higher speed
- **Senior citizens** showed higher churn tendency
- Customers **without tech support or online security** had significantly higher churn
- **KDE plots, correlation heatmaps, and univariate distribution plots** used throughout
- Custom `uniplot()` function built for efficient single-variable visualisation

---

## ⚙️ How to Run Locally

```bash
# Step 1 — Clone the repo
git clone https://github.com/raghav-010/customer-churn-prediction.git
cd customer-churn-prediction

# Step 2 — Install dependencies
pip install -r requirements.txt

# Step 3 — Launch the app
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`

---

## 🖥️ App Features

- 🔢 Input customer details via interactive form (contract type, tenure, charges, services)
- 📈 Real-time churn probability output
- ✅ Clear **Stay / Churn** result with confidence score
- 💡 No retraining needed — pre-saved model loads instantly

---

## 📚 Reference

Project built following the end-to-end ML tutorial by **Satyajit Pattnaik**:
[End To End Machine Learning Project With Deployment | Customer Churn Analysis](https://www.youtube.com/live/GVECbcKUio4)

**Key difference:** Replaced Flask deployment with **Streamlit** for faster, cleaner UI.

---

## 👤 Author

**Raghav Balaji V**
📧 raghav.vrb010@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/raghavbalaji010) · [GitHub](https://github.com/raghav-010)

---

*Built while working full-time and learning data science simultaneously — April 2026*
