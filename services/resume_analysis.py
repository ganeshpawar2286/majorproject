import re
from collections import Counter

COMMON_SKILLS = [
    "python",
    "java",
    "javascript",
    "html",
    "css",
    "react",
    "flask",
    "django",
    "sql",
    "pandas",
    "numpy",
    "machine learning",
    "nlp",
    "excel",
    "communication",
    "leadership",
    "problem solving",
]

ROLE_BY_SKILL = {
    "react": "Frontend Developer",
    "html": "Frontend Developer",
    "css": "Frontend Developer",
    "javascript": "Frontend Developer",
    "python": "Python Developer",
    "flask": "Python Developer",
    "django": "Python Developer",
    "pandas": "Data Analyst",
    "numpy": "Data Analyst",
    "sql": "Data Analyst",
    "machine learning": "Machine Learning Engineer",
    "nlp": "Machine Learning Engineer",
}


def analyze_resume_text(resume_text):
    lowered = resume_text.lower()
    detected_skills = [skill for skill in COMMON_SKILLS if skill in lowered]

    if not detected_skills:
        detected_skills = ["communication", "problem solving"]

    word_count = len(re.findall(r"\w+", resume_text))
    skill_counter = Counter(detected_skills)
    suggested_role = Counter(ROLE_BY_SKILL.get(skill, "General Professional") for skill in detected_skills).most_common(1)[0][0]
    score = min(100, 40 + len(detected_skills) * 6 + min(word_count // 20, 20))

    return {
        "score": score,
        "word_count": word_count,
        "skills": sorted(skill_counter.keys()),
        "suggested_role": suggested_role,
        "strengths": [
            "Relevant skills detected",
            "Resume contains enough content for matching",
        ],
        "improvements": [
            "Add measurable achievements",
            "Include project outcomes and keywords",
            "Tailor the resume for a target role",
        ],
    }
