import streamlit as st
import pandas as pd
import numpy as np

st.title("PivotCoach")
st.write("Your Career Transition Navigator")


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