import streamlit as st
import pandas as pd
import random
import plotly.express as px
import matplotlib as plt



# Text input for name
chart_title= st.text_input('Chart title')

# Button to scramble name
if st.button('Scramble me mucka'):
    chart_title= list(chart_title)  # Convert string to list
    random.shuffle(chart_title)  # Shuffle list
    chart_title= ''.join(chart_title)  # Convert list back to string
    st.write(f'Hello, {chart_title}!')
    
uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False, type=['png', 'jpg', 'csv', 'xlsx'])

if uploaded_file:
    st.write("filename:", uploaded_file.name)

    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    with st.sidebar:
        option1 = st.sidebar.selectbox(
        'What Category...',
        (df['category'].unique()))

    df = df[df['category'] == option1]
 
    with st.sidebar:
        option2 = st.sidebar.selectbox(
        'What Category_type...',
        (df['category_type'].unique()))

    df = df[df['category_type'] == option2]


    fig = px.line(df, x='time_period', y='number', title = chart_title)
    st.plotly_chart(fig)
