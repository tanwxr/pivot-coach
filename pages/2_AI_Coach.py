import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

# -----------------------
# LOAD DATA
# -----------------------

with open("embeddings/roles_embeddings.pkl", "rb") as f:
    data = pickle.load(f)

vectors = data["vectors"]
documents = data["documents"]
roles = data["roles"]


# -----------------------
# OPENAI
# -----------------------

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)


# -----------------------
# SEARCH FUNCTION
# -----------------------

def search_roles(query_embedding, top_k=5):

    scores = cosine_similarity(
        [query_embedding],
        embeddings
    )[0]

    indices = scores.argsort()[-top_k:][::-1]

    results = []

    for i in indices:
        results.append({
            "role": roles[i],
            "score": scores[i],
            "document": documents[i]
        })

    return results



# -----------------------
# UI
# -----------------------

st.title("🤖 AI Career Coach")

st.write(
    """
Tell me about your current skills, experience, 
and the kind of career move you want to make.
(Some examples of roles the model has learned are: Data Analyst, Data Scientist)
"""
)


user_input = st.text_area(
    "Your situation"
)


if st.button("Find my career paths"):

    # 1. Embed user question

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=user_input
    )

    query_embedding = response.data[0].embedding


    # 2. Retrieve roles

    matches = search_roles(query_embedding)


    st.subheader("Closest career paths")


    for match in matches:
        st.write(
            f"**{match['role']}** "
            f"(similarity: {match['score']:.2f})"
        )


    # 3. GPT explanation

    context = "\n\n".join(
        [
            m["document"]
            for m in matches
        ]
    )


    prompt = f"""
You are a career coach.

User:
{user_input}


Possible career paths:
{context}


Explain:
1. Which paths fit best
2. Why
3. What skills are missing
4. Suggested next steps
"""


    answer = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )


    st.subheader("Career advice")

    st.write(
        answer.choices[0].message.content
    )