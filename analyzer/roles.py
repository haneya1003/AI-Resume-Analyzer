ROLE_SKILLS = {


"AI/ML Engineer":[
"python",
"machine learning",
"deep learning",
"tensorflow",
"pytorch"
],


"Data Analyst":[
"python",
"sql",
"excel",
"power bi",
"tableau"
],


"Data Scientist":[
"python",
"machine learning",
"pandas",
"numpy"
],


"Cloud AI Engineer":[
"aws",
"azure",
"docker",
"kubernetes"
]


}



def recommend_roles(skills):

    skills=[
        s.lower()
        for s in skills
    ]


    results=[]


    for role, required in ROLE_SKILLS.items():

        count=0


        for skill in required:

            if skill in skills:
                count += 1


        score = (
            count /
            len(required)
        ) * 100


        results.append({

            "role":role,

            "score":round(score,2)

        })


    return sorted(

        results,

        key=lambda x:x["score"],

        reverse=True

    )