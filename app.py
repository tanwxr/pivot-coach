import streamlit as st

st.title("PivotCoach")
st.write("Your Career Transition Navigator")


page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Career Gap Explorer", "AI Coach"]
)