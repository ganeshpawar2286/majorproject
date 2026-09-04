import os
from dotenv import load_dotenv

# Base Directory resolution
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BACKEND_DIR)

# Load environment variables from .env file (check root and backend)
for env_candidate in [os.path.join(PROJECT_ROOT, ".env"), os.path.join(BACKEND_DIR, ".env")]:
    if os.path.exists(env_candidate):
        load_dotenv(dotenv_path=env_candidate)
        break

class Config:
    """Centralized System Environment & API Configuration Manager"""
    PORT = int(os.environ.get("PORT", 5000))
    FLASK_ENV = os.environ.get("FLASK_ENV", "development")
    SECRET_KEY = os.environ.get("SECRET_KEY", "prepwise_ai_super_secret_jwt_key_2026_pro")
    DATABASE_URL = os.environ.get("DATABASE_URL", f"sqlite:///{os.path.join(BACKEND_DIR, 'prepwise.db')}")
    
    # Third-Party Resume Parser API Keys
    AFFINDA_API_KEY = os.environ.get("AFFINDA_API_KEY", "")
    RCHILLI_USER_KEY = os.environ.get("RCHILLI_USER_KEY", "")
    TEXTKERNEL_ACCOUNT_ID = os.environ.get("TEXTKERNEL_ACCOUNT_ID", "")
    TEXTKERNEL_SERVICE_KEY = os.environ.get("TEXTKERNEL_SERVICE_KEY", "")
    
    # AI & LLM API Keys
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
    
    # Dataset Paths
    DATASET_JOBS_PATH = os.path.join(PROJECT_ROOT, os.environ.get("DATASET_JOBS_PATH", os.path.join("data", "jobs", "jobs_dataset.csv")))
    DATASET_RESUMES_PATH = os.path.join(PROJECT_ROOT, os.environ.get("DATASET_RESUMES_PATH", os.path.join("data", "resumes", "Resume.csv")))

config = Config()
