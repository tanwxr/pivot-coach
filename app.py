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


st.info(
"""
IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalised advice.)
""")



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
    
"""
)
