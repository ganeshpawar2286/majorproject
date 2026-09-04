import json
import secrets
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from backend.database import SessionLocal, User, UserProfile, ResumeModel

auth_bp = Blueprint("auth", __name__)

def generate_token(user_id):
    return f"pw_session_{user_id}_{secrets.token_hex(16)}"

@auth_bp.route("/register", methods=["POST"])
@auth_bp.route("/signup", methods=["POST"])
def register():
    data = request.get_json() or {}
    username = data.get("username", "").strip()
    email = data.get("email", "").strip().lower()
    if not email and "@" in username:
        email = username
    if not username:
        username = email.split("@")[0] if "@" in email else email

    password = data.get("password", "").strip()

    if not username or not email or not password:
        return jsonify({"error": "All fields (username, email, password) are required."}), 400

    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters long."}), 400

    db = SessionLocal()
    try:
        existing_user = db.query(User).filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return jsonify({"error": "Username or email is already registered. Please sign in."}), 400

        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        # Initialize profile
        profile = UserProfile(user_id=user.id, full_name=username.title())
        db.add(profile)
        db.commit()

        # Issue single session token
        token = generate_token(user.id)
        user.active_token = token
        db.commit()

        return jsonify({
            "message": "Account registered successfully!",
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email_or_user = (data.get("email") or data.get("username") or "").strip().lower()
    password = data.get("password", "").strip()

    if not email_or_user or not password:
        return jsonify({"error": "Email/Username and password are required."}), 400

    db = SessionLocal()
    try:
        user = db.query(User).filter(
            (User.email == email_or_user) | (User.username == email_or_user)
        ).first()

        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({"error": "Invalid email/username or password."}), 401

        # Enforce single session policy
        token = generate_token(user.id)
        user.active_token = token
        db.commit()

        return jsonify({
            "message": "Login successful!",
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json() or {}
    email = data.get("email", "").strip().lower()

    if not email:
        return jsonify({"error": "Registered email is required."}), 400

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return jsonify({"error": "No user account registered with that email."}), 404

        import random
        reset_code = str(random.randint(100000, 999999))
        user.reset_token = reset_code
        user.reset_token_expiry = datetime.utcnow() + timedelta(minutes=15)
        db.commit()

        return jsonify({
            "message": f"Password reset verification code generated for {email}.",
            "reset_code": reset_code,
            "email": email
        }), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@auth_bp.route("/reset-password", methods=["POST"])
def reset_password():
    data = request.get_json() or {}
    email = data.get("email", "").strip().lower()
    reset_code = data.get("reset_code", "").strip()
    new_password = data.get("new_password", "").strip()

    if not email or not reset_code or not new_password:
        return jsonify({"error": "Email, verification code, and new password are required."}), 400

    if len(new_password) < 6:
        return jsonify({"error": "New password must be at least 6 characters long."}), 400

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return jsonify({"error": "User account not found."}), 404

        if not user.reset_token or user.reset_token != reset_code:
            return jsonify({"error": "Invalid or incorrect password reset verification code."}), 400

        if user.reset_token_expiry and datetime.utcnow() > user.reset_token_expiry:
            return jsonify({"error": "Verification code has expired. Please request a new code."}), 400

        user.password_hash = generate_password_hash(new_password)
        user.reset_token = None
        user.reset_token_expiry = None
        user.active_token = None
        db.commit()

        return jsonify({
            "message": "Password reset successful! You can now log in with your new password."
        }), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@auth_bp.route("/verify-session", methods=["POST"])
def verify_session():
    data = request.get_json() or {}
    token = data.get("token", "")

    if not token or token.startswith("guest"):
        return jsonify({"valid": True, "user": {"id": 1, "username": "Guest Candidate", "email": "guest@prepwise.ai"}}), 200

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.active_token == token).first()
        if not user:
            return jsonify({
                "valid": False,
                "error": "Session expired or logged in from another device/browser. Single session policy enforced."
            }), 401

        return jsonify({
            "valid": True,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }), 200
    finally:
        db.close()

@auth_bp.route("/profile", methods=["GET"])
def get_profile():
    """
    Returns isolated user profile details strictly for current logged-in account.
    """
    token = request.headers.get("Authorization", "").replace("Bearer ", "").strip()
    db = SessionLocal()
    try:
        user = None
        if token:
            user = db.query(User).filter(User.active_token == token).first()
        
        if not user:
            return jsonify({"error": "Unauthorized session token."}), 401

        if not user.profile:
            user.profile = UserProfile(user_id=user.id, full_name=user.username.title())
            db.commit()

        skills = []
        try:
            skills = json.loads(user.profile.skills_json) if user.profile.skills_json else []
        except Exception:
            skills = []

        # Get latest parsed resume STRICTLY for THIS authenticated user
        latest_resume = db.query(ResumeModel).filter(ResumeModel.user_id == user.id).order_by(ResumeModel.id.desc()).first()
        resume_data = json.loads(latest_resume.parsed_json) if (latest_resume and latest_resume.parsed_json) else None

        return jsonify({
            "profile": {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "full_name": user.profile.full_name or user.username.title(),
                "headline": user.profile.headline or "Job Candidate & Professional",
                "target_role": user.profile.target_role or "Software Engineer",
                "industry_category": user.profile.industry_category or "INFORMATION-TECHNOLOGY",
                "bio": user.profile.bio or "",
                "skills": skills,
                "phone": user.profile.phone or "",
                "linkedin_url": user.profile.linkedin_url or "",
                "github_url": user.profile.github_url or ""
            },
            "latest_resume": resume_data
        }), 200
    finally:
        db.close()
