import json
from flask import Blueprint, request, jsonify
from models.resume_parser import resume_parser
from backend.database import SessionLocal, User, ResumeModel

resume_bp = Blueprint("resume", __name__)

def get_authorized_user_id(db, req):
    token = req.headers.get("Authorization", "").replace("Bearer ", "").strip()
    if token:
        user = db.query(User).filter(User.active_token == token).first()
        if user:
            return user.id
    first_user = db.query(User).first()
    return first_user.id if first_user else 1

@resume_bp.route("/parse", methods=["POST"])
def parse_resume_route():
    """
    Accepts PDF or DOCX resume upload via multipart form-data, or raw text input via JSON.
    Supports engine parameter: 'local' (default), 'affinda', 'rchilli', or 'textkernel'.
    """
    try:
        extracted_text = ""
        filename = "pasted_resume.txt"
        file_bytes = None

        if request.is_json:
            data = request.get_json(silent=True) or {}
        else:
            data = {}

        engine = request.form.get("engine") or data.get("engine") or "local"
        api_key = request.form.get("api_key") or data.get("api_key")

        if "file" in request.files:
            file = request.files["file"]
            filename = file.filename or "uploaded_resume.pdf"
            file_bytes = file.read()
            extracted_text = resume_parser.extract_text_from_file(file_bytes, filename)
        else:
            extracted_text = data.get("text", "")
            filename = data.get("filename", "custom_resume.txt")

        if not extracted_text or len(extracted_text.strip()) < 10:
            return jsonify({
                "error": "Could not extract readable text from the uploaded file. Please ensure it is a text-based PDF or DOCX file."
            }), 400

        parsed_result = resume_parser.parse_resume(
            extracted_text,
            engine=engine.lower(),
            file_bytes=file_bytes,
            filename=filename,
            api_key=api_key
        )

        db = SessionLocal()
        try:
            current_user_id = get_authorized_user_id(db, request)
            new_resume = ResumeModel(
                user_id=current_user_id,
                filename=filename,
                candidate_name=parsed_result["candidate_name"],
                category=parsed_result["predicted_category"],
                ats_score=parsed_result["ats_score"],
                parsed_json=json.dumps(parsed_result)
            )
            db.add(new_resume)
            db.commit()
            db.refresh(new_resume)
            parsed_result["resume_id"] = new_resume.id
        except Exception as e:
            db.rollback()
            print(f"Error saving resume DB: {e}")
        finally:
            db.close()

        return jsonify({
            "message": f"Resume analyzed using {parsed_result.get('engine_used', 'NLP Engine')}.",
            "data": parsed_result
        }), 200

    except Exception as err:
        print(f"Unhandled error in /parse: {err}")
        return jsonify({
            "error": f"An error occurred while parsing the resume: {str(err)}"
        }), 500

@resume_bp.route("/history", methods=["GET"])
def get_resume_history():
    db = SessionLocal()
    try:
        current_user_id = get_authorized_user_id(db, request)
        resumes = db.query(ResumeModel).filter(ResumeModel.user_id == current_user_id).order_by(ResumeModel.created_at.desc()).all()
        history = []
        for r in resumes:
            history.append({
                "id": r.id,
                "filename": r.filename,
                "candidate_name": r.candidate_name,
                "category": r.category,
                "ats_score": r.ats_score,
                "created_at": r.created_at.strftime("%Y-%m-%d %H:%M")
            })
        return jsonify({"history": history}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()
