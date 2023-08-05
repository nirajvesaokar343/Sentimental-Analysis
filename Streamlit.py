import subprocess
subprocess.call("pip install nltk", shell=True)

import streamlit as st
import pandas as pd
import nltk
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score

# Rest of your Streamlit code...


st.title('Amazon Alexa Sentiment Analysis')

# Load your preprocessed dataset here
df = pd.read_csv('amazon_alexa.csv')

# ... Code for preprocessing and model training ...

# Define the Streamlit app interface
st.subheader('Enter a review:')
user_input = st.text_input('')

if st.button('Analyze Sentiment'):
    # ... Code to preprocess user input and make predictions ...

    st.subheader('Prediction:')
    if prediction == 1:
        st.write('Positive sentiment')
    else:
        st.write('Negative sentiment')
