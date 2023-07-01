# WSR Project 
import streamlit as st

st.header('WSR Report')

color = st.color_picker('Pick A Color', '#00f900')

option = st.selectbox(
    'Please choose a project to view the details',
    ('MGM', 'Segdewick', 'Juvo'))


score = st.slider('Please specify your test score', 0, 100, 10)
st.write("My test score is ", score)

st.balloons()

st.image('/')
