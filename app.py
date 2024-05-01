import streamlit as st
import pickle
import whois
import numpy as np
from App.FeatureExtraction import FeatureExtraction

def process_url(url):
    with open('C://Projects//Phishing_Domain_Detection_Web_Extension//Model//phish.pkl', 'rb') as file:
        gbc = pickle.load(file)
        ul = FeatureExtraction(url)
        x = np.array(ul.getFeaturesList()).reshape(1,30) 
        y_pred = gbc.predict(x)[0]
        return y_pred

def dns_info(url):
    res = whois.whois(url)
    domain_name = res.domain_name
    regisetrar = res.registrar
    updated_date = res.updated_date
    creation_date = res.creation_date
    expiration_date = res.expiration_date
    name_servers = res.name_servers
    status = res.status
    organization = res.org
    country = res.country
    dnssec = res.dnssec
    email = res.emails
    dns_inf = [domain_name, regisetrar, updated_date, creation_date, expiration_date, name_servers, status, organization, country, dnssec, email]
    return dns_inf

st.markdown("<h1 style='text-align: center;'>WebGuardian</h1>", unsafe_allow_html=True)

url = st.text_input('Enter the URL:')

if st.button('Check URL'):
    # Placeholder for URL checking functionality
    text = " "
    if url == 'Enter the URL':
        st.write('Please enter a URL.')
    else:
        with st.spinner('Checking URL...'):
            res = process_url(url)
            if res == 1:
                text = "Safe"
            else:
                text = "Unsafe"
            st.text('The Website is ' + text)

if st.button('Analyze Website'):
    with st.spinner('The website is being scanned'):
        dnsl = dns_info(url)
        st.write('Domain Name : ', dnsl[0])
        st.write('Registered Name : ', dnsl[1])
        st.write('Updated Date : ', dnsl[2])
        st.write('Creation Data : ', dnsl[3])
        st.write('Expiration Date : ', dnsl[4])
        st.write('Name Servers : ', dnsl[5])
        st.write('Status Info : ', dnsl[6])
        st.write('Organization : ', dnsl[7])
        st.write('Country : ', dnsl[8])
        st.write('DNSSEC : ', dnsl[9])
        st.write('Email : ', dnsl[10])
