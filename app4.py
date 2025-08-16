# 📄 app4.py - Grammar Correction
import streamlit as st
from summarizer import grammar_corrector

st.set_page_config(page_title="Grammar Correction", layout="centered")
st.markdown("⬅️ [Back to Dashboard](http://localhost:8000/index.html)", unsafe_allow_html=True)

st.title("4. Grammar Correction ✍️")

text = st.text_area("Paste text to correct")
if st.button("Correct Grammar"):
    if text:
        corrected = grammar_corrector(text)
        st.success(corrected)