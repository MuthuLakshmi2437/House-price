import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model_pickle", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter the house details below.")

# User Inputs
area = st.number_input("Area (sq.ft)", min_value=100, value=1000)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=2
)

third_feature = st.number_input(
    "Third Feature",
    value=1
)

if st.button("Predict Price"):

    features = np.array([[area, bedrooms, bathrooms]])

    prediction = model.predict(features)

    st.success(f"Predicted Price : ₹ {prediction[0]:,.2f}")
