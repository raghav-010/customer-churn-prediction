import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(page_title="Churn Prediction", page_icon="📱", layout="wide")

# Custom CSS - Dark theme with neon colors
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Rajdhani:wght@400;600&display=swap');

    /* ── Global background ── */
    .stApp, .main, [data-testid="stAppViewContainer"] {
        background-color: #0a0a0f !important;
        color: #e0e0e0 !important;
    }
    [data-testid="stHeader"] { background-color: #0a0a0f !important; }
    [data-testid="stSidebar"] { background-color: #0d0d1a !important; }

    /* ── Title ── */
    .neon-title {
        font-family: 'Orbitron', monospace;
        font-size: 2.6rem;
        font-weight: 700;
        text-align: center;
        color: #00f5ff;
        text-shadow: 0 0 10px #00f5ff, 0 0 30px #00f5ff, 0 0 60px #0099cc;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        text-align: center;
        color: #7ecfff;
        font-size: 1rem;
        margin-bottom: 1.5rem;
        letter-spacing: 1px;
    }

    /* ── Section boxes ── */
    .section-box {
        background: linear-gradient(135deg, #0d0d2b 0%, #0a0a1f 100%);
        border: 1px solid #00f5ff44;
        border-radius: 16px;
        padding: 20px 25px 10px 25px;
        margin-bottom: 20px;
        box-shadow: 0 0 20px #00f5ff22, inset 0 0 30px #00f5ff08;
    }
    .section-title {
        font-family: 'Orbitron', monospace;
        font-size: 1rem;
        font-weight: 700;
        color: #00f5ff;
        text-shadow: 0 0 8px #00f5ff;
        letter-spacing: 2px;
        text-transform: uppercase;
        border-bottom: 1px solid #00f5ff33;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }

    /* ── Labels ── */
    label, .stSelectbox label, .stNumberInput label {
        color: #7ecfff !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
    }

    /* ── Selectbox & Number Input ── */
    [data-testid="stSelectbox"] > div > div,
    [data-testid="stNumberInput"] > div > div > input {
        background-color: #0d1b2e !important;
        border: 1px solid #00f5ff55 !important;
        border-radius: 8px !important;
        color: #ffffff !important;
    }
    [data-testid="stSelectbox"] > div > div:hover,
    [data-testid="stNumberInput"] > div > div > input:focus {
        border-color: #00f5ff !important;
        box-shadow: 0 0 8px #00f5ff66 !important;
    }

    /* ── Predict button ── */
    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, #00f5ff, #0066ff) !important;
        color: #000000 !important;
        font-family: 'Orbitron', monospace !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        padding: 18px 60px !important;
        border-radius: 50px !important;
        border: none !important;
        width: 100% !important;
        box-shadow: 0 0 25px #00f5ff88, 0 0 60px #00f5ff44 !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stButton"] > button:hover {
        background: linear-gradient(135deg, #ff00ff, #00f5ff) !important;
        box-shadow: 0 0 40px #ff00ffaa, 0 0 80px #00f5ff66 !important;
        transform: scale(1.03) !important;
    }

    /* ── Metric boxes ── */
    [data-testid="stMetric"] {
        background: #0d1b2e !important;
        border: 1px solid #00f5ff44 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        text-align: center !important;
    }
    [data-testid="stMetricLabel"] { color: #7ecfff !important; font-size: 0.8rem !important; }
    [data-testid="stMetricValue"] { color: #00f5ff !important; font-size: 1.8rem !important; text-shadow: 0 0 10px #00f5ff !important; }

    /* ── Result boxes ── */
    [data-testid="stSuccess"] {
        background: linear-gradient(135deg, #001a00, #003300) !important;
        border: 1px solid #00ff88 !important;
        border-radius: 12px !important;
        color: #00ff88 !important;
        font-size: 1.1rem !important;
        text-shadow: 0 0 8px #00ff88 !important;
        box-shadow: 0 0 20px #00ff8844 !important;
    }
    [data-testid="stError"] {
        background: linear-gradient(135deg, #1a0000, #330000) !important;
        border: 1px solid #ff3366 !important;
        border-radius: 12px !important;
        color: #ff3366 !important;
        font-size: 1.1rem !important;
        text-shadow: 0 0 8px #ff3366 !important;
        box-shadow: 0 0 20px #ff336644 !important;
    }

    /* ── Divider ── */
    hr { border-color: #00f5ff22 !important; }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #0a0a0f; }
    ::-webkit-scrollbar-thumb { background: #00f5ff44; border-radius: 3px; }
    </style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open('model.sav', 'rb'))

# ── Title ──────────────────────────────────────────────────────────
st.markdown("<div class='neon-title'>📱 CHURN PREDICTION AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>⚡ Telecom Customer Intelligence System ⚡</div>", unsafe_allow_html=True)
st.markdown("---")

# ── Section 1: Basic Info ──────────────────────────────────────────
st.markdown("<div class='section-box'><div class='section-title'>👤 Basic Information</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    senior_citizen  = st.selectbox("Senior Citizen", ["No", "Yes"])
    gender          = st.selectbox("Gender", ["Male", "Female"])
with col2:
    partner         = st.selectbox("Partner", ["Yes", "No"])
    dependents      = st.selectbox("Dependents", ["Yes", "No"])
with col3:
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 50.0)
    total_charges   = st.number_input("Total Charges ($)", 0.0, 10000.0, 500.0)
st.markdown("</div>", unsafe_allow_html=True)

# ── Section 2: Phone & Internet ───────────────────────────────────
st.markdown("<div class='section-box'><div class='section-title'>📞 Phone & Internet Services</div>", unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)
with col4:
    phone_service    = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines   = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
with col5:
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
with col6:
    st.write("")
st.markdown("</div>", unsafe_allow_html=True)

# ── Section 3: Online Services ────────────────────────────────────
st.markdown("<div class='section-box'><div class='section-title'>🔒 Online Services</div>", unsafe_allow_html=True)
col7, col8, col9 = st.columns(3)
with col7:
    online_security   = st.selectbox("Online Security",   ["No", "Yes", "No internet service"])
    online_backup     = st.selectbox("Online Backup",     ["No", "Yes", "No internet service"])
with col8:
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    tech_support      = st.selectbox("Tech Support",      ["No", "Yes", "No internet service"])
with col9:
    streaming_tv      = st.selectbox("Streaming TV",      ["No", "Yes", "No internet service"])
    streaming_movies  = st.selectbox("Streaming Movies",  ["No", "Yes", "No internet service"])
st.markdown("</div>", unsafe_allow_html=True)

# ── Section 4: Contract & Billing ─────────────────────────────────
st.markdown("<div class='section-box'><div class='section-title'>📄 Contract & Billing</div>", unsafe_allow_html=True)
col10, col11, col12 = st.columns(3)
with col10:
    contract          = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
with col11:
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method    = st.selectbox("Payment Method", [
        "Bank transfer (automatic)", "Credit card (automatic)",
        "Electronic check", "Mailed check"
    ])
with col12:
    tenure_group      = st.selectbox("Tenure Group (months)", [
        "1 - 12", "13 - 24", "25 - 36", "37 - 48", "49 - 60", "61 - 72"
    ])
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ── Encode ─────────────────────────────────────────────────────────
def encode_input():
    data = {
        'SeniorCitizen': [1 if senior_citizen == "Yes" else 0],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges':   [total_charges],
        'gender_Female':  [gender == "Female"],
        'gender_Male':    [gender == "Male"],
        'Partner_No':     [partner == "No"],
        'Partner_Yes':    [partner == "Yes"],
        'Dependents_No':  [dependents == "No"],
        'Dependents_Yes': [dependents == "Yes"],
        'PhoneService_No':  [phone_service == "No"],
        'PhoneService_Yes': [phone_service == "Yes"],
        'MultipleLines_No':               [multiple_lines == "No"],
        'MultipleLines_No phone service': [multiple_lines == "No phone service"],
        'MultipleLines_Yes':              [multiple_lines == "Yes"],
        'InternetService_DSL':            [internet_service == "DSL"],
        'InternetService_Fiber optic':    [internet_service == "Fiber optic"],
        'InternetService_No':             [internet_service == "No"],
        'OnlineSecurity_No':              [online_security == "No"],
        'OnlineSecurity_No internet service': [online_security == "No internet service"],
        'OnlineSecurity_Yes':             [online_security == "Yes"],
        'OnlineBackup_No':                [online_backup == "No"],
        'OnlineBackup_No internet service': [online_backup == "No internet service"],
        'OnlineBackup_Yes':               [online_backup == "Yes"],
        'DeviceProtection_No':            [device_protection == "No"],
        'DeviceProtection_No internet service': [device_protection == "No internet service"],
        'DeviceProtection_Yes':           [device_protection == "Yes"],
        'TechSupport_No':                 [tech_support == "No"],
        'TechSupport_No internet service':[tech_support == "No internet service"],
        'TechSupport_Yes':                [tech_support == "Yes"],
        'StreamingTV_No':                 [streaming_tv == "No"],
        'StreamingTV_No internet service':[streaming_tv == "No internet service"],
        'StreamingTV_Yes':                [streaming_tv == "Yes"],
        'StreamingMovies_No':             [streaming_movies == "No"],
        'StreamingMovies_No internet service': [streaming_movies == "No internet service"],
        'StreamingMovies_Yes':            [streaming_movies == "Yes"],
        'Contract_Month-to-month':        [contract == "Month-to-month"],
        'Contract_One year':              [contract == "One year"],
        'Contract_Two year':              [contract == "Two year"],
        'PaperlessBilling_No':            [paperless_billing == "No"],
        'PaperlessBilling_Yes':           [paperless_billing == "Yes"],
        'PaymentMethod_Bank transfer (automatic)': [payment_method == "Bank transfer (automatic)"],
        'PaymentMethod_Credit card (automatic)':   [payment_method == "Credit card (automatic)"],
        'PaymentMethod_Electronic check':          [payment_method == "Electronic check"],
        'PaymentMethod_Mailed check':              [payment_method == "Mailed check"],
        'tenure_group_1 - 12':  [tenure_group == "1 - 12"],
        'tenure_group_13 - 24': [tenure_group == "13 - 24"],
        'tenure_group_25 - 36': [tenure_group == "25 - 36"],
        'tenure_group_37 - 48': [tenure_group == "37 - 48"],
        'tenure_group_49 - 60': [tenure_group == "49 - 60"],
        'tenure_group_61 - 72': [tenure_group == "61 - 72"],
    }
    return pd.DataFrame(data)

# ── Predict Button ─────────────────────────────────────────────────
col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
with col_b2:
    predict_clicked = st.button("⚡ ANALYZE & PREDICT CHURN ⚡")

if predict_clicked:
    input_df = encode_input()
    model_columns = model.feature_names_in_
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = False
    input_df = input_df[model_columns]

    prediction  = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    st.markdown("---")
    st.markdown("<div class='section-title' style='text-align:center; font-size:1.3rem;'>🎯 PREDICTION RESULT</div>", unsafe_allow_html=True)

    col_r1, col_r2, col_r3 = st.columns(3)
    with col_r1:
        st.metric("🔴 Churn Probability",    f"{probability[1]*100:.1f}%")
    with col_r2:
        st.metric("🟢 Stay Probability",     f"{probability[0]*100:.1f}%")
    with col_r3:
        st.metric("📊 Prediction", "CHURN ⚠️" if prediction == 1 else "STAY ✅")

    st.markdown("<br>", unsafe_allow_html=True)
    if prediction == 1:
        st.error(f"⚠️  WARNING: This customer is HIGHLY LIKELY TO CHURN!  |  Confidence: {probability[1]*100:.1f}%")
    else:
        st.success(f"✅  SAFE: This customer is NOT likely to churn.  |  Confidence: {probability[0]*100:.1f}%")
