import streamlit as st

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

st.markdown(
"""
```mermaid
flowchart TD

A[User selects current and target role]
--> B[Retrieve role profiles]

B --> C[Compare skills]

C --> D[Identify existing skills]
C --> E[Identify missing skills]

B --> F[Retrieve salary range]

D --> G[Generate career summary]
E --> G

G --> H[GPT explanation]
H --> I[Display career advice]

""",
unsafe_allow_html=True
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

st.markdown(
"""
```mermaid
flowchart TD

A[User describes experience and goals]

A --> B[Create embedding using OpenAI Embeddings]

B --> C[Semantic similarity search]

C --> D[Retrieve matching job roles]

C --> E[Retrieve relevant courses]

D --> F[Combine retrieved context]
E --> F

F --> G[GPT Career Coach]

G --> H[Personalised recommendations]

""",
unsafe_allow_html=True
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