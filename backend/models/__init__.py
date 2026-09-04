"""
PrepWise AI - Backend Models Package
Exposes resume parsers, ATS analyzers, job recommendation engines,
interview evaluators, and coding assessment problem banks.
"""

from backend.models.dataset_loader import dataset_loader
from backend.models.resume_parser import resume_parser
from backend.models.job_matcher import job_matcher
from backend.models.interview_evaluator import interview_evaluator
from backend.models.coding_questions_bank import CODING_QUESTIONS
from backend.models.coding_problems import CODING_PROBLEMS

__all__ = [
    "dataset_loader",
    "resume_parser",
    "job_matcher",
    "interview_evaluator",
    "CODING_QUESTIONS",
    "CODING_PROBLEMS",
]
