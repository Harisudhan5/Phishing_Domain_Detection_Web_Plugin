import streamlit as st
import pickle
import numpy as np
from App.FeatureExtraction import FeatureExtraction

def process_url(url):
    with open('C://Projects//Phishing_Domain_Detection_Web_Extension//Model//phish.pkl', 'rb') as file:
        gbc = pickle.load(file)
        url = str(url)
        ul = FeatureExtraction(url)
        x = np.array(ul.getFeaturesList()).reshape(1,30) 
        y_pred =gbc.predict(x)[0]
        return y_pred



# Centered title
st.markdown("<h1 style='text-align: center;'>WebGuardian</h1>", unsafe_allow_html=True)

# Text input box for URL with "Enter the URL" text
url = st.text_input('Enter the URL:')

# Button for checking URL
if st.button('Check URL'):
    # Placeholder for URL checking functionality
    if url == 'Enter the URL':
        st.write('Please enter a URL.')
    else:
        res = process_url(url)
        text = ""
        if res == 1:text = "Safe"
        else:text = "Not Safe"
        st.text ('The Website is', text)
        # Add your URL checking functionality here

# Button for analyzing website
if st.button('Analyze Website'):
    # Placeholder for website analysis functionality
    st.write('Analyzing website:', url)
