"""
====================================================
ResumeForge Pro
Advanced ATS Keyword Extraction Engine
====================================================
"""


import re



# =====================================================
# KEYWORD DATABASE
# =====================================================


KEYWORD_LIST = [


    # Programming

    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "golang",
    "rust",
    "php",
    "ruby",
    "swift",
    "kotlin",
    "r programming",



    # Databases

    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "redis",
    "firebase",
    "oracle",
    "dynamodb",



    # Data Analytics

    "data analysis",
    "data analytics",
    "data science",
    "business intelligence",
    "statistics",
    "predictive analytics",
    "exploratory data analysis",

    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "plotly",
    "scipy",



    # Machine Learning

    "artificial intelligence",
    "machine learning",
    "deep learning",
    "computer vision",
    "natural language processing",
    "nlp",
    "generative ai",

    "tensorflow",
    "keras",
    "pytorch",
    "scikit-learn",
    "sklearn",
    "xgboost",
    "lightgbm",



    # Generative AI / LLM

    "llm",
    "large language model",
    "prompt engineering",
    "langchain",
    "ollama",
    "hugging face",
    "rag",
    "vector database",
    "embedding",



    # Cloud / DevOps

    "aws",
    "azure",
    "google cloud",
    "gcp",
    "docker",
    "kubernetes",
    "jenkins",
    "linux",
    "git",
    "github",



    # Visualization

    "excel",
    "power bi",
    "tableau",
    "looker",



    # Frameworks

    "streamlit",
    "flask",
    "fastapi",
    "django",
    "react",
    "node.js",



    # Soft Skills

    "communication",
    "problem solving",
    "teamwork",
    "leadership",
    "critical thinking",
    "time management",
    "analytical thinking",


]



# =====================================================
# ACTION WORD DATABASE
# =====================================================


ACTION_WORDS = [

    "developed",
    "designed",
    "implemented",
    "optimized",
    "built",
    "created",
    "engineered",
    "managed",
    "automated",
    "integrated",
    "improved",
    "deployed",
    "analyzed",
    "tested"

]



# =====================================================
# TEXT CLEANING
# =====================================================


def clean_text(text):

    if not text:

        return ""


    text = text.lower()


    text = text.replace(
        "/",
        " "
    )


    text = text.replace(
        "-",
        "-"
    )


    text = text.replace(
        "_",
        " "
    )


    text = re.sub(
        r"[^a-z0-9+#.\-\s]",
        " ",
        text
    )


    text = re.sub(
        r"\s+",
        " ",
        text
    )


    return text.strip()



# =====================================================
# KEYWORD SEARCH
# =====================================================


def contains_keyword(text, keyword):


    keyword = clean_text(keyword)


    # Handle single letters safely

    if keyword in [
        "r programming"
    ]:

        pattern = r"\br\sprogramming\b"


    else:

        pattern = (
            r"(?<!\w)"
            +
            re.escape(keyword)
            +
            r"(?!\w)"
        )


    return re.search(
        pattern,
        text
    ) is not None



# =====================================================
# EXTRACT KEYWORDS
# =====================================================


def extract_keywords(text):


    text = clean_text(text)


    detected = []


    for keyword in KEYWORD_LIST:


        if contains_keyword(
            text,
            keyword
        ):

            detected.append(
                keyword
            )


    return sorted(
        list(set(detected))
    )



# =====================================================
# MATCH KEYWORDS
# =====================================================


def matched_keywords(
        resume_text,
        job_description
):


    resume_keywords = set(
        extract_keywords(
            resume_text
        )
    )


    jd_keywords = set(
        extract_keywords(
            job_description
        )
    )


    return sorted(

        resume_keywords
        &
        jd_keywords

    )



# =====================================================
# MISSING KEYWORDS
# =====================================================


def missing_keywords(
        resume_text,
        job_description
):


    resume_keywords = set(
        extract_keywords(
            resume_text
        )
    )


    jd_keywords = set(
        extract_keywords(
            job_description
        )
    )


    return sorted(

        jd_keywords
        -
        resume_keywords

    )



# =====================================================
# KEYWORD COVERAGE
# =====================================================


def keyword_coverage(
        resume_text,
        job_description
):


    jd_keywords = extract_keywords(
        job_description
    )


    if len(jd_keywords) == 0:

        return 0



    matched = matched_keywords(
        resume_text,
        job_description
    )


    score = (

        len(matched)
        /
        len(jd_keywords)

    ) * 100



    # Prevent unrealistic 100%

    if score == 100 and len(jd_keywords) > 8:

        score = 95



    return round(
        score,
        2
    )



# =====================================================
# KEYWORD STATISTICS
# =====================================================


def keyword_statistics(
        resume_text,
        job_description
):


    resume_keywords = extract_keywords(
        resume_text
    )


    jd_keywords = extract_keywords(
        job_description
    )


    matched = matched_keywords(
        resume_text,
        job_description
    )


    missing = missing_keywords(
        resume_text,
        job_description
    )


    return {


        "resume_keywords":
            resume_keywords,


        "required_keywords":
            jd_keywords,


        "matched_keywords":
            matched,


        "missing_keywords":
            missing,


        "resume_keyword_count":
            len(resume_keywords),


        "required_keyword_count":
            len(jd_keywords),


        "matched_count":
            len(matched),


        "missing_count":
            len(missing),


        "coverage":
            keyword_coverage(
                resume_text,
                job_description
            )

    }