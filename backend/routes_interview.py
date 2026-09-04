import json
from flask import Blueprint, request, jsonify
from backend.models.interview_evaluator import interview_evaluator
from backend.database import SessionLocal, User, InterviewSessionModel, InterviewResponseModel

interview_bp = Blueprint("interview", __name__)

def get_authorized_user_id(db, req):
    token = req.headers.get("Authorization", "").replace("Bearer ", "").strip()
    if token:
        user = db.query(User).filter(User.active_token == token).first()
        if user:
            return user.id
    first_user = db.query(User).first()
    return first_user.id if first_user else 1

@interview_bp.route("/start-session", methods=["POST"])
def start_interview_session():
    data = request.get_json() or {}
    category = data.get("category", "INFORMATION-TECHNOLOGY")
    target_role = data.get("target_role", "Software Engineer")
    initial_difficulty = data.get("difficulty", "Medium")
    resume_skills = data.get("resume_skills", [])
    candidate_name = data.get("candidate_name", "Candidate")

    db = SessionLocal()
    try:
        current_user_id = get_authorized_user_id(db, request)
        new_session = InterviewSessionModel(
            user_id=current_user_id,
            category=category,
            target_role=target_role,
            current_difficulty=initial_difficulty,
            completed=False
        )
        db.add(new_session)
        db.commit()
        db.refresh(new_session)

        # Generate first question tailored to uploaded resume skills
        q = interview_evaluator.generate_question(
            category, target_role, initial_difficulty, resume_skills=resume_skills, candidate_name=candidate_name
        )

        return jsonify({
            "session_id": new_session.id,
            "category": category,
            "target_role": target_role,
            "difficulty": initial_difficulty,
            "question": q
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@interview_bp.route("/evaluate-answer", methods=["POST"])
def evaluate_answer():
    data = request.get_json() or {}
    session_id = data.get("session_id")
    question_text = data.get("question", "")
    target_keywords = data.get("target_keywords", [])
    user_response = data.get("user_response", "").strip()
    current_difficulty = data.get("current_difficulty", "Medium")
    category = data.get("category", "INFORMATION-TECHNOLOGY")
    target_role = data.get("target_role", "Software Engineer")
    asked_questions = data.get("asked_questions", [])
    resume_skills = data.get("resume_skills", [])

    if not user_response:
        return jsonify({"error": "Candidate response text is required."}), 400

    eval_result = interview_evaluator.evaluate_response(
        question_text, target_keywords, user_response, current_difficulty
    )

    db = SessionLocal()
    try:
        if session_id:
            resp_model = InterviewResponseModel(
                session_id=session_id,
                question=question_text,
                question_category=category,
                user_response=user_response,
                overall_score=eval_result["overall_score"],
                keyword_score=eval_result["keyword_score"],
                coherence_score=eval_result["coherence_score"],
                fluency_score=eval_result["fluency_score"],
                confidence_score=eval_result["confidence_score"],
                feedback_json=json.dumps({
                    "feedback": eval_result["feedback"],
                    "strengths": eval_result["strengths"],
                    "areas_for_improvement": eval_result["areas_for_improvement"]
                })
            )
            db.add(resp_model)

            session = db.query(InterviewSessionModel).filter(InterviewSessionModel.id == session_id).first()
            if session:
                session.current_difficulty = eval_result["next_difficulty"]
                all_resps = db.query(InterviewResponseModel).filter(InterviewResponseModel.session_id == session_id).all()
                if all_resps:
                    avg_score = sum(r.overall_score for r in all_resps) / len(all_resps)
                    session.total_score = round(avg_score, 1)
                    if avg_score >= 75:
                        session.performance_tier = "High"
                    elif avg_score >= 50:
                        session.performance_tier = "Medium"
                    else:
                        session.performance_tier = "Low"

            db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error saving interview response DB: {e}")
    finally:
        db.close()

    next_question = interview_evaluator.generate_question(
        category, target_role, eval_result["next_difficulty"], asked_ids=asked_questions, resume_skills=resume_skills
    )

    return jsonify({
        "evaluation": eval_result,
        "next_question": next_question
    }), 200
