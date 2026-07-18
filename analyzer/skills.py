"""
====================================================
AI Resume Analyzer Pro
Universal Skill Extraction Engine
====================================================
"""


import re


# ======================================================
# TECHNICAL SKILL DATABASE
# ======================================================


SKILL_DATABASE = [

    # Programming

    "python",
    "java",
    "javascript",
    "typescript",
    "c++",
    "c#",
    "php",
    "ruby",
    "go",
    "r programming",


    # AI / ML

    "artificial intelligence",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "nlp",
    "computer vision",
    "generative ai",
    "llm",
    "prompt engineering",
    "hugging face",
    "opencv",


    # Data Analytics

    "data analysis",
    "data science",
    "statistics",
    "pandas",
    "numpy",
    "excel",
    "advanced excel",
    "power bi",
    "tableau",
    "data visualization",


    # Databases

    "sql",
    "mysql",
    "postgresql",
    "oracle",
    "mongodb",
    "nosql",
    "database management",


    # Development

    "html",
    "css",
    "react",
    "angular",
    "node.js",
    "express",
    "django",
    "flask",
    "fastapi",
    "rest api",


    # Software Engineering

    "data structures",
    "algorithms",
    "object oriented programming",
    "oops",
    "software development",
    "git",
    "github",
    "version control",


    # Cloud

    "aws",
    "azure",
    "google cloud",
    "gcp",
    "cloud computing",


    # DevOps

    "docker",
    "kubernetes",
    "jenkins",
    "ci/cd",
    "linux",
    "terraform",


    # Testing

    "manual testing",
    "automation testing",
    "selenium",
    "test automation",
    "api testing",
    "jira",


    # Cyber Security

    "cybersecurity",
    "network security",
    "ethical hacking",
    "penetration testing",
    "firewalls",


    # Networking

    "networking",
    "tcp/ip",
    "dns",
    "routers",
    "switches",
    "ccna",


    # Tools

    "slack",
    "figma",
    "powerpoint"

]



# ======================================================
# SOFT SKILLS
# ======================================================


SOFT_SKILLS = [

    "communication",
    "leadership",
    "problem solving",
    "teamwork",
    "collaboration"

]



# ======================================================
# EXTRACT SKILLS
# ======================================================


def extract_skills(text):

    text = text.lower()

    found = []


    for skill in SKILL_DATABASE:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found.append(
                skill.title()
            )


    return sorted(
        list(set(found))
    )



# ======================================================
# EXTRACT SOFT SKILLS
# ======================================================


def extract_soft_skills(text):

    text = text.lower()

    found = []


    for skill in SOFT_SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"


        if re.search(pattern, text):

            found.append(
                skill.title()
            )


    return sorted(
        list(set(found))
    )



# ======================================================
# SKILL STATISTICS
# ======================================================


def skill_statistics(
        resume_text,
        job_description
):


    resume_skills = extract_skills(
        resume_text
    )


    required_skills = extract_skills(
        job_description
    )


    matched = list(

        set(resume_skills)
        &
        set(required_skills)

    )


    missing = list(

        set(required_skills)
        -
        set(resume_skills)

    )


    return {

        "resume_skills":
            resume_skills,


        "matched_skills":
            sorted(matched),


        "missing_skills":
            sorted(missing),


        "total_required":
            len(required_skills),


        "total_matched":
            len(matched)

    }



# ======================================================
# SKILL COVERAGE SCORE
# ======================================================


def skill_coverage(
        resume_text,
        job_description
):


    data = skill_statistics(

        resume_text,

        job_description

    )


    if data["total_required"] == 0:

        return 0



    score = (

        data["total_matched"]

        /

        data["total_required"]

    ) * 100



    # Avoid fake perfect scores

    if score == 100 and data["total_required"] > 5:

        score = 95



    return round(
        score,
        2
    )



# ======================================================
# MISSING SKILLS
# ======================================================


def missing_skills(
        resume_text,
        job_description
):


    return skill_statistics(

        resume_text,

        job_description

    )["missing_skills"]