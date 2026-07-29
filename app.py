from flask import Flask, render_template, request

from services.recommendation import recommend_jobs
from services.resume_analysis import analyze_resume_text
from services.mock_interview import generate_interview_feedback, generate_questions
from services.resume_parser import extract_resume_text, format_resume_preview

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

SAMPLE_JOBS = [
    {
        "title": "Python Developer",
        "company": "TechNova",
        "skills": ["python", "flask", "sql", "api"],
        "location": "Remote",
    },
    {
        "title": "Data Analyst",
        "company": "InsightWorks",
        "skills": ["python", "pandas", "excel", "sql"],
        "location": "Hybrid",
    },
    {
        "title": "Frontend Developer",
        "company": "BrightUI",
        "skills": ["html", "css", "javascript", "react"],
        "location": "On-site",
    },
    {
        "title": "Machine Learning Intern",
        "company": "AI Labs",
        "skills": ["python", "machine learning", "nlp", "data"],
        "location": "Remote",
    },
]

@app.route("/", methods=["GET", "POST"])
def index():
    analysis = None
    recommendations = []
    questions = []
    feedback = None
    resume_text = ""
    target_role = ""
    uploaded_filename = ""
    error_message = ""
    resume_preview = ""

    if request.method == "POST":
        target_role = request.form.get("target_role", "").strip()
        resume_file = request.files.get("resume_file")

        if resume_file and resume_file.filename:
            uploaded_filename = resume_file.filename
            try:
                resume_text = extract_resume_text(resume_file)
                resume_preview = format_resume_preview(resume_text)
            except ValueError as exc:
                error_message = str(exc)
        else:
            error_message = "Please upload a resume file in PDF, DOCX, or TXT format."

        if not error_message and resume_text:
            analysis = analyze_resume_text(resume_text)
            recommendations = recommend_jobs(analysis["skills"], SAMPLE_JOBS, target_role)
            questions = generate_questions(target_role or analysis["suggested_role"], analysis["skills"])
            feedback = generate_interview_feedback(resume_text, analysis)

    return render_template(
        "index.html",
        analysis=analysis,
        recommendations=recommendations,
        questions=questions,
        feedback=feedback,
        resume_text=resume_text,
        resume_preview=resume_preview,
        target_role=target_role,
        uploaded_filename=uploaded_filename,
        error_message=error_message,
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
