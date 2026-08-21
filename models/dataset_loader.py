import os
import pandas as pd
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOBS_CSV_PATH = os.path.join(BASE_DIR, "archive (2)", "jobs_dataset.csv")
RESUME_CSV_PATH = os.path.join(BASE_DIR, "archive (3)", "Resume", "Resume.csv")

class DatasetLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatasetLoader, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.jobs_df = None
        self.resumes_df = None
        self.categories = []
        self._load_datasets()
        self._initialized = True

    def _load_datasets(self):
        # Load Jobs Dataset
        if os.path.exists(JOBS_CSV_PATH):
            try:
                df = pd.read_csv(JOBS_CSV_PATH)
                # Clean missing fields
                df['positionName'] = df['positionName'].fillna('Job Position')
                df['description'] = df['description'].fillna('')
                df['company'] = df['company'].fillna('Top Company')
                df['location'] = df['location'].fillna('Remote / Various')
                df['salary'] = df['salary'].fillna('Competitive')
                
                # Composite text for vector matching
                df['combined_text'] = (
                    df['positionName'].astype(str) + " " +
                    df['searchInput/position'].fillna('').astype(str) + " " +
                    df['description'].astype(str)
                )
                self.jobs_df = df
                logger.info(f"Loaded {len(df)} jobs from {JOBS_CSV_PATH}")
            except Exception as e:
                logger.error(f"Error loading jobs dataset: {e}")
                self.jobs_df = pd.DataFrame()
        else:
            logger.warning(f"Jobs CSV path not found: {JOBS_CSV_PATH}")
            self.jobs_df = pd.DataFrame()

        # Load Resumes Dataset
        if os.path.exists(RESUME_CSV_PATH):
            try:
                df_res = pd.read_csv(RESUME_CSV_PATH)
                self.resumes_df = df_res
                self.categories = sorted(df_res['Category'].dropna().unique().tolist())
                logger.info(f"Loaded {len(df_res)} resumes across {len(self.categories)} categories")
            except Exception as e:
                logger.error(f"Error loading resume dataset: {e}")
                self.resumes_df = pd.DataFrame()
                self.categories = [
                    "INFORMATION-TECHNOLOGY", "ENGINEERING", "FINANCE", "HR",
                    "BUSINESS-DEVELOPMENT", "SALES", "MARKETING", "HEALTHCARE"
                ]
        else:
            logger.warning(f"Resume CSV path not found: {RESUME_CSV_PATH}")
            self.resumes_df = pd.DataFrame()
            self.categories = [
                "INFORMATION-TECHNOLOGY", "ENGINEERING", "FINANCE", "HR",
                "BUSINESS-DEVELOPMENT", "SALES", "MARKETING", "HEALTHCARE"
            ]

    def get_jobs(self, limit=100):
        if self.jobs_df is not None and not self.jobs_df.empty:
            return self.jobs_df.head(limit)
        return pd.DataFrame()

    def get_categories(self):
        return self.categories

dataset_loader = DatasetLoader()
