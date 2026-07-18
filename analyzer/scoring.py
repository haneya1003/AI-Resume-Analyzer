"""
AI Resume Analyzer Pro
Advanced Resume Scoring Engine
"""

from analyzer.ats import calculate_ats_score

from analyzer.matcher import (
    calculate_match_score,
    match_breakdown,
)

from analyzer.skills import (
    skill_coverage,
    skill_statistics,
)

from analyzer.keywords import (
    keyword_coverage,
    keyword_statistics,
)


# =====================================================
# SCORE WEIGHTS
# =====================================================


ATS_WEIGHT = 0.30
MATCH_WEIGHT = 0.35
SKILL_WEIGHT = 0.20
KEYWORD_WEIGHT = 0.15


# =====================================================
# BONUS SCORE
# =====================================================

def calculate_bonus_score(
    resume_text,
    job_description
):

    skills = skill_statistics(
        resume_text,
        job_description
    )

    keywords = keyword_statistics(
        resume_text,
        job_description
    )


    bonus = 0


    if len(skills["matched_skills"]) >= 8:
        bonus += 2


    if len(keywords["matched_keywords"]) >= 8:
        bonus += 2


    return min(bonus,4)



# =====================================================
# FINAL SCORE
# =====================================================

def calculate_overall_score(
    ats,
    match,
    skill,
    keyword,
    bonus
):

    score = (

        ats * ATS_WEIGHT

        +

        match * MATCH_WEIGHT

        +

        skill * SKILL_WEIGHT

        +

        keyword * KEYWORD_WEIGHT

        +

        bonus

    )


    return round(
        min(score,100),
        2
    )



# =====================================================
# GRADE
# =====================================================

def recruiter_grade(score):

    if score >= 90:
        return "A+"

    elif score >= 80:
        return "A"

    elif score >= 70:
        return "B+"

    elif score >= 60:
        return "B"

    elif score >= 50:
        return "C"

    else:
        return "Needs Improvement"




# =====================================================
# INTERVIEW CHANCE
# =====================================================

def interview_probability(score):

    if score >= 90:
        return "90%"

    elif score >= 80:
        return "75%"

    elif score >= 70:
        return "60%"

    elif score >= 60:
        return "45%"

    else:
        return "25%"

# =====================================================
# MAIN ANALYSIS PIPELINE
# =====================================================

def analyze_scores(
    resume_text,
    job_description
):


    # ATS SCORE

    ats_score, feedback = calculate_ats_score(
        resume_text,
        job_description
    )


    print(
        "SCORING ATS VALUE:",
        ats_score
    )



    # MATCH SCORE

    match_score = calculate_match_score(
        resume_text,
        job_description
    )



    # SKILL SCORE

    skill_score = skill_coverage(
        resume_text,
        job_description
    )



    # KEYWORD SCORE

    keyword_score = keyword_coverage(
        resume_text,
        job_description
    )



    # BONUS

    bonus_score = calculate_bonus_score(
        resume_text,
        job_description
    )



    # FINAL

    overall_score = calculate_overall_score(

        ats_score,

        match_score,

        skill_score,

        keyword_score,

        bonus_score

    )



    grade = recruiter_grade(
        overall_score
    )


    chance = interview_probability(
        overall_score
    )



    return {


        "overall_score":
            overall_score,


        "ats_score":
            round(ats_score,2),


        "job_match":
            round(match_score,2),


        "skill_match":
            round(skill_score,2),


        "keyword_match":
            round(keyword_score,2),


        "bonus_score":
            bonus_score,


        "grade":
            grade,


        "interview_probability":
            chance,


        "feedback":
            feedback,


        "match_breakdown":
            match_breakdown(
                resume_text,
                job_description
            ),


        "skills":
            skill_statistics(
                resume_text,
                job_description
            ),


        "keywords":
            keyword_statistics(
                resume_text,
                job_description
            )

    }