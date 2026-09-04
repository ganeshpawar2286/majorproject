from flask import Blueprint, request, jsonify
from backend.models.job_matcher import job_matcher
from backend.models.dataset_loader import dataset_loader

jobs_bp = Blueprint("jobs", __name__)

@jobs_bp.route("/recommendations", methods=["POST"])
def get_job_recommendations():
    """
    Takes parsed resume data (skills, category, snippet) and matches against all 760 jobs in dataset.
    Returns up to top_n (default 1000) job recommendations with acceptance probabilities and skill gaps.
    """
    data = request.get_json() or {}
    resume_data = data.get("resume_data", {})
    top_n = data.get("top_n", 1000)

    if not resume_data:
        # Fallback default resume features
        resume_data = {
            "skills": ["Python", "SQL", "JavaScript", "React", "Git", "AWS"],
            "predicted_category": "INFORMATION-TECHNOLOGY",
            "raw_text_snippet": "Software Engineer experienced in Python, Web Development, and Databases."
        }

    recommendations = job_matcher.predict_company_acceptance(resume_data, top_n=top_n)

    return jsonify({
        "message": f"Found top {len(recommendations)} company job matches out of all 760 jobs in dataset.",
        "recommendations": recommendations,
        "categories": dataset_loader.get_categories()
    }), 200

@jobs_bp.route("/match-custom", methods=["POST"])
def match_custom_job():
    """
    Matches candidate resume against a specific target job posting provided by user.
    """
    data = request.get_json() or {}
    resume_data = data.get("resume_data", {})
    job_title = data.get("job_title", "Target Position")
    job_description = data.get("job_description", "")

    if not job_description:
        return jsonify({"error": "Job description text is required."}), 400

    match_result = job_matcher.match_custom_job_description(resume_data, job_title, job_description)

    return jsonify({
        "message": "Custom job description evaluation completed.",
        "match_result": match_result
    }), 200
