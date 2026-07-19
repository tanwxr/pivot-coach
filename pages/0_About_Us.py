import streamlit as st

st.title("About Us")

st.markdown(
'''
## 🌏 Project Scope

Pivot Coach is an AI-powered career guidance application designed to help
professionals understand career opportunities, identify skill gaps, and
discover relevant learning pathways.

The project focuses on the Singapore job market by combining:
- Job market intelligence from real job listings
- Skills analysis across career roles
- Training recommendations from available courses
- Generative AI explanations to provide personalised guidance

The application contains two main use cases:

1. **Career Gap Explorer**  
   Helps users compare their current role against a target career path.

2. **AI Career Coach**  
   Uses semantic search and AI recommendations to suggest suitable career
   pathways and learning opportunities.

---

## 🎯 Objectives

The objectives of Pivot Coach are to:

- Help users understand how their current skills compare against target roles
- Identify missing skills required for career transitions
- Provide visibility into salary ranges and job demand
- Recommend relevant courses to support upskilling
- Demonstrate how AI techniques such as embeddings and large language models
  can improve career decision-making

---

## 📊 Data Sources

The insights in this application are built using Singapore career and skills
data from two main sources:

### MyCareersFuture Job Listings

Used to analyse:

- Current job market demand
- Popular career roles
- Salary ranges
- Required skills
- Employer demand

The job data is cleaned and aggregated to create role profiles containing:
- Standardised job titles
- Common skills
- Salary benchmarks
- Hiring activity indicators

---

### SkillsFuture Course Directory

Used to identify available learning opportunities and connect courses with
career transition pathways.

Course information includes:

- Course titles
- Skills covered
- Training providers
- Course information and descriptions

This dataset supports AI-powered course recommendations.

---

## 🚀 Features

### 1. Career Gap Explorer

Understand the distance between your current role and your desired career.

The tool compares:

- ✅ Skills you already have
- ⚠️ Skills you need to develop
- 💰 Your salary position compared against the target role range
- 📈 Market demand for different roles

An AI explanation layer provides additional guidance by explaining:

- How suitable the transition may be
- Which skills should be prioritised
- Suggested next steps

---

### 2. AI Career Coach

Receive personalised career recommendations through AI.

The AI Career Coach uses **embeddings and semantic search** to understand
the relationship between:

- User experience
- Job roles
- Required skills
- Available courses

Instead of relying only on keyword matching, the system retrieves
semantically similar career paths and courses before generating AI advice.

Example:

> "I am a Data Analyst. What should I learn to become a Data Engineer?"

The AI recommends suitable pathways based on market data and available
training options.

---

## 💡 Project Vision

Pivot Coach transforms complex job market information into actionable career
guidance.

By combining data analytics, embeddings, and generative AI, the application
helps users answer three key questions:

**Where am I now?**  
→ Understand current skills and career position.

**Where can I go?**  
→ Explore possible career pathways.

**How do I get there?**  
→ Discover skills and courses needed for progression.

'''
)