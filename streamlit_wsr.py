# WSR Project 
import streamlit as st

st.header('WSR Report')



score = st.slider('Please specify your test score', 0, 100, 10)
st.write("My test score is ", score)
