from analyzer.scoring import analyze_scores


resume = """

Python
Machine Learning
TensorFlow
Pandas
NumPy
SQL
Power BI
Docker
AWS
Linux

Projects:
AI Resume Analyzer

Education:
BSc Artificial Intelligence

"""


jd = """

AI ML Engineer

Required Skills:

Python
Machine Learning
Deep Learning
TensorFlow
PyTorch
SQL
Docker
AWS
Git
Streamlit

"""


result = analyze_scores(
    resume,
    jd
)


print("\nRESULT")
print("----------------")

print(
    "Overall:",
    result["overall_score"]
)

print(
    "ATS:",
    result["ats_score"]
)

print(
    "Match:",
    result["job_match"]
)

print(
    "Grade:",
    result["grade"]
)