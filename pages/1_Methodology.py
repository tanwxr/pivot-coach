import streamlit as st
import pandas as pd

st.title("📚 Methodology")

st.write(
"""
This page explains the data pipeline, machine learning approach,
and AI architecture behind Pivot Coach.
"""
)


st.header("1. Data Collection & Preparation")

st.markdown(
"""
The application uses two main datasets:

### Job Market Dataset
Source:
- Job listings collected from public job portals
- Contains job titles, employers, salary ranges, descriptions and skills

Processing:
1. Clean job titles
2. Standardise job families
3. Aggregate similar roles
4. Extract common skills
5. Calculate salary ranges

Output:
- Normalised role profiles
- Skill distributions
- Salary benchmarks

### Course Dataset
Source:
- Online learning course catalogue

Processing:
1. Clean course metadata
2. Extract course skills
3. Standardise provider and fee information

Output:
- Course documents used for semantic recommendation
"""
)

st.image(
    "assets/career_advice_flowchart.png",
    caption="Career Gap Explorer workflow",
    use_container_width=True
)



###

# Use Case 2: AI Career Coach

### 

st.header("🤖 Use Case 2: AI Career Coach")

st.markdown(
"""
### Objective

Provide personalised career recommendations by matching
a user's experience with possible career paths and courses.

### Approach

The application uses Retrieval Augmented Generation (RAG).

Instead of asking an LLM to answer from memory:

1. User input is converted into an embedding.

2. The embedding is compared against:
   - Job role embeddings
   - Course embeddings

3. The closest matches are retrieved.

4. Retrieved information is passed to GPT.

5. GPT generates grounded career advice.
"""
)
st.image(
    "assets/career_coach_rag_flowchart.png",
    caption="AI coach workflow",
    use_container_width=True
)

st.header("⚙️ Technical Architecture")

st.markdown(
"""
### Technologies Used

| Component | Technology |
|---|---|
| Data Processing | Python, Pandas |
| Similarity Search | Cosine Similarity |
| Embeddings | OpenAI text-embedding-3-small |
| LLM Explanation | GPT-4.1-mini |
| Application | Streamlit |
| Deployment | Streamlit Cloud |
| Version Control | GitHub |

### Embedding Strategy

Job roles and courses are converted into numerical vectors once.

These vectors are stored locally as pickle files:

- role_embeddings.pkl
- course_embeddings.pkl

During user interaction:
- Only the user's query is embedded
- Existing vectors are reused
- Retrieved documents are sent to GPT
"""
)

st.image(
    "assets/rag_pipeline_five_stages.png",
    caption="RAG Pipeline",
    use_container_width=True
)


st.markdown(
"""
---

### Preview raw data below:

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