"""
ResumeForge Pro
Professional PDF Report Generator
"""

from pathlib import Path
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)

from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

# ==========================================================
# STYLES
# ==========================================================

styles = getSampleStyleSheet()

TITLE_STYLE = ParagraphStyle(
    "Title",
    parent=styles["Heading1"],
    alignment=TA_CENTER,
    fontSize=22,
    textColor=colors.black,
    spaceAfter=20,
)

HEADING_STYLE = ParagraphStyle(
    "Heading",
    parent=styles["Heading2"],
    fontSize=15,
    textColor=colors.HexColor("#111111"),
    spaceBefore=10,
    spaceAfter=8,
)

BODY_STYLE = styles["BodyText"]

# ==========================================================
# TABLE STYLE
# ==========================================================

TABLE_STYLE = TableStyle([

    ("BACKGROUND",(0,0),(-1,0),colors.black),

    ("TEXTCOLOR",(0,0),(-1,0),colors.white),

    ("GRID",(0,0),(-1,-1),1,colors.grey),

    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

    ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

    ("BOTTOMPADDING",(0,0),(-1,0),10),

    ("TOPPADDING",(0,1),(-1,-1),8),

    ("BOTTOMPADDING",(0,1),(-1,-1),8),

    ("ALIGN",(0,0),(-1,-1),"CENTER"),

])

# ==========================================================
# REPORT HEADER
# ==========================================================

def report_header(story):

    story.append(
        Paragraph(
            "ResumeForge Pro",
            TITLE_STYLE
        )
    )

    story.append(
        Paragraph(
            "Professional AI Resume Analysis Report",
            BODY_STYLE
        )
    )

    story.append(
        Paragraph(
            f"Generated : {datetime.now().strftime('%d %B %Y %I:%M %p')}",
            BODY_STYLE
        )
    )

    story.append(
        Spacer(1,0.3*inch)
    )

# ==========================================================
# SCORE TABLE
# ==========================================================

def score_table(

    ats_score,

    match_score,

    skill_score,

    keyword_score,

    overall_score

):

    data=[

        [
            "Metric",
            "Score"
        ],

        [
            "Overall Score",
            f"{overall_score}%"
        ],

        [
            "ATS Score",
            f"{ats_score}%"
        ],

        [
            "Resume Match",
            f"{match_score}%"
        ],

        [
            "Skill Coverage",
            f"{skill_score}%"
        ],

        [
            "Keyword Coverage",
            f"{keyword_score}%"
        ]

    ]

    table=Table(
        data,
        colWidths=[3.5*inch,2*inch]
    )

    table.setStyle(TABLE_STYLE)

    return table
# ==========================================================
# SKILLS TABLE
# ==========================================================

def skills_table(title, skills):

    if not skills:
        skills = ["None"]

    data = [["Skills"]]

    for skill in skills:
        data.append([skill.title()])

    table = Table(
        data,
        colWidths=[5.5 * inch]
    )

    table.setStyle(TABLE_STYLE)

    return [
        Paragraph(title, HEADING_STYLE),
        table,
        Spacer(1, 0.2 * inch)
    ]


# ==========================================================
# FEEDBACK SECTION
# ==========================================================

def feedback_section(title, feedback):

    items = []

    items.append(
        Paragraph(title, HEADING_STYLE)
    )

    if isinstance(feedback, list):

        for line in feedback:

            items.append(
                Paragraph(f"• {line}", BODY_STYLE)
            )

    else:

        items.append(
            Paragraph(str(feedback), BODY_STYLE)
        )

    items.append(
        Spacer(1, 0.2 * inch)
    )

    return items


# ==========================================================
# MAIN REPORT
# ==========================================================

def generate_report(

    output_path,

    ats_score,

    match_score,

    skills_found,

    missing_skills,

    keyword_score,

    ai_review,

    overall_score=None,

    feedback=None

):

    if overall_score is None:

        overall_score = round(

            (ats_score + match_score + keyword_score) / 3,

            2

        )

    if feedback is None:

        feedback = []

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    doc = SimpleDocTemplate(str(output_path))

    story = []

    # ======================================================
    # HEADER
    # ======================================================

    report_header(story)

    # ======================================================
    # SCORE TABLE
    # ======================================================

    story.append(
        Paragraph(
            "Resume Score Summary",
            HEADING_STYLE
        )
    )

    story.append(

        score_table(

            ats_score,

            match_score,

            len(skills_found),

            keyword_score,

            overall_score

        )

    )

    story.append(
        Spacer(1, 0.25 * inch)
    )

    # ======================================================
    # SKILLS
    # ======================================================

    story.extend(

        skills_table(

            "Detected Skills",

            skills_found

        )

    )

    story.extend(

        skills_table(

            "Missing Skills",

            missing_skills

        )

    )

    # ======================================================
    # ATS FEEDBACK
    # ======================================================

    story.extend(

        feedback_section(

            "ATS Recommendations",

            feedback

        )

    )

    # ======================================================
    # AI REVIEW
    # ======================================================

    story.append(

        Paragraph(

            "AI Recruiter Review",

            HEADING_STYLE

        )

    )

    story.append(

        Paragraph(

            str(ai_review).replace("\n", "<br/>"),

            BODY_STYLE

        )

    )

    story.append(
        Spacer(1, 0.3 * inch)
    )

    # ======================================================
    # FOOTER
    # ======================================================

    story.append(

        Paragraph(

            "<b>Generated by ResumeForge Pro</b>",

            BODY_STYLE

        )

    )

    story.append(

        Paragraph(

            "AI Resume Analyzer | ATS Checker | Recruiter Insights",

            BODY_STYLE

        )

    )

    # ======================================================
    # BUILD PDF
    # ======================================================

    doc.build(story)

    return str(output_path)


# ==========================================================
# END OF FILE
# ==========================================================