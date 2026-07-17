import pdfplumber
from docx import Document


def extract_text(uploaded_file):
    """
    Extract text from PDF or DOCX resume.
    """

    if uploaded_file.name.endswith(".pdf"):
        text = ""

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    elif uploaded_file.name.endswith(".docx"):
        document = Document(uploaded_file)

        text = "\n".join(
            paragraph.text for paragraph in document.paragraphs
        )

        return text

    return ""