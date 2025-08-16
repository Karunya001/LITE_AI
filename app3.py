# 📄 app3.py - News Summarization
import streamlit as st
from retriever import summarize_news

st.set_page_config(page_title="News Summarization", layout="centered")
st.markdown("⬅️ [Back to Dashboard](http://localhost:8000/index.html)", unsafe_allow_html=True)

st.title("3. News Headlines / Editorial Summarization 🗞️")

text = st.text_area("Paste news editorial or headlines")
if st.button("Summarize News"):
    if text:
        summary = summarize_news(text)
        st.success(summary)
