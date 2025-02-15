import streamlit as st
import requests
import pandas as pd

# Set the title of the Streamlit app
st.title("Tech Stack Portfolio")

# Fetch data from the FastAPI backend
@st.cache
def fetch_tech_stack():
    response = requests.get("http://localhost:8000/api/v1/tech-stack")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data from the API.")
        return []

# Display the tech stack data
tech_stack_data = fetch_tech_stack()

if tech_stack_data:
    df = pd.DataFrame(tech_stack_data)
    st.write(df)

# Add a sidebar for user input
st.sidebar.header("User Input")

# Example input field
user_input = st.sidebar.text_input("Enter a technology or skill:")

if user_input:
    st.sidebar.write(f"You entered: {user_input}")