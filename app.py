import streamlit as st
import pickle
import numpy as np

# Page Config
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Load Model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Custom CSS Styling
st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 40px !important;
    font-weight: 900;
    color: #4CAF50;
    margin-top: 30px;
    margin-bottom: 20px;
}

.subtitle {
    text-align:center;
    font-size:18px;
    margin-bottom:30px;
}

.result {
    font-size:26px;
    font-weight:bold;
    color:#00ff9d;
    text-align:center;
}

.footer {
    text-align:center;
    margin-top:40px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<p class="main-title">🏠 House Price Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Predict house price using Square Footage, Bedrooms and Bathrooms</p>', unsafe_allow_html=True)

# Input Section
st.markdown('<div class="card">', unsafe_allow_html=True)

square_footage = st.slider(
    "Square Footage",
    500, 5000, 1800
)

bedrooms = st.slider(
    "Number of Bedrooms",
    1, 6, 3
)

bathrooms = st.slider(
    "Number of Bathrooms",
    1, 5, 2
)

predict_button = st.button("Predict Price")

st.markdown('</div>', unsafe_allow_html=True)

# Prediction
if predict_button:

    features = np.array([[square_footage, bedrooms, bathrooms]])

    prediction = model.predict(features)

    st.markdown(
        f'<p class="result">Predicted House Price: ${prediction[0]:,.2f}</p>',
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    '<p class="footer">Built with ❤️ using Streamlit | Machine Learning Project</p>',
    unsafe_allow_html=True
)