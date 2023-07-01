# WSR Project 
import streamlit as st
#import snowflake.connector

st.title('WSR Reporting Tool')

#color = st.color_picker('Current Status of the project', '#00f900')


option = st.selectbox(
    'Client & Project',
    ('MGM', 'Segdewick', 'Juvo'))

st.write('Client selected : ', option)

st.date_input('SOW Start Date')

st.date_input('SOW End Date')

#st.image()
#st.image()

st.write('WSR STATUS : ', 'GREEN')

st.date_input('WSR End Date')

score = st.slider(' Status of the Project', 0, 100, 10)

if st.button('Save'):
    st.write('Updating the table with the changes')
if st.button('Cancel'):
    st.write('No updates to the table')

