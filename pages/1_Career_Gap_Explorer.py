import streamlit as st
import pandas as pd
from rapidfuzz import process, fuzz

# -----------------------
# LOAD DATA
# -----------------------
jobs = pd.read_csv("data/jobs.csv")

# -----------------------
# CANONICAL ROLES
# -----------------------
canonical_roles = [
    "data engineer",
    "data analyst",
    "cybersecurity analyst",
    "product manager",
    "accountant"
]

def standardise_role(role):
    role = role.lower().strip()

    match = process.extractOne(
        role,
        canonical_roles,
        scorer=fuzz.token_sort_ratio
    )

    if match[1] >= 80:
        return match[0]

    return role

# -----------------------
# CLEAN ROLE
# -----------------------
jobs["role_clean"] = jobs["title"].apply(standardise_role)

# -----------------------
# REMOVE DUPLICATES
# -----------------------
jobs = jobs.drop_duplicates(subset=["role_clean", "skills"])

# -----------------------
# CLEAN SKILLS
# -----------------------
jobs["skills"] = (
    jobs["skills"]
    .str.lower()
    .str.split(",")
)

jobs["skills"] = jobs["skills"].apply(
    lambda x: [s.strip() for s in x if s and s.strip()]
)

# -----------------------
# MERGE SKILLS PER ROLE
# -----------------------
def merge_skills(series):
    all_skills = []
    for skills in series:
        all_skills.extend(skills)
    return sorted(set(all_skills))

df_merged = (
    jobs.groupby("role_clean")["skills"]
    .apply(merge_skills)
    .reset_index()
)

# -----------------------
# STREAMLIT UI
# -----------------------
st.title("Career Gap Explorer")

roles = df_merged["role_clean"].tolist()

current_role = st.selectbox("Current Role", roles)
target_role = st.selectbox("Target Role", roles)

# -----------------------
# SKILL LOOKUP
# -----------------------
def get_skills(role):
    return set(
        df_merged[df_merged["role_clean"] == role]["skills"].values[0]
    )

current_skills = get_skills(current_role)
target_skills = get_skills(target_role)

missing_skills = target_skills - current_skills
common_skills = target_skills & current_skills

# Make Skill Cards
st.subheader("Skills you already have")

for skill in sorted(common_skills):
    st.markdown(
        f"""
        <div style="
            padding:10px;
            margin:5px 0px;
            border-radius:8px;
            background-color:#e6f4ea;
            color:#1e4620;
            font-weight:500;
        ">
        ✔ {skill}
        </div>
        """,
        unsafe_allow_html=True
    )

st.subheader("Skills to learn")

for skill in sorted(missing_skills):
    st.markdown(
        f"""
        <div style="
            padding:10px;
            margin:5px 0px;
            border-radius:8px;
            background-color:#fdecea;
            color:#611a15;
            font-weight:500;
        ">
        ⚠ {skill}
        </div>
        """,
        unsafe_allow_html=True
    )