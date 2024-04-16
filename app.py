import streamlit as st 
import pandas as pd
st.markdown("<h1 style='color: blue;'> Customer Analysis Dataset</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='color: white;'>View the dataset of clothing retail reviews </h4>", unsafe_allow_html=True)
if st.button("See the dataset"):
    df=pd.read_csv("data.csv")
    st.write(df)