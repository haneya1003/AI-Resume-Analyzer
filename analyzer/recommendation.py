"""
====================================================
ResumeForge Pro
AI Skill Recommendation Engine
====================================================
"""


def skill_recommendations(
        missing_skills
):

    recommendations = []


    for skill in missing_skills:

        recommendations.append(
            f"Consider learning {skill} to improve your resume match."
        )


    if not recommendations:

        recommendations.append(
            "Your resume covers most required skills."
        )


    return recommendations