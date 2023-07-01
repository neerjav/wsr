# WSR Project 
import streamlit as st
#import snowflake.connectory 
import pandas as pd
import numpy as np

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
   
st.title('WSR Reporting Tool')

#color = st.color_picker('Current Status of the project', '#00f900')

col1, col2, col3 = st.columns(3)
with col1:
   option = st.selectbox(
    'Client & Project',
    ('MGM', 'Segdewick', 'Juvo'))

   st.date_input('SOW Start Date')

   st.date_input('SOW End Date')

with col2:
   st.image("https://static.wixstatic.com/media/b75d87_9ec065c9fb634ed2a8a1f636c53524e0~mv2.png/v1/fill/w_1000,h_1000,al_c/b75d87_9ec065c9fb634ed2a8a1f636c53524e0~mv2.png")

with col3:
   st.date_input('WSR End Date')
   st.write('WSR STATUS : ', 'GREEN')

col1, col2 = st.columns(2)

with col1:
   st.slider(' Status of the Project', 0, 100, 10)
with col2:
   st.text_input(
        "Team Details",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder='Enter the team info',)

col1, col2 = st.columns(2)

with col1:
   st.text_input(
        "Engagement Summary",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder='Please enter the summary of the project',)
with col2:
   st.text_input(
        "Tech Stack",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder='Enter the tech stack used',)

#if st.button('Save'):
 #   st.write('Updating the table with the changes')
#if st.button('Cancel'):
 #   st.write('No updates to the table')

#button_text = "Save", "Cancel"

#for text, col in zip(button_text, st.columns(len(button_text))):
#    if col.button(text):
 #       col.write(f"{text} clicked")

col1, col2 = st.columns([0.12,1])

with col1:
    st.button('Save')
with col2:
    st.button('Cancel')

st.header('Key Accomplishments of the Week')

#creating a sample dataframe 

df = pd.DataFrame(

    np.random.randn(7, 5),

    columns=('col %d' % i for i in range(3)))



#displaying the dataframe in a static manner

st.table(df)


