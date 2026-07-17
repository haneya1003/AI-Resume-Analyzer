import ollama


def analyze_resume(resume_text, job_description):
    """
    Analyze the resume using Llama 3.2
    """

    prompt = f"""
You are an expert ATS Resume Reviewer.

Resume:
{resume_text}

Job Description:
{job_description}

Analyze the resume and provide:

1. ATS Score (out of 100)

2. Resume Summary

3. Strengths

4. Weaknesses

5. Missing Skills

6. Suggestions for Improvement

7. Final Recommendation
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]