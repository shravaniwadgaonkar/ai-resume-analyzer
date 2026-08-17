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
            resume_text += text + "\n"

    # Check whether text was extracted
    if not resume_text.strip():

        st.error(
            "⚠️ No selectable text was found in this PDF. "
            "This may be a scanned/image-based resume."
        )

        st.info(
            "Please upload a PDF created from selectable text, "
            "or use an OCR-enabled version of your resume."
        )

    else:

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
                "docker",
                "artificial intelligence",
                "natural language processing"
            ]

            resume_skills = []

            for skill in skills:
                if re.search(
                    r"\b" + re.escape(skill) + r"\b",
                    resume_lower
                ):
                    resume_skills.append(skill)

            required_skills = []

            for skill in skills:
                if re.search(
                    r"\b" + re.escape(skill) + r"\b",
                    job_lower
                ):
                    required_skills.append(skill)

            missing_skills = [
                skill
                for skill in required_skills
                if skill not in resume_skills
            ]

            matched_skills = [
                skill
                for skill in required_skills
                if skill in resume_skills
            ]

            if required_skills:
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

            if matched_skills:
                st.write(", ".join(matched_skills))
            else:
                st.write("No matching skills found.")

            st.write("### ⚠️ Skills You May Need")

            if missing_skills:
                st.write(", ".join(missing_skills))
            else:
                st.write("No major missing skills detected.")

            st.write("### 💡 Recommendations")

            if "python" in missing_skills:
                st.write(
                    "• Add Python projects or experience."
                )

            if "sql" in missing_skills:
                st.write(
                    "• Add SQL skills or a SQL-based project."
                )

            if "machine learning" in missing_skills:
                st.write(
                    "• Add a machine learning project."
                )

            if "github" in missing_skills:
                st.write(
                    "• Add your GitHub profile."
                )

            if not missing_skills:
                st.success(
                    "Your resume matches the detected job requirements well!"
                )

            st.success("Analysis completed!")
