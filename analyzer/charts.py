from analyzer.skills import (
    extract_skills,
    missing_skills,
    skill_coverage
)

from analyzer.keywords import (
    keyword_coverage
)


def score_breakdown(ats_score, match_score):
    """
    Summary scores for dashboard cards.
    """
    return {
        "ATS Score": ats_score,
        "Resume Match": round(match_score, 2),
        "Remaining": max(0, 100 - ats_score)
    }


def skill_chart_data(resume_text, job_description):
    """
    Data for skills chart.
    """
    found = len(extract_skills(resume_text))
    missing = len(missing_skills(resume_text, job_description))

    return {
        "Found": found,
        "Missing": missing
    }


def coverage_chart_data(resume_text, job_description):
    """
    Data for coverage chart.
    """
    return {
        "Skill Coverage": skill_coverage(
            resume_text,
            job_description
        ),
        "Keyword Coverage": keyword_coverage(
            resume_text,
            job_description
        )
    }


def dashboard_data(
    resume_text,
    job_description,
    ats_score,
    match_score
):
    """
    Complete dashboard data.
    """

    return {
        "scores": score_breakdown(
            ats_score,
            match_score
        ),

        "skills": skill_chart_data(
            resume_text,
            job_description
        ),

        "coverage": coverage_chart_data(
            resume_text,
            job_description
        )
    }