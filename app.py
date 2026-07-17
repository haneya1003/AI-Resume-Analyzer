import streamlit as st
from analyzer.parser import extract_text
from analyzer.llm import analyze_resume
from analyzer.matcher import calculate_match_score

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="ResumeForge - AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📄 ResumeForge - AI Resume Analyzer Pro")

st.markdown("""
Analyze your resume using AI and compare it with a Job Description.

### Features
- 📄 Resume Upload
- 🎯 Resume Match Score
- 🤖 AI Resume Analysis
- 📊 ATS Analysis
- 📑 PDF Report (Coming Soon)
""")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("ResumeForge")
st.sidebar.success("Version 1.0")

# -----------------------------
# Upload Resume
# -----------------------------
resume = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)

# -----------------------------
# Job Description
# -----------------------------
job_description = st.text_area(
    "Paste the Job Description",
    height=200
)

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze Resume"):

    if resume is None:
        st.warning("Please upload your resume.")

    elif job_description.strip() == "":
        st.warning("Please paste the Job Description.")

    else:

        # Extract Resume Text
        resume_text = extract_text(resume)

        st.success("✅ Resume Parsed Successfully!")

        st.subheader("📄 Extracted Resume")

        st.text_area(
            "Resume Content",
            value=resume_text,
            height=250
        )

        # Resume Match Score
        st.divider()

        st.subheader("📈 Resume Match Score")

        match_score = calculate_match_score(
            resume_text,
            job_description
        )

        st.progress(int(match_score))

        st.metric(
            label="Resume Match",
            value=f"{match_score}%"
        )

        # AI Analysis
        st.divider()

        st.subheader("🤖 AI Resume Analysis")

        with st.spinner("Analyzing with Llama 3.2..."):
            ai_result = analyze_resume(
                resume_text,
                job_description
            )

        st.markdown(ai_result)

        st.success("✅ Analysis Complete!")