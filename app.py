import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and analyze your skills.")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "txt"]
)

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

    st.write("### File Information")
    st.write("File name:", uploaded_file.name)
    st.write("File size:", uploaded_file.size, "bytes")

    st.info("Resume analysis will be added next.")
