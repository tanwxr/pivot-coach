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

st.title("PivotCoach")
st.write("Your Career Transition Navigator")



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

## 📊 Data Sources

The insights in this app are built using Singapore career and skills data:

- **MyCareersFuture job listings**  
  Used to analyze current job demand, salary ranges, role popularity,
  and required skills across different career paths.

- **SkillsFuture course directory**  
  Used to identify available training opportunities and map courses
  to the skills needed for career transitions.

---

## 🧭 What can you do?

### 1. Career Gap Explorer

Understand the gap between your current role and your target role.

The tool compares:

- ✅ Skills you already have
- ⚠️ Skills you need to develop
- 💰 Current salary position versus target role salary range
- 📈 Job market demand for different roles

You can also ask an AI career coach to explain:
- How difficult your transition might be
- Which skills to prioritise
- Suggested learning pathways

---

### 2. AI Course Coach

Find relevant courses using AI-powered recommendations.

Instead of relying only on keyword matching, the course recommender uses
**embeddings** to understand the meaning behind skills and course content.

It helps answer questions like:

> "I am a Data Analyst. What courses can help me become a Data Engineer?"

The AI matches your career goals with relevant SkillsFuture courses based on
skills, course descriptions, and learning outcomes.

---

## 🎯 Goal

Turn job market data into actionable career guidance —
helping professionals understand **where they are, where they want to go,
and how to get there.**

"""
)

def load_data(nrows, url):
    data = pd.read_csv(url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000, './data/jobs.csv')
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! ")

if st.checkbox('Show raw data for jobs'):
    st.subheader('Raw data extracted from MyCareersFuture')
    st.write(data)



# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000, './data/courses.csv')
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! ")

if st.checkbox('Show raw data for courses'):
    st.subheader('Raw data extracted from SkillsFuture')
    st.write(data)