import streamlit as st
from pypdf import PdfReader
import re

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

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

        resume_lower = resume_text.lower()
        job_lower = job_description.lower()

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

        required_skills = [
            skill for skill in skills
            if re.search(r"\b" + re.escape(skill) + r"\b", job_lower)
        ]

        for skill in required_skills:
            if skill not in resume_skills:
                missing_skills.append(skill)

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

        st.write("### 💡 Recommendations")

        recommendations = []

        if "python" not in resume_lower:
            recommendations.append(
                "Add Python projects or experience to your resume."
            )

        if "sql" not in resume_lower:
            recommendations.append(
                "Consider adding SQL skills and a SQL-based project."
            )

        if "machine learning" not in resume_lower:
            recommendations.append(
                "Add a machine learning project if you have one."
            )

        if "github" not in resume_lower:
            recommendations.append(
                "Add your GitHub profile to showcase your projects."
            )

        if recommendations:
            for recommendation in recommendations:
                st.write("•", recommendation)
        else:
            st.write(
                "Your resume contains several important skills "
                "for this job. Keep building your portfolio!"
            )

        st.success("Analysis completed!")
