import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI


# -----------------------
# LOAD EMBEDDINGS
# -----------------------

with open("data/role_embeddings.pkl", "rb") as f:
    job_data = pickle.load(f)

with open("data/course_embeddings.pkl", "rb") as f:
    course_data = pickle.load(f)


job_vectors = job_data["vectors"]
job_documents = job_data["documents"]

course_vectors = course_data["vectors"]
course_documents = course_data["documents"]


# -----------------------
# OPENAI
# -----------------------

client = OpenAI(
    api_key=st.secrets["MY_API_KEY"]
)


# -----------------------
# SEMANTIC SEARCH
# -----------------------

def semantic_search(query_embedding, vectors, documents, top_k=5):

    scores = cosine_similarity(
        [query_embedding],
        vectors
    )[0]

    indices = scores.argsort()[-top_k:][::-1]

    results = []

    for i in indices:
        results.append(
            {
                "score": scores[i],
                "document": documents[i]
            }
        )

    return results



# -----------------------
# UI
# -----------------------

st.title("🤖 AI Career Coach")


st.write(
    """
Tell me about your current experience, skills, 
and the career direction you are considering.

The AI Coach will:
- analyse suitable career paths from real job listings
- identify skill gaps
- recommend courses to close those gaps
"""
)


user_input = st.text_area(
    "Your career situation",
    placeholder="Example: I am a Data Analyst with SQL experience and want to move into Data Engineering"
)



if st.button("🚀 Find my career path"):


    # -----------------------
    # 1. Embed user input
    # -----------------------

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=user_input
    )

    query_embedding = response.data[0].embedding



    # -----------------------
    # 2. Search job database
    # -----------------------

    job_matches = semantic_search(
        query_embedding,
        job_vectors,
        job_documents,
        top_k=5
    )


    # -----------------------
    # 3. Search course database
    # -----------------------

    course_matches = semantic_search(
        query_embedding,
        course_vectors,
        course_documents,
        top_k=5
    )



    # -----------------------
    # DISPLAY RESULTS
    # -----------------------

    st.subheader("💼 Possible Career Paths")

    for match in job_matches:

        st.markdown(
            f"""
**Similarity score:** {match['score']:.2f}

{match['document']}
"""
        )



    st.subheader("📚 Recommended Learning Options")

    for match in course_matches:

        st.markdown(
            f"""
**Similarity score:** {match['score']:.2f}

{match['document']}
"""
        )



    # -----------------------
    # 4. GPT Career Coach
    # -----------------------

    job_context = "\n\n".join(
        [
            x["document"]
            for x in job_matches
        ]
    )

    course_context = "\n\n".join(
        [
            x["document"]
            for x in course_matches
        ]
    )


    prompt = f"""
You are an AI career coach.

User situation:
{user_input}


Relevant job market information:
{job_context}


Relevant courses:
{course_context}


Provide advice:

1. What career paths fit this person?
2. Why are these roles suitable?
3. What skills are missing?
4. Which courses should they take first?
5. Give a realistic transition roadmap.
"""


    answer = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    st.subheader("🧠 AI Career Advice")

    st.write(
        answer.choices[0].message.content
    )