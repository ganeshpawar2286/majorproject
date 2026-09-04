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

class CodingQuestionModel(Base):
    __tablename__ = "coding_questions"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(String(100), unique=True, index=True, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(String(20), nullable=False, index=True) # Easy, Medium, Hard
    topic = Column(String(50), nullable=False, index=True) # Arrays, Strings, etc.
    supported_languages_json = Column(Text, default='["python", "java", "cpp", "javascript"]')
    constraints = Column(Text, default="")
    input_format = Column(Text, default="")
    output_format = Column(Text, default="")
    examples_json = Column(Text, default="[]") # List of {input, output, explanation}
    starter_code_json = Column(Text, default="{}") # {python, java, cpp, javascript}
    solution_json = Column(Text, default="{}") # {python, java, cpp, javascript}
    test_cases_json = Column(Text, default="[]") # Public test cases [{input, expected_output}]
    hidden_test_cases_json = Column(Text, default="[]") # Hidden test cases [{input, expected_output}]
    time_limit_ms = Column(Integer, default=2000)
    memory_limit_mb = Column(Integer, default=256)
    tags_json = Column(Text, default="[]")
    created_at = Column(DateTime, default=datetime.utcnow)

class CodingInterviewSessionModel(Base):
    __tablename__ = "coding_interviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    language = Column(String(50), default="python")
    difficulty = Column(String(20), default="Medium")
    topic = Column(String(50), default="All")
    question_count = Column(Integer, default=3)
    question_ids_json = Column(Text, default="[]")
    current_question_index = Column(Integer, default=0)
    status = Column(String(30), default="in_progress") # in_progress, completed, abandoned
    total_score = Column(Float, default=0.0)
    accuracy = Column(Float, default=0.0)
    time_spent_seconds = Column(Integer, default=0)
    completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="coding_interviews")
    submissions = relationship("CodingSubmissionModel", back_populates="interview_session", cascade="all, delete-orphan")

class CodingSubmissionModel(Base):
    __tablename__ = "coding_submissions"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("coding_interviews.id"), nullable=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    question_id = Column(String(100), nullable=False, index=True)
    language = Column(String(50), default="python")
    code = Column(Text, nullable=False)
    status = Column(String(40), default="Pending") # Accepted, Wrong Answer, Time Limit Exceeded, Runtime Error, Compilation Error
    passed_test_cases = Column(Integer, default=0)
    total_test_cases = Column(Integer, default=0)
    execution_time_ms = Column(Float, default=0.0)
    memory_used_mb = Column(Float, default=0.0)
    stdout = Column(Text, default="")
    stderr = Column(Text, default="")
    error_message = Column(Text, default="")
    submitted_at = Column(DateTime, default=datetime.utcnow)

    interview_session = relationship("CodingInterviewSessionModel", back_populates="submissions")
    ai_evaluation = relationship("CodingAIEvaluationModel", uselist=False, back_populates="submission", cascade="all, delete-orphan")

class CodingAIEvaluationModel(Base):
    __tablename__ = "coding_ai_evaluations"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("coding_submissions.id"), unique=True, nullable=False)
    overall_score = Column(Float, default=0.0) # out of 50
    correctness_score = Column(Float, default=0.0) # out of 10
    time_complexity_score = Column(Float, default=0.0) # out of 10
    space_complexity_score = Column(Float, default=0.0) # out of 10
    code_quality_score = Column(Float, default=0.0) # out of 10
    problem_solving_score = Column(Float, default=0.0) # out of 10
    time_complexity = Column(String(50), default="O(N)")
    space_complexity = Column(String(50), default="O(1)")
    strengths_json = Column(Text, default="[]")
    improvements_json = Column(Text, default="[]")
    explanation = Column(Text, default="")
    follow_up_question = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    submission = relationship("CodingSubmissionModel", back_populates="ai_evaluation")

class CodingProgressModel(Base):
    __tablename__ = "coding_user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    interviews_completed = Column(Integer, default=0)
    best_score = Column(Float, default=0.0)
    average_score = Column(Float, default=0.0)
    problems_solved = Column(Integer, default=0)
    current_streak_days = Column(Integer, default=1)
    last_practice_date = Column(DateTime, default=datetime.utcnow)
    topic_stats_json = Column(Text, default="{}") # {topic: {attempted, solved, accuracy}}
    demonstrated_skills_json = Column(Text, default="[]") # skills proven in coding test
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", backref="coding_progress")

def init_db():
    Base.metadata.create_all(bind=ENGINE)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

