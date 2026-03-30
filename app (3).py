import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('car_price_model.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #74ebd5, #ACB6E5);
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
    }
    .title {
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🚗 Car Price Predictor</div>', unsafe_allow_html=True)
st.write("### Enter Car Details Below:")

# Inputs (organized in columns)
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("📅 Year", min_value=2000, max_value=2025)
    price = st.number_input("💰 Present Price (lakhs)")
    kms = st.number_input("🛣️ Kilometers Driven")

with col2:
    fuel = st.selectbox("⛽ Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller = st.selectbox("🏪 Seller Type", ["Dealer", "Individual"])
    trans = st.selectbox("⚙️ Transmission", ["Manual", "Automatic"])

owner = st.slider("👤 Number of Owners", 0, 3)

# Prediction button
if st.button("🚀 Predict Price"):
    fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
    seller_map = {"Dealer": 0, "Individual": 1}
    trans_map = {"Manual": 0, "Automatic": 1}

    input_data = np.array([[year, price, kms,
                            fuel_map[fuel],
                            seller_map[seller],
                            trans_map[trans],
                            owner]])

    prediction = model.predict(input_data)

    st.success(f"💎 Estimated Car Price: ₹ {round(prediction[0], 2)} Lakhs")

# Footer
st.markdown("---")
