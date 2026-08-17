import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and extract the text automatically.")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    st.subheader("📋 Extracted Resume Text")

    if resume_text:
        st.text_area(
            "Resume content",
            resume_text,
            height=400
        )
    else:
        st.warning("Could not extract text from this PDF.")
