import streamlit as st
from retriever import run_qa

st.set_page_config(page_title="Ask a Question", layout="centered")
st.markdown("⬅️ [Back to Dashboard](http://localhost:8000/index.html)", unsafe_allow_html=True)

st.title("5. Ask a Question from Text 🧠")

context = st.text_area("Paste input text (context):")
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if context and question:
        answer = run_qa(context, question)
        st.success(answer)
