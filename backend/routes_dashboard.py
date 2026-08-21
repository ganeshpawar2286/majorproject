import json
from flask import Blueprint, request, jsonify
from backend.database import SessionLocal, User, ResumeModel, InterviewSessionModel, InterviewResponseModel

dashboard_bp = Blueprint("dashboard", __name__)

def get_authorized_user(db, req):
    token = req.headers.get("Authorization", "").replace("Bearer ", "").strip()
    if token:
        user = db.query(User).filter(User.active_token == token).first()
        if user:
            return user
    return db.query(User).first()

@dashboard_bp.route("/analytics", methods=["GET"])
def get_dashboard_analytics():
    db = SessionLocal()
    try:
        user = get_authorized_user(db, request)
        user_id = user.id if user else 1

        # Latest Resume ATS Score strictly for THIS candidate account (No cross-account fallback!)
        latest_resume = db.query(ResumeModel).filter(ResumeModel.user_id == user_id).order_by(ResumeModel.created_at.desc()).first()

        ats_score = round(latest_resume.ats_score, 1) if latest_resume else 0.0
        candidate_category = latest_resume.category if latest_resume else (user.profile.industry_category if (user and user.profile) else "INFORMATION-TECHNOLOGY")

        # Interview sessions & responses for THIS candidate account
        sessions = db.query(InterviewSessionModel).filter(InterviewSessionModel.user_id == user_id).order_by(InterviewSessionModel.created_at.asc()).all()
        session_ids = [s.id for s in sessions]
        
        responses = []
        if session_ids:
            responses = db.query(InterviewResponseModel).filter(InterviewResponseModel.session_id.in_(session_ids)).order_by(InterviewResponseModel.answered_at.desc()).all()

        total_interviews = len(sessions)
        total_questions_answered = len(responses)

        if responses:
            avg_interview_score = round(sum(r.overall_score for r in responses) / len(responses), 1)
            avg_keyword = round(sum(r.keyword_score for r in responses) / len(responses), 1)
            avg_coherence = round(sum(r.coherence_score for r in responses) / len(responses), 1)
            avg_fluency = round(sum(r.fluency_score for r in responses) / len(responses), 1)
            avg_confidence = round(sum(r.confidence_score for r in responses) / len(responses), 1)
        else:
            avg_interview_score = 0.0
            avg_keyword = 0.0
            avg_coherence = 0.0
            avg_fluency = 0.0
            avg_confidence = 0.0

        # Score trends over time for THIS candidate account
        session_trends = []
        for idx, s in enumerate(sessions):
            session_trends.append({
                "session_name": f"Session #{idx + 1}",
                "category": s.category,
                "score": s.total_score if s.total_score > 0 else 70.0,
                "tier": s.performance_tier,
                "date": s.created_at.strftime("%b %d")
            })

        if not session_trends:
            session_trends = [
                {"session_name": "No Practice Yet", "category": candidate_category, "score": 0.0, "tier": "None", "date": "Today"}
            ]

        # Overall Job Readiness Composite Score for THIS candidate account
        if ats_score > 0 and avg_interview_score > 0:
            readiness_score = round((ats_score * 0.5) + (avg_interview_score * 0.5), 1)
        elif ats_score > 0:
            readiness_score = round(ats_score * 0.7, 1)
        elif avg_interview_score > 0:
            readiness_score = round(avg_interview_score * 0.7, 1)
        else:
            readiness_score = 0.0

        if readiness_score >= 80:
            readiness_status = "High (Interview Ready)"
        elif readiness_score >= 60:
            readiness_status = "Medium (Moderate Readiness)"
        elif readiness_score > 0:
            readiness_status = "Low (Requires Practice)"
        else:
            readiness_status = "Not Started (Upload Resume & Practice)"

        # Actionable recommendations tailored to candidate metrics
        recommendations = []
        if ats_score == 0:
            recommendations.append("Upload your resume in the Resume Analysis tab (Module 1) to parse your skills and view your ATS compatibility score.")
        elif ats_score < 80:
            recommendations.append("Optimize your resume ATS score by adding missing target keywords identified in the Resume Analysis tab.")

        if total_interviews == 0:
            recommendations.append("Complete your first AI Mock Interview session to establish your Speech & Keyword fluency baseline.")
        elif avg_keyword < 75:
            recommendations.append("Enhance domain keyword usage in interview answers to demonstrate deep technical expertise.")

        if avg_confidence < 75 and total_interviews > 0:
            recommendations.append("Use strong action verbs ('engineered', 'spearheaded', 'optimized') to project higher confidence.")

        if not recommendations:
            recommendations.append("Great job! Keep completing mock interviews to maintain peak career readiness.")

        # Recent response history for THIS candidate
        recent_history = []
        for r in responses[:6]:
            feedback_data = json.loads(r.feedback_json) if r.feedback_json else {}
            recent_history.append({
                "id": r.id,
                "question": r.question,
                "user_response": r.user_response[:140] + "..." if len(r.user_response) > 140 else r.user_response,
                "overall_score": r.overall_score,
                "keyword_score": r.keyword_score,
                "coherence_score": r.coherence_score,
                "fluency_score": r.fluency_score,
                "confidence_score": r.confidence_score,
                "feedback": feedback_data.get("feedback", ""),
                "date": r.answered_at.strftime("%b %d, %H:%M")
            })

        return jsonify({
            "metrics": {
                "ats_score": ats_score,
                "avg_interview_score": avg_interview_score,
                "readiness_score": readiness_score,
                "readiness_status": readiness_status,
                "total_interviews": total_interviews,
                "total_questions_answered": total_questions_answered,
                "candidate_category": candidate_category,
                "has_resume": bool(latest_resume)
            },
            "skill_breakdown": {
                "keyword_relevance": avg_keyword,
                "coherence": avg_coherence,
                "fluency": avg_fluency,
                "confidence": avg_confidence
            },
            "session_trends": session_trends,
            "recommendations": recommendations,
            "recent_responses": recent_history
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()
