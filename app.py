"""
====================================================
AI Resume Analyzer
Professional ATS Resume Screening System
====================================================
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import streamlit as st
from pathlib import Path

import plotly.graph_objects as go


# ======================================================
# NEW FEATURES
# ======================================================

from analyzer.recommendation import skill_recommendations
from analyzer.review import resume_strengths
from analyzer.roles import recommend_roles


# ======================================================
# IMPORT MODULES
# ======================================================

from analyzer.parser import (
    extract_text,
    validate_resume,
    resume_statistics,
)


from analyzer.skills import (
    skill_statistics,
)


from analyzer.keywords import (
    keyword_statistics,
)


from analyzer.ats import (
    calculate_ats_score,
)


from analyzer.scoring import (
    analyze_scores,
)


from analyzer.llm import (
    analyze_resume,
)


from analyzer.report import (
    generate_report,
)



# ======================================================
# PAGE CONFIG
# ======================================================


st.set_page_config(

    page_title="AI Resume Analyzer Pro",

    page_icon="🤖",

    layout="wide",

    initial_sidebar_state="expanded"

)



# ======================================================
# CUSTOM CSS
# ======================================================


st.markdown("""

<style>


.main{

background:#ffffff;

}



.block-container{

padding-top:1rem;

padding-bottom:2rem;

}



.title{

font-size:40px;

font-weight:700;

}



.subtitle{

font-size:18px;

color:#666;

}



footer{

visibility:hidden;

}


header{

visibility:hidden;

}



</style>


""", unsafe_allow_html=True)



# ======================================================
# HEADER
# ======================================================


header_left, header_right = st.columns([1,6])



with header_left:


    logo = Path(
        "assets/logo.png"
    )


    if logo.exists():

        st.image(

            str(logo),

            width=80

        )



with header_right:


    st.markdown(

        "<div class='title'>🤖 AI Resume Analyzer Pro</div>",

        unsafe_allow_html=True

    )


    st.markdown(

        "<div class='subtitle'>Advanced ATS Resume Screening using NLP, AI & LLM</div>",

        unsafe_allow_html=True

    )



st.divider()



# ======================================================
# SIDEBAR
# ======================================================


st.sidebar.title(
    "AI Resume Analyzer Pro"
)



st.sidebar.markdown(
    "### Features"
)



features = [

    "ATS Compatibility",

    "Semantic Resume Matching",

    "Skill Gap Analysis",

    "Keyword Coverage",

    "AI Recruiter Review",

    "PDF Report"

]



for feature in features:

    st.sidebar.success(feature)



st.sidebar.divider()



st.sidebar.markdown(
    "### Built With"
)



tools = [

    "Python",

    "Streamlit",

    "Sentence Transformers",

    "Ollama Llama 3.2",

    "Plotly"

]


for tool in tools:

    st.sidebar.write(
        "• " + tool
    )



# ======================================================
# INPUT SECTION
# ======================================================


left, right = st.columns(2)



with left:


    uploaded_resume = st.file_uploader(

        "Upload Resume",

        type=[

            "pdf",

            "docx"

        ]

    )



with right:


    job_description = st.text_area(

        "Paste Job Description",

        height=250

    )



analyze = st.button(

    "🚀 Analyze Resume",

    use_container_width=True

)



# ======================================================
# ANALYSIS START
# ======================================================


if analyze:


    if uploaded_resume is None:


        st.error(
            "Please upload a resume."
        )


        st.stop()



    if len(job_description.strip()) < 20:


        st.error(
            "Please paste a valid job description."
        )


        st.stop()



    with st.spinner(
        "Reading Resume..."
    ):


        resume_text = extract_text(

            uploaded_resume

        )



    valid, message = validate_resume(

        resume_text

    )



    if not valid:


        st.error(message)

        st.stop()
            # ======================================================
    # SCORE ANALYSIS
    # ======================================================


    with st.spinner(
        "Analyzing Resume..."
    ):


        results = analyze_scores(

            resume_text,

            job_description

        )
        ats_score = results["ats_score"]



    overall_score = results["overall_score"]

    ats_score = results["ats_score"]

    job_match = results["job_match"]

    skill_match = results["skill_match"]

    keyword_match = results["keyword_match"]

    grade = results["grade"]

    interview_probability = results["interview_probability"]

    feedback = results["feedback"]



    # ======================================================
    # RESUME DATA
    # ======================================================


    stats = resume_statistics(

        resume_text

    )



    skills = skill_statistics(

        resume_text,

        job_description

    )



    keywords = keyword_statistics(

        resume_text,

        job_description

    )



    # ======================================================
    # AI REVIEW
    # ======================================================


    with st.spinner(

        "Generating AI Recruiter Review..."

    ):


        ai_review = analyze_resume(

            resume_text,

            job_description

        )



    st.success(

        "Analysis Completed Successfully!"

    )



    st.divider()



    # ======================================================
    # DASHBOARD
    # ======================================================


    st.header(

        "📊 Resume Dashboard"

    )



    c1,c2,c3,c4 = st.columns(4)



    c1.metric(

        "Overall Score",

        f"{overall_score:.2f}%"

    )



    c2.metric(

        "ATS Score",

        f"{ats_score:.2f}%"

    )



    c3.metric(

        "Resume Match",

        f"{job_match:.2f}%"

    )



    c4.metric(

        "Recruiter Grade",

        grade

    )



    st.divider()



    # ======================================================
    # PERFORMANCE CHART
    # ======================================================


    chart = go.Figure()



    chart.add_trace(

        go.Bar(

            x=[

                "Overall",

                "ATS",

                "Match",

                "Skills",

                "Keywords"

            ],


            y=[

                overall_score,

                ats_score,

                job_match,

                skill_match,

                keyword_match

            ],

            text=[

                f"{overall_score:.2f}%",

                f"{ats_score:.2f}%",

                f"{job_match:.2f}%",

                f"{skill_match:.2f}%",

                f"{keyword_match:.2f}%"

            ],

            textposition="outside"

        )

    )

    chart.update_layout(

        title="Resume Performance",

        template="plotly_white",

        height=450

    )



    st.plotly_chart(

        chart,

        use_container_width=True

    )



    # ======================================================
    # SCORE BREAKDOWN
    # ======================================================


    st.header(

        "📈 Performance Breakdown"

    )



    st.write(
        "Overall Resume Score"
    )

    st.progress(
        int(overall_score)
    )



    st.write(
        "ATS Compatibility"
    )

    st.progress(
        int(ats_score)
    )



    st.write(
        "Semantic Resume Match"
    )

    st.progress(
        int(job_match)
    )



    st.write(
        "Skill Coverage"
    )

    st.progress(
        int(skill_match)
    )



    st.write(
        "Keyword Coverage"
    )

    st.progress(
        int(keyword_match)
    )



    st.divider()



    # ======================================================
    # RESUME STATISTICS
    # ======================================================


    st.header(

        "📄 Resume Statistics"

    )



    s1,s2,s3 = st.columns(3)



    s1.metric(

        "Words",

        stats["word_count"]

    )


    s2.metric(

        "Characters",

        stats["character_count"]

    )


    s3.metric(

        "Lines",

        stats["line_count"]

    )



    st.divider()



    # ======================================================
    # RECRUITER PREDICTION
    # ======================================================


    st.header(

        "🎯 Recruiter Prediction"

    )



    p1,p2 = st.columns(2)



    with p1:


        st.metric(

            "Interview Chance",

            interview_probability

        )



    with p2:


        if overall_score >= 90:


            st.success(

                "Excellent Resume"

            )


        elif overall_score >=70:


            st.warning(

                "Good Resume"

            )


        else:


            st.error(

                "Needs Improvement"

            )



    st.divider()
        # ======================================================
    # TABS
    # ======================================================


    tab1, tab2, tab3, tab4 = st.tabs([

        "🟢 Skills",

        "🔑 Keywords",

        "🤖 AI Review",

        "📄 PDF Report"

    ])



    # ======================================================
    # TAB 1 - SKILLS
    # ======================================================


    with tab1:


        st.subheader(
            "Detected Skills"
        )



        if skills["resume_skills"]:


            cols = st.columns(3)


            for index, skill in enumerate(
                skills["resume_skills"]
            ):


                cols[index % 3].success(

                    skill.title()

                )


        else:


            st.warning(
                "No skills detected."
            )



        st.divider()



        st.subheader(
            "Matched Skills"
        )



        if skills["matched_skills"]:


            cols = st.columns(3)


            for index, skill in enumerate(
                skills["matched_skills"]
            ):


                cols[index % 3].info(

                    skill.title()

                )


        else:


            st.warning(
                "No matched skills found."
            )



        st.divider()



        st.subheader(
            "Missing Skills"
        )



        if skills["missing_skills"]:


            cols = st.columns(3)


            for index, skill in enumerate(
                skills["missing_skills"]
            ):


                cols[index % 3].error(

                    skill.title()

                )


        else:


            st.success(
                "No missing skills detected."
            )



        # ==================================================
        # NEW FEATURES
        # ==================================================


        st.divider()



        st.subheader(
            "🚀 Skill Improvement Roadmap"
        )



        roadmap = skill_recommendations(

            skills["missing_skills"]

        )



        if roadmap:


            for item in roadmap:


                st.write(
                    "✔ ",
                    item
                )


        else:


            st.success(
                "Your resume covers required skills."
            )



        st.divider()



        st.subheader(
            "💪 Resume Strengths"
        )



        strengths = resume_strengths(

            skills["resume_skills"]

        )



        if strengths:


            for item in strengths:


                st.success(item)


        else:


            st.warning(
                "Add more projects and technical skills."
            )



        st.divider()



        st.subheader(
            "🎯 Recommended Job Roles"
        )



        roles = recommend_roles(

            skills["resume_skills"]

        )



        for role in roles[:4]:


            st.info(

                f"{role['role']} : {role['score']}%"

            )



    # ======================================================
    # TAB 2 - KEYWORDS
    # ======================================================


    with tab2:


        st.subheader(
            "Keyword Coverage"
        )


        st.metric(

            "Coverage",

            f"{keywords['coverage']}%"

        )


        st.progress(

            int(keywords["coverage"])

        )


        st.divider()



        col1,col2 = st.columns(2)



        with col1:


            st.markdown(
                "### Matched Keywords"
            )


            for word in keywords["matched_keywords"]:


                st.success(word)



        with col2:


            st.markdown(
                "### Missing Keywords"
            )


            for word in keywords["missing_keywords"]:


                st.error(word)



    # ======================================================
    # TAB 3 - AI REVIEW
    # ======================================================


    with tab3:


        st.subheader(
            "🤖 AI Recruiter Review"
        )


        st.markdown(

            ai_review

        )


        st.divider()



        st.subheader(

            "ATS Recommendations"

        )



        if feedback:


            for item in feedback:


                st.info(item)


        else:


            st.success(
                "No ATS issues detected."
            )



    # ======================================================
    # TAB 4 - PDF REPORT
    # ======================================================


    with tab4:


        st.subheader(

            "📄 Download Resume Report"

        )



        reports = Path(

            "reports"

        )


        reports.mkdir(

            exist_ok=True

        )



        pdf_file = reports / "AI_Resume_Report.pdf"



        generate_report(

            str(pdf_file),

            ats_score,

            job_match,

            skills["resume_skills"],

            skills["missing_skills"],

            keyword_match,

            ai_review,

            overall_score,

            feedback

        )



        with open(

            pdf_file,

            "rb"

        ) as pdf:



            st.download_button(

                "📥 Download PDF Report",

                pdf,

                file_name="AI_Resume_Report.pdf",

                mime="application/pdf",

                use_container_width=True

            )



    st.divider()



    st.caption(

        "AI Resume Analyzer Pro • ATS Screening • NLP Matching • LLM Recruiter Analysis"

    )



else:


    st.info(

        """

##  Welcome to AI Resume Analyzer Pro 🤖 


### How to use:


1. Upload your Resume

2. Paste Job Description

3. Click Analyze Resume

4. Review ATS score, skills and AI feedback

5. Download PDF report


"""

    )