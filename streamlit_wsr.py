# WSR Project 
import streamlit as st

st.title('WSR Reporting Tool')

#color = st.color_picker('Current Status of the project', '#00f900')


option = st.selectbox(
    'Please choose a project to view the details',
    ('MGM', 'Segdewick', 'Juvo'))

st.write('Client selected : ', option)

st.date_input('Project Start Date')

st.date_input('SOW End Date')


score = st.slider(' Status of the Project', 0, 100, 10)

