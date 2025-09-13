import streamlit as st
import pickle
import numpy as np

st.title("House Price Predictor!")

area = st.number_input("Enter the in sq ft", 500, 10000)
rooms = st.slider("Number of rooms", 1, 10)

model = pickle.load(open("house_price_model.pkl", "rb"))
if st.button("Predict Price"):
    features = np.array([[area, rooms]])
    prediction = model.predict(features)

    st.subheader(f"Predicted Price: ${prediction[0]:,.2f}")