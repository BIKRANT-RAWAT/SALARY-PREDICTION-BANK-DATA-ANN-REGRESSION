import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# -----------------------------
# Load Model and Encoders
# -----------------------------
model = tf.keras.models.load_model('model.h5')

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# -----------------------------
# Page Config & Styling
# -----------------------------
st.set_page_config(page_title="Salary Prediction", page_icon="💼", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f9fafc;
    }
    div.stButton > button:first-child {
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: 600;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #0056b3;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# App Header
# -----------------------------
st.title("💼 Salary Prediction Using Bank Data")
st.markdown(
    """
    This app predicts a customer’s **Estimated Salary** based on their banking profile using a trained
    **Artificial Neural Network (ANN)** model.
    """
)
st.markdown("---")

# -----------------------------
# Input Section
# -----------------------------
st.subheader("📋 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    geography = st.selectbox('🌍 Geography', onehot_encoder_geo.categories_[0])
    gender = st.selectbox('🧍 Gender', label_encoder_gender.classes_)
    age = st.slider('🎂 Age', 18, 92, 35)
    tenure = st.slider('📆 Tenure (Years with Bank)', 0, 10, 5)
    num_of_products = st.slider('🛍️ Number of Products', 1, 4, 1)

with col2:
    credit_score = st.number_input('💳 Credit Score', min_value=300, max_value=900, value=650)
    balance = st.number_input('💰 Account Balance', value=50000.0)
    has_cr_card = st.selectbox('💳 Has Credit Card?', [0, 1])
    is_active_member = st.selectbox('✅ Is Active Member?', [0, 1])

st.markdown("---")

# -----------------------------
# Prepare Input Data
# -----------------------------
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
})

# One-hot encode 'Geography'
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(
    geo_encoded, 
    columns=onehot_encoder_geo.get_feature_names_out(['Geography'])
)

# Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# -----------------------------
# Prediction Button
# -----------------------------
st.markdown("### 🧠 Model Prediction")

submit = st.button("🚀 Predict Salary")

if submit:
    prediction = model.predict(input_data_scaled)
    estimated_salary = float(prediction[0][0])

    st.markdown("---")
    st.subheader("📊 Prediction Result")
    st.metric(label="💼 Estimated Salary", value=f"${estimated_salary:,.2f}")
    st.success("✅ Prediction completed successfully!")

    # st.markdown(
    #     "<p style='text-align:center; color:gray;'>Powered by Artificial Neural Networks 🤖</p>",
    #     unsafe_allow_html=True
    # )
