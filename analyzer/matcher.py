from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_match_score(resume_text, job_description):
    """
    Calculate semantic similarity between resume and job description.
    Returns a percentage from 0 to 100.
    """

    resume_embedding = model.encode([resume_text])
    jd_embedding = model.encode([job_description])

    similarity = cosine_similarity(
        resume_embedding,
        jd_embedding
    )[0][0]

    percentage = round(similarity * 100, 2)

    # Clamp between 0 and 100
    percentage = max(0, min(100, percentage))

    return percentage