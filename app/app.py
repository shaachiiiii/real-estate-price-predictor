import streamlit as st
import joblib
import numpy as np

# Load the trained model from same folder
model = joblib.load("model.pkl")

# App title
st.title("Chennai House Price Predictor")

# Input fields
int_sqft = st.number_input("Interior Area (in sqft):", min_value=500, max_value=3000, value=1000)
n_bedroom = st.number_input("Number of Bedrooms:", min_value=1, max_value=5, value=2)
n_bathroom = st.number_input("Number of Bathrooms:", min_value=1, max_value=3, value=2)
n_room = st.number_input("Total Rooms:", min_value=2, max_value=10, value=4)
dist_mainroad = st.slider("Distance from Main Road (in meters):", 0, 200, 50)

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[int_sqft, n_bedroom, n_bathroom, n_room, dist_mainroad]])
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹ {int(prediction[0]):,}")