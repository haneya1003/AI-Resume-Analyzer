"""
ResumeForge Pro
AI Recruiter Review using Ollama
"""

import ollama

# ==========================================================
# SYSTEM PROMPT
# ==========================================================

SYSTEM_PROMPT = """
You are a Senior Technical Recruiter with over 15 years of experience.

Review the resume against the provided job description.

Your response MUST be professional and structured.

Return the following sections exactly:

1. Overall Evaluation
2. Strengths
3. Weaknesses
4. Missing Skills
5. ATS Improvements
6. Recruiter Recommendation
7. Interview Questions (5)
8. Final Verdict

Keep the review concise, practical, and recruiter-focused.
"""


# ==========================================================
# BUILD PROMPT
# ==========================================================

def build_prompt(
    resume_text,
    job_description
):

    prompt = f"""
Job Description
----------------
{job_description}

Resume
-------
{resume_text}

Instructions
------------
Compare the resume with the job description.

Only mention skills that actually exist or are genuinely missing.

Provide actionable suggestions.

Avoid hallucinations.

"""

    return prompt


# ==========================================================
# OLLAMA CALL
# ==========================================================

def call_llm(prompt):

    response = ollama.chat(

        model="llama3.2",

        messages=[

            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },

            {
                "role":"user",
                "content":prompt
            }

        ]

    )

    return response["message"]["content"]
# ==========================================================
# MAIN AI ANALYSIS
# ==========================================================

def analyze_resume(
    resume_text,
    job_description
):
    """
    Generates an AI recruiter review using Ollama.
    """

    try:

        prompt = build_prompt(
            resume_text,
            job_description
        )

        return call_llm(prompt)

    except Exception as e:

        return f"""
# AI Recruiter Review Unavailable

ResumeForge could not connect to Ollama.

Possible reasons:

• Ollama is not running
• Llama 3.2 model is not installed
• Ollama service is unavailable

Error:
{str(e)}

To fix:

1. Open Terminal

2. Start Ollama

   ollama serve

3. Verify installed models

   ollama list

4. If llama3.2 is missing

   ollama pull llama3.2

After starting Ollama, rerun the analysis.
"""


# ==========================================================
# QUICK SUMMARY
# ==========================================================

def quick_summary(
    resume_text,
    job_description
):
    """
    Returns a concise recruiter summary.
    """

    prompt = f"""
You are a recruiter.

Resume:
{resume_text}

Job Description:
{job_description}

Write exactly 5 bullet points covering:

- Overall Match
- Biggest Strength
- Biggest Weakness
- Most Important Missing Skill
- Hiring Recommendation

Keep it under 150 words.
"""

    try:

        return call_llm(prompt)

    except Exception:

        return (
            "AI Summary unavailable. "
            "Please ensure Ollama is running."
        )


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

def generate_interview_questions(
    resume_text,
    job_description
):
    """
    Generate interview questions tailored to the resume.
    """

    prompt = f"""
You are a Senior Technical Interviewer.

Resume:
{resume_text}

Job Description:
{job_description}

Generate:

- 5 Technical Questions
- 3 HR Questions
- 2 Project-Based Questions

Number every question.
"""

    try:

        return call_llm(prompt)

    except Exception:

        return (
            "Interview questions could not be generated "
            "because Ollama is unavailable."
        )


# ==========================================================
# END OF FILE
# ==========================================================