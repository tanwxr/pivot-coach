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
    
"""
)
