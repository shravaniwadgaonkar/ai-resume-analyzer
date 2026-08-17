import streamlit as st
from pypdf import PdfReader
import re

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")

# Upload resume
uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

# Job description
job_description = st.text_area(
    "Paste the job description here",
    height=200
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    st.subheader("📋 Resume Preview")

    st.text_area(
        "Extracted text",
        resume_text,
        height=300
    )

    if job_description:

        # Convert everything to lowercase
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()

        # Skills to check
        skills = [
            "python",
            "sql",
            "machine learning",
            "deep learning",
            "pandas",
            "numpy",
            "scikit-learn",
            "tensorflow",
            "pytorch",
            "data analysis",
            "statistics",
            "git",
            "github",
            "streamlit",
            "aws",
            "docker"
        ]

        resume_skills = []
        missing_skills = []

        for skill in skills:

            if re.search(r"\b" + re.escape(skill) + r"\b", resume_lower):
                resume_skills.append(skill)

            elif re.search(r"\b" + re.escape(skill) + r"\b", job_lower):
                missing_skills.append(skill)

        # Calculate match
        required_skills = [
            skill for skill in skills
            if re.search(r"\b" + re.escape(skill) + r"\b", job_lower)
        ]

        if required_skills:

            matched_skills = [
                skill for skill in required_skills
                if skill in resume_skills
            ]

            score = (
                len(matched_skills)
                / len(required_skills)
            ) * 100

        else:
            score = 0

        st.subheader("📊 Resume Analysis")

        st.metric(
            "Job Match Score",
            f"{score:.1f}%"
        )

        st.write("### ✅ Skills Found")

        if resume_skills:
            st.write(", ".join(resume_skills))
        else:
            st.write("No matching skills found.")

        st.write("### ⚠️ Skills You May Need")

        if missing_skills:
            st.write(", ".join(missing_skills))
        else:
            st.write("No major missing skills detected.")

        st.success("Analysis completed!")
