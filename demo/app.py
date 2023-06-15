import streamlit as st
import pandas as pd
import random
import plotly.express as px
import matplotlib as plt

# Set title
st.title('Hello, world!')

# Text input for name
name = st.text_input('Your name')

# Button to scramble name
if st.button('Scramble me mucka'):
    name = list(name)  # Convert string to list
    random.shuffle(name)  # Shuffle list
    name = ''.join(name)  # Convert list back to string
    st.write(f'Hello, {name}!')
    
uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True, type=['png', 'jpg', 'csv', 'xlsx'])

if uploaded_files:
    st.write("filename:", uploaded_file.name)

# Create and display a simple DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [23, 78, 22, 19],
    'Country': ['USA', 'Sweden', 'Canada', 'Germany']
}
df = pd.DataFrame(data)
st.dataframe(df) 
