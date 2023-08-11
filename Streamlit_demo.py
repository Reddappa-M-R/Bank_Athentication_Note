# Do some changes because i did for flask this i did not run

import streamlit as st
import requests
import pandas as pd

# Streamlit UI
st.title("Bank Note Authentication Prediction")

variance = st.number_input("Variance", value=0.5)
skewness = st.number_input("Skewness", value=0.5)
curtosis = st.number_input("Curtosis", value=0.5)
entropy = st.number_input("Entropy", value=0.5)

# Predict button
if st.button("Predict"):
    # Prepare data
    data = {
        "variance": variance,
        "skewness": skewness,
        "curtosis": curtosis,
        "entropy": entropy
    }

    # Make API request
    response = requests.get("http://localhost:8000/predict", params=data)
    prediction = response.text

    # Display prediction
    st.write(f"Prediction: {prediction}")

# Upload CSV file for batch prediction
st.header("Batch Prediction")
file = st.file_uploader("Upload a CSV file for batch prediction", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.write("Uploaded Data:")
    st.dataframe(df)

    if st.button("Predict Batch"):
        # Make API request
        response = requests.post("http://localhost:8000/predict_file", files={"file": file})
        predictions = response.text

        # Display predictions
        st.write("Batch Predictions:")
        st.write(predictions)
