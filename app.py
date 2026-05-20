import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

# Title
st.title("House Price Prediction App")

# Input
area = st.number_input("Enter House Area")

# Prediction
if st.button("Predict"):
    prediction = model.predict(np.array([[area]]))

    st.success(f"Predicted Price: {prediction[0]}")