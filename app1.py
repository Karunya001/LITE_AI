import streamlit as st
from summarizer import generate_summary

# ✅ Configure Streamlit page
st.set_page_config(page_title="Text Summarization", layout="centered")

# 🔙 Back to dashboard link
st.markdown("⬅️ [Back to Dashboard](http://localhost:8000/index.html)", unsafe_allow_html=True)

# 🧠 App Title
st.title("1. General Text Summarization 🧠")

# 📥 Text input area
text = st.text_area("Enter the text you want to summarize:", height=250)

# 🛠️ Custom instruction input
instruction = st.text_input(
    "✏️ Custom summarization instruction (optional)",
    placeholder="e.g., In bullet points, 3-line summary, poetic tone, etc."
)

# ▶️ Summarization trigger
if st.button("Summarize"):
    if text:
        prompt = instruction.strip() if instruction.strip() else "Summarize the text"
        summary = generate_summary(text, prompt)
        st.subheader("📝 Summary Output")
        st.success(summary)
    else:
        st.warning("⚠️ Please enter text to summarize.")
