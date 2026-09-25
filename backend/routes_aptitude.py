from flask import Blueprint, request, jsonify
from backend.models.aptitude_bank import (
    get_all_aptitude_questions,
    get_aptitude_categories,
    filter_aptitude_questions,
    generate_random_aptitude_test,
    evaluate_aptitude_test
)

aptitude_bp = Blueprint("aptitude", __name__)

@aptitude_bp.route("/categories", methods=["GET"])
def get_categories():
    """Returns available aptitude categories and topics"""
    try:
        categories = get_aptitude_categories()
        total_questions = len(get_all_aptitude_questions())
        return jsonify({
            "total_questions": total_questions,
            "categories": categories
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@aptitude_bp.route("/questions", methods=["GET", "POST"])
def get_questions():
    """
    Returns aptitude questions filtered by category, topic, difficulty, or mode ('practice' | 'test').
    In practice mode, includes answers, formulas, and step-by-step solutions.
    In test mode, sensitive fields are withheld.
    """
    if request.method == "POST":
        body = request.get_json() or {}
        category = body.get("category", "All")
        topic = body.get("topic", "All")
        difficulty = body.get("difficulty", "All")
        mode = body.get("mode", "practice")
        limit = int(body.get("limit", 50))
        shuffle = body.get("shuffle", True)
        if isinstance(shuffle, str):
            shuffle = shuffle.lower() in ["true", "1", "yes"]
    else:
        category = request.args.get("category", "All")
        topic = request.args.get("topic", "All")
        difficulty = request.args.get("difficulty", "All")
        mode = request.args.get("mode", "practice")
        limit = int(request.args.get("limit", 50))
        shuffle = request.args.get("shuffle", "true").lower() in ["true", "1", "yes"]

    questions = filter_aptitude_questions(
        category=category,
        topic=topic,
        difficulty=difficulty,
        mode=mode,
        limit=limit,
        shuffle=shuffle
    )

    return jsonify({
        "count": len(questions),
        "mode": mode,
        "questions": questions
    }), 200

@aptitude_bp.route("/test/start", methods=["POST"])
def start_aptitude_test():
    """Generates a timed balanced assessment test across all 4 aptitude domains (supports up to 50 questions)"""
    body = request.get_json() or {}
    total_count = int(body.get("question_count", 20))
    test_data = generate_random_aptitude_test(total_count=total_count)
    return jsonify(test_data), 200

@aptitude_bp.route("/test/submit", methods=["POST"])
def submit_aptitude_test():
    """
    Evaluates candidate answers submitted from test or practice session.
    Input: { "answers": { "quant-time-work-1": 1, ... } }
    Returns overall score, section breakdown, and full step-by-step explanations.
    """
    body = request.get_json() or {}
    answers = body.get("answers", {})

    if not answers:
        return jsonify({
            "total_questions": 0,
            "answered_count": 0,
            "correct_count": 0,
            "incorrect_count": 0,
            "overall_score": 0.0,
            "section_breakdown": {},
            "detailed_results": []
        }), 200

    results = evaluate_aptitude_test(answers)
    return jsonify(results), 200
