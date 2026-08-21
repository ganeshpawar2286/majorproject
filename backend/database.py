import os
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "backend", "prepwise.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

ENGINE = create_engine(f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(200), nullable=False)
    active_token = Column(String(255), nullable=True) # Enforces single active session per mail ID
    reset_token = Column(String(100), nullable=True)  # Forgot password OTP/Token
    reset_token_expiry = Column(DateTime, nullable=True)
    last_login_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    profile = relationship("UserProfile", uselist=False, back_populates="user", cascade="all, delete-orphan")
    resumes = relationship("ResumeModel", back_populates="user", cascade="all, delete-orphan")
    interview_sessions = relationship("InterviewSessionModel", back_populates="user", cascade="all, delete-orphan")

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    full_name = Column(String(100), default="")
    headline = Column(String(150), default="")
    target_role = Column(String(100), default="Software Engineer")
    industry_category = Column(String(100), default="INFORMATION-TECHNOLOGY")
    bio = Column(Text, default="")
    skills_json = Column(Text, default="[]")
    phone = Column(String(50), default="")
    linkedin_url = Column(String(255), default="")
    github_url = Column(String(255), default="")
    portfolio_url = Column(String(255), default="")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="profile")

class ResumeModel(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    filename = Column(String(255), nullable=False)
    candidate_name = Column(String(100), default="Candidate")
    category = Column(String(100), default="INFORMATION-TECHNOLOGY")
    ats_score = Column(Float, default=0.0)
    parsed_json = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="resumes")

class InterviewSessionModel(Base):
    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    category = Column(String(100), default="INFORMATION-TECHNOLOGY")
    target_role = Column(String(100), default="Software Engineer")
    current_difficulty = Column(String(20), default="Medium")
    total_score = Column(Float, default=0.0)
    performance_tier = Column(String(20), default="Medium")
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="interview_sessions")
    responses = relationship("InterviewResponseModel", back_populates="session", cascade="all, delete-orphan")

class InterviewResponseModel(Base):
    __tablename__ = "interview_responses"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("interview_sessions.id"), nullable=False)
    question = Column(Text, nullable=False)
    question_category = Column(String(100), default="Technical")
    user_response = Column(Text, nullable=False)
    overall_score = Column(Float, default=0.0)
    keyword_score = Column(Float, default=0.0)
    coherence_score = Column(Float, default=0.0)
    fluency_score = Column(Float, default=0.0)
    confidence_score = Column(Float, default=0.0)
    feedback_json = Column(Text, nullable=False)
    answered_at = Column(DateTime, default=datetime.utcnow)

    session = relationship("InterviewSessionModel", back_populates="responses")

def init_db():
    Base.metadata.create_all(bind=ENGINE)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
