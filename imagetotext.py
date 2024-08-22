import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

heading_color = "#155461"
st.markdown(f"<h1 style='text-align: center; color: {heading_color};'>Welcome to Text Generation Application based on Image</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: {heading_color};'>Will Explore the Meaning in the image......</h3>", unsafe_allow_html=True)


def query(file):
    data = file.read()  
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

uploaded_file = st.file_uploader("Upload an image", type='jpg')

if uploaded_file is not None:
    output = query(uploaded_file) 
    st.write(output) 
