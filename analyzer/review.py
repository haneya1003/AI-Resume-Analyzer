def resume_strengths(skills):

    strengths=[]


    skills=[
        s.lower()
        for s in skills
    ]


    if "python" in skills:
        strengths.append(
            "Strong Python programming foundation"
        )


    if "machine learning" in skills:
        strengths.append(
            "Machine Learning knowledge detected"
        )


    if "sql" in skills:
        strengths.append(
            "Database and SQL skills"
        )


    if "aws" in skills or "azure" in skills:
        strengths.append(
            "Cloud platform exposure"
        )


    if "docker" in skills:
        strengths.append(
            "Deployment knowledge using Docker"
        )


    return strengths