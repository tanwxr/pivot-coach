import streamlit as st

st.title("About Us")

st.markdown(
'''
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
'''
)