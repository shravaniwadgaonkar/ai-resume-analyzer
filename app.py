import streamlit as st
from pypdf import PdfReader
import re

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write(
    "Upload your resume and compare it with a job description."
)

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the job description here",
    height=220
)

# Skills and concepts the analyzer can detect
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
    "data visualization",
    "statistics",
    "git",
    "github",
    "streamlit",
    "aws",
    "docker",
    "artificial intelligence",
    "natural language processing",
    "prompt engineering",
    "generative ai",
    "api",
    "apis",
    "ai agents",
    "automation",
    "image models",
    "video models",
    "open-source models",
    "model evaluation",
    "software development",
    "business automation"
]

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text + "\n"

    if not resume_text.strip():

        st.error(
            "⚠️ No selectable text was found in this PDF. "
            "Please upload a text-based PDF."
        )

    else:

        st.subheader("📋 Resume Preview")

        st.text_area(
            "Extracted text",
            resume_text,
            height=350
        )

        if job_description.strip():

            resume_lower = resume_text.lower()
            job_lower = job_description.lower()

            # Detect skills in resume
            resume_skills = []

            for skill in skills:
                if skill in resume_lower:
                    resume_skills.append(skill)

            # Detect skills required by job
            required_skills = []

            for skill in skills:
                if skill in job_lower:
                    required_skills.append(skill)

            # Find matches
            matched_skills = [
                skill
                for skill in required_skills
                if skill in resume_skills
            ]

            missing_skills = [
                skill
                for skill in required_skills
                if skill not in resume_skills
            ]

            # Calculate realistic score
            if required_skills:

                score = (
                    len(matched_skills)
                    / len(required_skills)
                ) * 100

            else:
                score = 0

            st.subheader("📊 Resume Analysis")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Job Match Score",
                    f"{score:.1f}%"
                )

            with col2:
                st.metric(
                    "Matched Skills",
                    len(matched_skills)
                )

            with col3:
                st.metric(
                    "Missing Skills",
                    len(missing_skills)
                )

            st.divider()

            st.write("### ✅ Skills Found")

            if matched_skills:

                for skill in matched_skills:
                    st.write(f"✅ {skill.title()}")

            else:
                st.write("No matching skills detected.")

            st.write("### ⚠️ Skills You May Need")

            if missing_skills:

                for skill in missing_skills:
                    st.write(f"⚠️ {skill.title()}")

            else:

                st.success(
                    "No major missing skills detected."
                )

            st.write("### 💡 Recommendations")

            recommendations = []

            if "python" in missing_skills:
                recommendations.append(
                    "Add Python projects or practical Python experience."
                )

            if "sql" in missing_skills:
                recommendations.append(
                    "Add SQL projects and demonstrate database skills."
                )

            if "ai agents" in missing_skills:
                recommendations.append(
                    "Build a small AI agent that can use tools."
                )

            if "api" in missing_skills or "apis" in missing_skills:
                recommendations.append(
                    "Build a project that integrates an AI or REST API."
                )

            if "model evaluation" in missing_skills:
                recommendations.append(
                    "Add evaluation metrics or comparison tests to an ML project."
                )

            if "open-source models" in missing_skills:
                recommendations.append(
                    "Experiment with an open-source model and document the results."
                )

            if "image models" in missing_skills or "video models" in missing_skills:
                recommendations.append(
                    "Experiment with an image/video generation API and document the workflow."
                )

            if "github" in missing_skills:
                recommendations.append(
                    "Add your GitHub profile and project repositories."
                )

            if recommendations:

                for recommendation in recommendations:
                    st.write(f"• {recommendation}")

            else:

                st.success(
                    "Your resume demonstrates the main skills detected in the job description."
                )

            st.divider()

            st.caption(
                "Note: This score is based on detected keywords and "
                "is an indicator, not a hiring decision."
            )

            st.success("Analysis completed!")
