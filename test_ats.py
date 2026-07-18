from analyzer.ats import calculate_ats_score


resume_text = """

Education:
Bachelor of Science in Artificial Intelligence

Skills:
Python
Machine Learning
Deep Learning
SQL
Pandas
NumPy
TensorFlow
PyTorch
NLP
Computer Vision
Docker
AWS
Azure
Git
Linux
Streamlit

Projects:
AI Resume Analyzer
Machine Learning Model
Computer Vision Project

Experience:
Built AI applications using Python and ML.

Certification:
AWS Cloud Fundamentals

"""


jd = """

AI/ML Engineer

Required Skills:

Python
Machine Learning
Deep Learning
SQL
TensorFlow
PyTorch
NLP
Computer Vision
Docker
AWS
Azure
Git
Linux
Streamlit

"""


score, feedback = calculate_ats_score(
    resume_text,
    jd
)


print("\nATS SCORE:", score)

print("\nFeedback:")

for item in feedback:
    print("-", item)