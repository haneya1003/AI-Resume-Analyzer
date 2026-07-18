"""
AI Resume Analyzer Pro
Advanced ATS Compatibility Engine
"""


def calculate_ats_score(resume_text, job_description):

    resume = resume_text.lower()
    jd = job_description.lower()

    feedback = []

    total_score = 0


    # ==========================================
    # 1. JD KEYWORD MATCHING (30%)
    # ==========================================

    stop_words = {
        "the","and","with","using","experience",
        "candidate","required","preferred",
        "knowledge","strong","ability",
        "work","team","develop","looking",
        "good","basic","skills"
    }


    jd_words = (
        jd.replace(",", " ")
          .replace(".", " ")
          .replace(":", " ")
          .split()
    )


    keywords = set(
        word for word in jd_words
        if len(word) > 4
        and word not in stop_words
    )


    matched_keywords = [
        word for word in keywords
        if word in resume
    ]


    keyword_score = 0

    if keywords:
        keyword_score = (
            len(matched_keywords)
            /
            len(keywords)
        ) * 30


    total_score += keyword_score


    if keyword_score < 20:
        feedback.append(
            "Increase job-specific keywords."
        )


    # ==========================================
    # 2. TECHNICAL SKILL MATCH (30%)
    # ==========================================


    skill_library = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "pandas",
        "numpy",
        "nlp",
        "docker",
        "aws",
        "azure",
        "git",
        "linux",
        "streamlit",
        "power bi",
        "tableau",
        "excel"
    ]


    jd_skills = [
        skill for skill in skill_library
        if skill in jd
    ]


    matched_skills = [
        skill for skill in jd_skills
        if skill in resume
    ]


    skill_score = 0

    if jd_skills:
        skill_score = (
            len(matched_skills)
            /
            len(jd_skills)
        ) * 30


    total_score += skill_score


    if len(matched_skills) < len(jd_skills):

        missing = set(jd_skills) - set(matched_skills)

        feedback.append(
            f"Missing skills: {', '.join(missing)}"
        )



    # ==========================================
    # 3. RESUME STRUCTURE (25%)
    # ==========================================


    sections = [
        "education",
        "skills",
        "projects",
        "experience",
        "certification",
        "summary"
    ]


    found_sections = [
        section
        for section in sections
        if section in resume
    ]


    structure_score = (
        len(found_sections)
        /
        len(sections)
    ) * 25


    total_score += structure_score



    if len(found_sections) < 4:

        feedback.append(
            "Add clear resume sections."
        )



    # ==========================================
    # 4. ATS FORMAT SCORE (10%)
    # ==========================================


    formatting_score = 10


    if len(resume_text) < 700:
        formatting_score -= 3
        feedback.append(
            "Resume content is short."
        )


    if "table" in resume:
        formatting_score -= 2
        feedback.append(
            "Avoid tables for ATS compatibility."
        )


    total_score += max(formatting_score,0)



    # ==========================================
    # FINAL SCORE
    # ==========================================


    final_score = round(
        min(total_score,95),
        2
    )


    if final_score >= 95:

        final_score = 95



    if final_score >= 85:

        feedback.append(
            "Excellent ATS compatibility."
        )

    elif final_score >= 70:

        feedback.append(
            "Good ATS compatibility."
        )

    else:

        feedback.append(
            "Resume needs optimization."
        )


    return final_score, feedback