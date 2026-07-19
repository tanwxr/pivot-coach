import streamlit as st
import pandas as pd
import ast

# -----------------------
# LOAD DATA
# -----------------------
jobs = pd.read_csv("data/jobs_clean.csv")

jobs["skills"] = jobs["skills"].apply(ast.literal_eval)



# -----------------------
# STREAMLIT UI
# -----------------------
st.title("Career Gap Explorer")

roles = jobs["title_clean"].tolist()

roles = (
    jobs[jobs["job_count"] >= 2]
    .sort_values(
        "job_count",
        ascending=False
    )["title_clean"]
    .tolist()
)


current_role = st.selectbox("Current Role", roles)
target_role = st.selectbox("Target Role", roles)


# -----------------------
# SALARY COMPARISON
# -----------------------

st.subheader("Salary Comparison")
current_salary = st.number_input(
    "Your current monthly salary",
    min_value=0,
    value=5000,
    step=200
)

target_row = jobs[jobs["title_clean"] == target_role].iloc[0]

target_min = target_row["salary_min"]
target_max = target_row["salary_max"]

st.metric(
    label=f"Typical salary range: {target_role}",
    value=f"${target_min:,.0f} - ${target_max:,.0f}"
)

salary_progress = min(
    current_salary / target_max,
    1.0
)

salary_pct = (
    (current_salary - target_min)
    / (target_max - target_min)
)

salary_pct = max(0, min(salary_pct, 1))

st.progress(salary_pct)

if current_salary < target_min:
    st.warning("Below the typical salary range")

elif current_salary > target_max:
    st.success("Above the typical salary range")

else:
    st.success("Within the typical salary range")



# -----------------------
# SKILL LOOKUP
# -----------------------
def get_skills(role):
    return set(
        jobs[jobs["title_clean"] == role]["skills"].values[0]
    )

current_skills = get_skills(current_role)
target_skills = get_skills(target_role)

missing_skills = target_skills - current_skills
common_skills = target_skills & current_skills


# -----------------------
# LLM Explainer
# -----------------------
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["MY_API_KEY"]
)

prompt = f"""
Current role: {current_role}

Target role: {target_role}

Skills already possessed:
{', '.join(common_skills)}

Missing skills:
{', '.join(missing_skills)}

Provide:
1. Difficulty of transition
2. Recommended learning order
"""

st.info(
    "🤖 Want a personalised explanation of your career move? "
    "Ask the AI Career Coach below!"
)


if st.button("✨ Explain my career transition"):

    with st.spinner("Analyzing transition..."):

        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.markdown(response.choices[0].message.content)


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