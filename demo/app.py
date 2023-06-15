import streamlit as st
import pandas as pd
import random

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

# Read and display HTML
with open('index.html', 'r') as f:
    html_string = f.read()
st.markdown(html_string, unsafe_allow_html=True)

# Create and display a simple DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [23, 78, 22, 19],
    'Country': ['USA', 'Sweden', 'Canada', 'Germany']
}
df = pd.DataFrame(data)
st.dataframe(df)
