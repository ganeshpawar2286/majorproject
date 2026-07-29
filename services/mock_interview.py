def generate_questions(role, skills):
    role = role or "General Professional"
    skill_focus = skills[0] if skills else "your recent project"

    return [
        f"Tell me about yourself for the {role} role.",
        f"How have you used {skill_focus} in a project or internship?",
        "Describe a challenge you faced and how you solved it.",
        "Why are you interested in this role and this company?",
    ]


def generate_interview_feedback(resume_text, analysis):
    length = len(resume_text.split())

    if length < 80:
        content_feedback = "Your resume summary is brief. Add more project detail and impact statements."
    else:
        content_feedback = "Your resume has enough detail for interview preparation. Focus on concise storytelling."

    return {
        "overall": min(100, analysis["score"] + 5),
        "content_feedback": content_feedback,
        "communication_feedback": "Practice answering in short, structured points using STAR format.",
        "next_steps": [
            "Refine your resume summary",
            "Practice answers aloud",
            "Review role-specific technical questions",
        ],
    }
