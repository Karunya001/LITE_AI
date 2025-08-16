# 📄 app2.py - Science & Technology Summarization (Text + File Upload)

from retriever import summarize_science_doc
import docx2txt
import PyPDF2
import streamlit as st

st.set_page_config(page_title="Science & Tech Summarization", layout="centered")
st.markdown("⬅️ [Back to Dashboard](http://localhost:8000/index.html)", unsafe_allow_html=True)

st.title("2. Science & Technology Document Summarization 🔬")

# Option 1: Text Box
st.markdown("### 🔹 Option 1: Paste Science/Tech Text")
text = st.text_area("Paste science/tech article here")

if st.button("Summarize Pasted Text"):
    if text:
        st.info("🔄 Generating summary...")
        with st.spinner("Working..."):
            summary = summarize_science_doc(text[:1500])  # limit for stability
        st.success(summary)

# Option 2: Upload File
st.markdown("### 🔹 Option 2: Upload a Science/Tech Document")
uploaded_file = st.file_uploader("Upload .pdf, .docx, or .txt file", type=["pdf", "docx", "txt"])

if uploaded_file:
    file_text = ""
    try:
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                file_text += page.extract_text()

        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            file_text = docx2txt.process(uploaded_file)

        elif uploaded_file.type == "text/plain":
            file_text = uploaded_file.read().decode("utf-8")

    except Exception as e:
        st.error("⚠️ Error reading file: " + str(e))

    if file_text:
        st.success("✅ File loaded successfully.")
        st.text(f"Document length: {len(file_text)} characters")

        if st.button("Summarize Uploaded Document"):
            st.info("🔄 Generating summary...")
            with st.spinner("Summarizing document..."):
                trimmed_text = file_text[:1500]  # limit to prevent lag/freeze
                summary = summarize_science_doc(trimmed_text)
            st.success(summary)
