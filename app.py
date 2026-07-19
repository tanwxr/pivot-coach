import streamlit as st
import pandas as pd
import numpy as np

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MY_API_KEY") or st.secrets["MY_API_KEY"]

st.set_page_config(
    page_title="Pivot Coach",
    page_icon="🚀"
)

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

st.title("🚀 Pivot Coach")

st.markdown(
"""
## Navigate your next career move with data and AI

Pivot Coach helps you understand where you stand in the job market and
discover practical pathways to your next role.

This tool combines real-world job market data with AI-powered analysis to
help you make more informed career decisions.

---

## 🔗 Project Repository

View the source code and documentation here:

[GitHub Repository](https://github.com/tanwxr/pivot-coach)
    

---

### Preview Raw Data Below

"""
)


def load_data(nrows, url):
    data = pd.read_csv(url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading jobs data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000, './data/jobs.csv')
# Notify the reader that the data was successfully loaded.
data_load_state.text("Jobs Data Loaded! ")

if st.checkbox('Show raw data for jobs'):
    st.subheader('Raw data extracted from MyCareersFuture')
    st.write(data)



# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading course data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000, './data/courses.csv')
# Notify the reader that the data was successfully loaded.
data_load_state.text("Course Data Loaded! ")

if st.checkbox('Show raw data for courses'):
    st.subheader('Raw data extracted from SkillsFuture')
    st.write(data)