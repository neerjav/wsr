# WSR Project 
import streamlit as st

st.title('WSR Reporting Tool')

#color = st.color_picker('Current Status of the project', '#00f900')


option = st.selectbox(
    'Please choose a project to view the details',
    ('MGM', 'Segdewick', 'Juvo'))

st.date_input('Project Start Date')

st.date_input('SOW End Date')


score = st.slider('Please specify your test score', 0, 100, 10)
st.write("My test score is ", score)

