"""
ResumeForge Pro
Resume Parser
Supports PDF and DOCX
"""

from pathlib import Path
import re

import pdfplumber
from docx import Document

# ==========================================================
# TEXT CLEANING
# ==========================================================

def clean_text(text: str) -> str:
    """
    Clean extracted resume text.
    """

    if not text:
        return ""

    text = text.replace("\t", " ")
    text = text.replace("\r", " ")

    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ ]{2,}", " ", text)

    return text.strip()


# ==========================================================
# PDF PARSER
# ==========================================================

def extract_pdf_text(file):

    pages = []

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            txt = page.extract_text()

            if txt:

                pages.append(txt)

    return clean_text(
        "\n".join(pages)
    )


# ==========================================================
# DOCX PARSER
# ==========================================================

def extract_docx_text(file):

    document = Document(file)

    paragraphs = []

    for para in document.paragraphs:

        if para.text.strip():

            paragraphs.append(
                para.text.strip()
            )

    return clean_text(
        "\n".join(paragraphs)
    )


# ==========================================================
# FILE TYPE
# ==========================================================

def get_extension(file):

    if hasattr(file, "name"):

        return Path(file.name).suffix.lower()

    return ""
# ==========================================================
# MAIN EXTRACTION FUNCTION
# ==========================================================

def extract_text(file):
    """
    Automatically detects file type and extracts text.
    """

    if file is None:
        raise ValueError("No resume file uploaded.")

    extension = get_extension(file)

    if extension == ".pdf":
        return extract_pdf_text(file)

    elif extension == ".docx":
        return extract_docx_text(file)

    raise ValueError(
        f"Unsupported file format: {extension}"
    )


# ==========================================================
# WORD COUNT
# ==========================================================

def word_count(text):

    if not text:
        return 0

    return len(text.split())


# ==========================================================
# CHARACTER COUNT
# ==========================================================

def character_count(text):

    if not text:
        return 0

    return len(text)


# ==========================================================
# LINE COUNT
# ==========================================================

def line_count(text):

    if not text:
        return 0

    return len(
        text.splitlines()
    )


# ==========================================================
# RESUME STATISTICS
# ==========================================================

def resume_statistics(text):

    return {

        "word_count": word_count(text),

        "character_count": character_count(text),

        "line_count": line_count(text)

    }


# ==========================================================
# VALIDATION
# ==========================================================

def validate_resume(text):
    """
    Basic validation of extracted resume.
    """

    if not text:

        return False, "Resume is empty."

    if word_count(text) < 50:

        return False, "Resume appears too short."

    return True, "Resume parsed successfully."


# ==========================================================
# END OF FILE
# ==========================================================
