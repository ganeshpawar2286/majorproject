import json
from flask import Blueprint, request, jsonify
from backend.models.interview_evaluator import interview_evaluator
from backend.database import SessionLocal, User, ResumeModel, InterviewSessionModel, InterviewResponseModel

interview_bp = Blueprint("interview", __name__)

def get_authorized_user_id(db, req):
    token = req.headers.get("Authorization", "").replace("Bearer ", "").strip()
    if token:
        user = db.query(User).filter(User.active_token == token).first()
        if user:
            return user.id
    first_user = db.query(User).first()
    return first_user.id if first_user else 1

def get_candidate_resume_data(db, user_id):
    """Fetches and parses the candidate's latest uploaded resume."""
    resume = db.query(ResumeModel).filter(ResumeModel.user_id == user_id).order_by(ResumeModel.created_at.desc()).first()
    if not resume:
        resume = db.query(ResumeModel).order_by(ResumeModel.created_at.desc()).first()

    if resume and resume.parsed_json:
        try:
            parsed = json.loads(resume.parsed_json)
            parsed["filename"] = resume.filename
            return parsed
        except Exception as e:
            print(f"Error parsing resume JSON: {e}")
    return None

@interview_bp.route("/resume-profile", methods=["GET"])
def get_interview_resume_profile():
    """
    Returns the uploaded candidate resume profile for mock interview question personalization.
    """
    db = SessionLocal()
    try:
        user_id = get_authorized_user_id(db, request)
        resume_data = get_candidate_resume_data(db, user_id)
        if resume_data:
            return jsonify({
                "has_resume": True,
                "resume": {
                    "candidate_name": resume_data.get("candidate_name", "Candidate"),
                    "skills": resume_data.get("skills", []),
                    "predicted_category": resume_data.get("predicted_category", "INFORMATION-TECHNOLOGY"),
                    "experience_years": resume_data.get("experience_years", 2),
                    "education": resume_data.get("education", []),
                    "ats_score": resume_data.get("ats_score", 0),
                    "filename": resume_data.get("filename", "Uploaded Resume.pdf"),
                    "raw_text_snippet": resume_data.get("raw_text_snippet", "")
                }
            }), 200
        return jsonify({
            "has_resume": False,
            "resume": None,
            "message": "No resume found. Generic questions will be used until a resume is uploaded."
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@interview_bp.route("/start-session", methods=["POST"])
def start_interview_session():
    data = request.get_json() or {}
    category = data.get("category", "INFORMATION-TECHNOLOGY")
    target_role = data.get("target_role", "Software Engineer")
    initial_difficulty = data.get("difficulty", "Medium")
    resume_skills = data.get("resume_skills", [])
    candidate_name = data.get("candidate_name", "Candidate")
    resume_filename = data.get("filename", "")

    db = SessionLocal()
    try:
        current_user_id = get_authorized_user_id(db, request)

        # If resume skills not supplied in request payload, auto-load from DB
        if not resume_skills or len(resume_skills) == 0:
            db_resume = get_candidate_resume_data(db, current_user_id)
            if db_resume:
                resume_skills = db_resume.get("skills", [])
                if candidate_name == "Candidate" and db_resume.get("candidate_name"):
                    candidate_name = db_resume.get("candidate_name")
                if db_resume.get("predicted_category") and category == "INFORMATION-TECHNOLOGY":
                    category = db_resume.get("predicted_category")
                resume_filename = db_resume.get("filename", resume_filename)

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

        # Generate first question tailored specifically to uploaded resume skills & project stack
        q = interview_evaluator.generate_question(
            category=category,
            target_role=target_role,
            difficulty=initial_difficulty,
            resume_skills=resume_skills,
            candidate_name=candidate_name
        )

        return jsonify({
            "session_id": new_session.id,
            "category": category,
            "target_role": target_role,
            "difficulty": initial_difficulty,
            "question": q,
            "resume_tailored": bool(resume_skills),
            "resume_skills": resume_skills,
            "candidate_name": candidate_name,
            "resume_filename": resume_filename
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
    question_text = data.get("question", "") or data.get("question_text", "")
    target_keywords = data.get("target_keywords") or data.get("keywords") or []
    user_response = (data.get("user_response") or data.get("user_answer") or "").strip()
    current_difficulty = data.get("current_difficulty", "Medium")
    category = data.get("category", "INFORMATION-TECHNOLOGY")
    target_role = data.get("target_role", "Software Engineer")
    asked_questions = data.get("asked_questions", [])
    resume_skills = data.get("resume_skills", [])
    candidate_name = data.get("candidate_name", "Candidate")

    if not user_response:
        return jsonify({"error": "Candidate response text is required."}), 400

    db = SessionLocal()
    try:
        current_user_id = get_authorized_user_id(db, request)

        # Ensure resume skills remain active throughout session even if frontend omits them
        if not resume_skills or len(resume_skills) == 0:
            db_resume = get_candidate_resume_data(db, current_user_id)
            if db_resume:
                resume_skills = db_resume.get("skills", [])
                if candidate_name == "Candidate" and db_resume.get("candidate_name"):
                    candidate_name = db_resume.get("candidate_name")

        eval_result = interview_evaluator.evaluate_response(
            question_text, target_keywords, user_response, current_difficulty
        )

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

        # Generate next question dynamically tailored to uploaded resume skills
        next_question = interview_evaluator.generate_question(
            category=category,
            target_role=target_role,
            difficulty=eval_result["next_difficulty"],
            asked_ids=asked_questions,
            resume_skills=resume_skills,
            candidate_name=candidate_name
        )

        return jsonify({
            "evaluation": eval_result,
            "next_question": next_question,
            "resume_tailored": bool(resume_skills)
        }), 200
    except Exception as e:
        db.rollback()
        print(f"Error evaluating interview response: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()
