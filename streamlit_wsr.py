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

#if st.button('Save'):
 #   st.write('Updating the table with the changes')
#if st.button('Cancel'):
 #   st.write('No updates to the table')

#button_text = "Save", "Cancel"

#for text, col in zip(button_text, st.columns(len(button_text))):
#    if col.button(text):
 #       col.write(f"{text} clicked")

col1, col2 = st.columns([0.26,1])

with col1:
    st.button('Save')
with col2:
    st.button('Cancel')


