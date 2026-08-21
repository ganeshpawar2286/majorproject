import secrets
import random
import json
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from backend.database import SessionLocal, User, UserProfile, ResumeModel

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json() or {}
    username = data.get("username", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "").strip()

    if not username or not email or not password:
        return jsonify({"error": "Username, email, and password are required."}), 400

    db = SessionLocal()
    try:
        # Enforce strictly 1 account per email ID & username
        existing_user = db.query(User).filter(
            (User.username == username) | (User.email == email)
        ).first()
        
        if existing_user:
            if existing_user.email.lower() == email:
                return jsonify({"error": "An account with this email address already exists. Only 1 account per email ID is allowed."}), 409
            return jsonify({"error": "Username already taken. Please choose another username."}), 409

        hashed_pw = generate_password_hash(password)
        new_user = User(
            username=username,
            email=email,
            password_hash=hashed_pw
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Initialize User Profile for new account
        new_profile = UserProfile(
            user_id=new_user.id,
            full_name=username.title(),
            headline=f"Job Candidate & Professional",
            target_role="Software Engineer",
            industry_category="INFORMATION-TECHNOLOGY",
            bio="Welcome to my PrepWise AI candidate profile.",
            skills_json="[]"
        )
        db.add(new_profile)
        db.commit()

        return jsonify({
            "message": "Account created successfully! Please sign in.",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email
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
    username_or_email = data.get("username", "").strip().lower()
    password = data.get("password", "").strip()

    if not username_or_email or not password:
        return jsonify({"error": "Email/Username and password are required."}), 400

    db = SessionLocal()
    try:
        user = db.query(User).filter(
            (User.username == username_or_email) | (User.email == username_or_email)
        ).first()

        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({"error": "Invalid email address/username or password."}), 401

        # Enforce Single Active Session per Mail ID
        new_token = f"pw_session_{user.id}_{secrets.token_hex(16)}"
        user.active_token = new_token
        user.last_login_at = datetime.utcnow()

        # Ensure profile exists for account
        if not user.profile:
            user.profile = UserProfile(
                user_id=user.id,
                full_name=user.username.title(),
                target_role="Software Engineer",
                industry_category="INFORMATION-TECHNOLOGY"
            )

        db.commit()

        return jsonify({
            "message": "Login successful!",
            "token": new_token,
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
        return jsonify({"error": "Please enter your registered email address."}), 400

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return jsonify({"error": "No account found with this email address. Please check your spelling or sign up."}), 444

        reset_code = f"{random.randint(100000, 999999)}"
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
    Returns isolated user profile details for current logged-in account.
    """
    token = request.headers.get("Authorization", "").replace("Bearer ", "").strip()
    db = SessionLocal()
    try:
        user = None
        if token:
            user = db.query(User).filter(User.active_token == token).first()
        if not user:
            user = db.query(User).first()

        if not user:
            return jsonify({"error": "No user account found."}), 404

        if not user.profile:
            user.profile = UserProfile(user_id=user.id, full_name=user.username.title())
            db.commit()

        skills = []
        try:
            skills = json.loads(user.profile.skills_json) if user.profile.skills_json else []
        except Exception:
            skills = []

        # Get latest parsed resume for account
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
                "github_url": user.profile.github_url or "",
                "portfolio_url": user.profile.portfolio_url or "",
                "created_at": user.created_at.strftime("%Y-%m-%d") if user.created_at else "2026-01-01"
            },
            "latest_resume": resume_data
        }), 200
    finally:
        db.close()

@auth_bp.route("/profile", methods=["PUT"])
def update_profile():
    """
    Updates user profile details for current logged-in account.
    """
    token = request.headers.get("Authorization", "").replace("Bearer ", "").strip()
    data = request.get_json() or {}

    db = SessionLocal()
    try:
        user = None
        if token:
            user = db.query(User).filter(User.active_token == token).first()
        if not user:
            user = db.query(User).first()

        if not user:
            return jsonify({"error": "No user account found."}), 404

        if not user.profile:
            user.profile = UserProfile(user_id=user.id, full_name=user.username.title())
            db.add(user.profile)

        if "full_name" in data: user.profile.full_name = data["full_name"].strip()
        if "headline" in data: user.profile.headline = data["headline"].strip()
        if "target_role" in data: user.profile.target_role = data["target_role"].strip()
        if "industry_category" in data: user.profile.industry_category = data["industry_category"].strip()
        if "bio" in data: user.profile.bio = data["bio"].strip()
        if "skills" in data: user.profile.skills_json = json.dumps(data["skills"])
        if "phone" in data: user.profile.phone = data["phone"].strip()
        if "linkedin_url" in data: user.profile.linkedin_url = data["linkedin_url"].strip()
        if "github_url" in data: user.profile.github_url = data["github_url"].strip()
        if "portfolio_url" in data: user.profile.portfolio_url = data["portfolio_url"].strip()

        db.commit()

        return jsonify({
            "message": "User profile updated successfully!",
            "profile": {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "full_name": user.profile.full_name,
                "headline": user.profile.headline,
                "target_role": user.profile.target_role,
                "industry_category": user.profile.industry_category,
                "bio": user.profile.bio,
                "skills": json.loads(user.profile.skills_json) if user.profile.skills_json else [],
                "phone": user.profile.phone,
                "linkedin_url": user.profile.linkedin_url,
                "github_url": user.profile.github_url,
                "portfolio_url": user.profile.portfolio_url
            }
        }), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()
