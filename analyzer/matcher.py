"""
ResumeForge Pro
Semantic Resume Matching Engine
"""

from functools import lru_cache

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from analyzer.keywords import (
    keyword_coverage,
    keyword_statistics
)

from analyzer.skills import (
    skill_coverage,
    skill_statistics
)

# ==========================================================
# LOAD SENTENCE TRANSFORMER MODEL (CACHE)
# ==========================================================

@lru_cache(maxsize=1)
def get_model():
    """
    Load the embedding model only once.
    """

    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


# ==========================================================
# EMBEDDING
# ==========================================================

def get_embedding(text):

    model = get_model()

    return model.encode(
        [text],
        normalize_embeddings=True
    )


# ==========================================================
# SEMANTIC SIMILARITY
# ==========================================================

def semantic_similarity(
    resume_text,
    job_description
):
    """
    Returns semantic similarity score (0-100).
    """

    resume_vector = get_embedding(
        resume_text
    )

    jd_vector = get_embedding(
        job_description
    )

    similarity = cosine_similarity(
        resume_vector,
        jd_vector
    )[0][0]

    similarity = max(
        0,
        min(
            similarity,
            1
        )
    )

    return round(
        similarity * 100,
        2
    )


# ==========================================================
# EXPERIENCE BONUS
# ==========================================================

def experience_bonus(resume_text):

    resume = resume_text.lower()

    import re

    matches = re.findall(
        r"(\d+)\+?\s*years?",
        resume
    )

    if matches:

        years = max(
            int(x)
            for x in matches
        )

        if years >= 5:
            return 5

        elif years >= 3:
            return 3

        elif years >= 1:
            return 2

    return 0

# ==========================================================
# PROJECT BONUS
# ==========================================================

def project_bonus(resume_text):

    text = resume_text.lower()

    project_keywords = [
        "project",
        "developed",
        "built",
        "implemented",
        "deployed"
    ]


    found = sum(
        1 for word in project_keywords
        if word in text
    )


    if found >= 4:
        return 4

    elif found >= 2:
        return 2

    return 0

# ==========================================================
# EDUCATION BONUS
# ==========================================================

def education_bonus(resume_text):

    text = resume_text.lower()


    education_keywords = [
        "bachelor",
        "master",
        "bsc",
        "msc",
        "artificial intelligence",
        "data science"
    ]


    matches = sum(
        1 for item in education_keywords
        if item in text
    )


    if matches >= 3:
        return 2

    return 0

# ==========================================================
# FINAL MATCH SCORE
# ==========================================================

def calculate_match_score(
    resume_text,
    job_description
):
    """
    Final Resume Match Score

    Weight Distribution:
    -------------------
    Semantic Similarity : 50%
    Skill Coverage      : 30%
    Keyword Coverage    : 20%
    """

    semantic_score = semantic_similarity(
        resume_text,
        job_description
    )

    skill_score = skill_coverage(
        resume_text,
        job_description
    )

    keyword_score = keyword_coverage(
        resume_text,
        job_description
    )

    bonus = (
        experience_bonus(resume_text)
        +
        project_bonus(resume_text)
        +
        education_bonus(resume_text)
    )

    final_score = (

        semantic_score * 0.50

        +

        skill_score * 0.30

        +

        keyword_score * 0.20

    )

    final_score += min(bonus,8)

    final_score = min(
        final_score,
        100
    )

    return round(
        final_score,
        2
    )


# ==========================================================
# MATCH BREAKDOWN
# ==========================================================

def match_breakdown(
    resume_text,
    job_description
):

    semantic_score = semantic_similarity(
        resume_text,
        job_description
    )

    skill_score = skill_coverage(
        resume_text,
        job_description
    )

    keyword_score = keyword_coverage(
        resume_text,
        job_description
    )

    final_score = calculate_match_score(
        resume_text,
        job_description
    )

    return {

        "semantic_score":
        semantic_score,

        "skill_score":
        skill_score,

        "keyword_score":
        keyword_score,

        "final_score":
        final_score,

        "skill_details":
        skill_statistics(
            resume_text,
            job_description
        ),

        "keyword_details":
        keyword_statistics(
            resume_text,
            job_description
        )
    }


# ==========================================================
# END OF FILE
# ==========================================================