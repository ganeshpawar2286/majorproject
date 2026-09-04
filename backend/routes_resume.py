import json
from flask import Blueprint, request, jsonify
from backend.models.resume_parser import resume_parser
from backend.database import SessionLocal, User, ResumeModel

resume_bp = Blueprint("resume", __name__)

def get_authorized_user_id(db, req):
    token = req.headers.get("Authorization", "").replace("Bearer ", "").strip()
    if token:
        user = db.query(User).filter(User.active_token == token).first()
        if user:
            return user.id
    return None

@resume_bp.route("/parse", methods=["POST"])
def parse_resume_route():
    """
    Accepts PDF or DOCX resume upload via multipart form-data, or raw text input via JSON.
    Strictly validates that the document is a Candidate Resume and rejects GST invoices, receipts, bills, etc.
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

        # STRICT DOCUMENT TYPE CLASSIFICATION & INTENT VALIDATION
        is_valid, validation_msg = resume_parser.validate_is_resume(extracted_text, filename=filename)
        if not is_valid:
            return jsonify({
                "error": validation_msg,
                "is_valid_resume": False
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
            if current_user_id:
                user_res = db.query(ResumeModel).filter(ResumeModel.user_id == current_user_id).first()
                skills_json = json.dumps(parsed_result.get("skills", []))
                breakdown_json = json.dumps(parsed_result.get("section_breakdown", {}))

                if user_res:
                    user_res.candidate_name = parsed_result.get("candidate_name")
                    user_res.email = parsed_result.get("email")
                    user_res.phone = parsed_result.get("phone")
                    user_res.skills = skills_json
                    user_res.predicted_category = parsed_result.get("predicted_category")
                    user_res.ats_score = parsed_result.get("ats_score", 0.0)
                    user_res.section_breakdown = breakdown_json
                    user_res.raw_text_snippet = parsed_result.get("raw_text_snippet")
                else:
                    new_res = ResumeModel(
                        user_id=current_user_id,
                        candidate_name=parsed_result.get("candidate_name"),
                        email=parsed_result.get("email"),
                        phone=parsed_result.get("phone"),
                        skills=skills_json,
                        predicted_category=parsed_result.get("predicted_category"),
                        ats_score=parsed_result.get("ats_score", 0.0),
                        section_breakdown=breakdown_json,
                        raw_text_snippet=parsed_result.get("raw_text_snippet")
                    )
                    db.add(new_res)
                db.commit()
        except Exception as db_err:
            db.rollback()
            print(f"Error persisting resume to DB: {db_err}")
        finally:
            db.close()

        return jsonify({
            "message": f"Resume parsed successfully using {parsed_result.get('engine_used', 'Local Engine')}.",
            "data": parsed_result
        }), 200

    except Exception as e:
        print(f"Error parsing resume: {e}")
        return jsonify({"error": f"Failed to parse resume file: {str(e)}"}), 500
