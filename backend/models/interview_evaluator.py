import re
import random
from backend.models.dataset_loader import dataset_loader
from backend.models.deep_answer_evaluator import deep_answer_evaluator

# Category-specific & Role-based Interview Question Banks
QUESTION_BANK = {
    "INFORMATION-TECHNOLOGY": {
        "Easy": [
            {
                "question": "Can you walk me through your recent project experience and how you utilized your primary technical stack?",
                "target_keywords": ["project", "architecture", "framework", "database", "testing", "code", "development"],
                "category": "Technical Overview"
            },
            {
                "question": "How do you ensure code quality, readability, and maintainability when working in a team environment?",
                "target_keywords": ["code review", "git", "clean code", "unit testing", "documentation", "refactoring"],
                "category": "Software Engineering Practices"
            }
        ],
        "Medium": [
            {
                "question": "Explain a challenging technical bug or performance bottleneck you encountered. How did you diagnose and resolve it?",
                "target_keywords": ["debugging", "logs", "profiling", "root cause", "optimization", "performance", "resolution"],
                "category": "Problem Solving & Debugging"
            },
            {
                "question": "How do you design scalable RESTful APIs or database schemas to handle high concurrent user traffic?",
                "target_keywords": ["rest api", "schema", "indexing", "caching", "redis", "scalability", "load balancing"],
                "category": "System Design & Architecture"
            }
        ],
        "Hard": [
            {
                "question": "Describe a scenario where you had to make a trade-off between architectural purity and project deadlines. How did you manage technical debt?",
                "target_keywords": ["trade-off", "technical debt", "stakeholders", "refactoring", "milestones", "risk management"],
                "category": "Engineering Leadership & Strategy"
            },
            {
                "question": "Walk me through how you would architect a distributed real-time data streaming pipeline with failover resilience.",
                "target_keywords": ["kafka", "microservices", "replication", "fault tolerance", "event driven", "throughput"],
                "category": "Advanced Systems Architecture"
            }
        ]
    },
    "ENGINEERING": {
        "Easy": [
            {
                "question": "What engineering methodologies and CAD/modeling or simulation tools do you rely on most in your design workflow?",
                "target_keywords": ["design", "cad", "simulation", "modeling", "specs", "standards", "safety"],
                "category": "Engineering Fundamentals"
            }
        ],
        "Medium": [
            {
                "question": "Describe an instance where a prototype failed during initial testing. What steps did you take to re-engineer the component?",
                "target_keywords": ["prototype", "failure analysis", "testing", "tolerances", "stress test", "iteration"],
                "category": "Quality & Testing"
            }
        ],
        "Hard": [
            {
                "question": "How do you approach root-cause failure analysis in complex electromechanical or structural systems under harsh operating environments?",
                "target_keywords": ["root cause", "fea", "materials", "thermal", "compliance", "reliability"],
                "category": "Advanced Engineering Analysis"
            }
        ]
    },
    "FINANCE": {
        "Easy": [
            {
                "question": "How do you ensure accuracy and compliance when preparing financial reports and forecasting models?",
                "target_keywords": ["reconciliation", "compliance", "excel", "gaap", "audit", "forecasting"],
                "category": "Financial Reporting"
            }
        ],
        "Medium": [
            {
                "question": "Walk me through your process for evaluating investment risk and building discounted cash flow (DCF) models.",
                "target_keywords": ["dcf", "valuation", "wacc", "cash flow", "risk assessment", "variance"],
                "category": "Valuation & Analysis"
            }
        ],
        "Hard": [
            {
                "question": "How would you navigate capital allocation strategies during periods of high market volatility and inflation?",
                "target_keywords": ["hedging", "liquidity", "capital allocation", "macroeconomic", "portfolio strategy"],
                "category": "Strategic Finance"
            }
        ]
    },
    "HR": {
        "Easy": [
            {
                "question": "How do you handle conflict resolution between employees while maintaining workplace policy and empathy?",
                "target_keywords": ["communication", "conflict resolution", "policy", "empathy", "mediation", "confidentiality"],
                "category": "Employee Relations"
            }
        ],
        "Medium": [
            {
                "question": "What strategies do you use to attract and retain top talent in highly competitive labor markets?",
                "target_keywords": ["sourcing", "employer brand", "onboarding", "retention", "benefits", "engagement"],
                "category": "Talent Acquisition"
            }
        ],
        "Hard": [
            {
                "question": "Describe how you lead organizational restructuring or change management initiatives with minimal disruption to morale.",
                "target_keywords": ["change management", "culture", "leadership", "stakeholders", "communication plan"],
                "category": "Strategic HR Leadership"
            }
        ]
    }
}

GENERIC_QUESTIONS = {
    "Easy": [
        {
            "question": "Tell me about yourself and highlight key achievements from your background that align with this target role.",
            "target_keywords": ["experience", "achievements", "skills", "growth", "contribute", "background"],
            "category": "Behavioral Introduction"
        }
    ],
    "Medium": [
        {
            "question": "Describe a situation where you had to work under tight deadlines with competing priorities. How did you prioritize your tasks?",
            "target_keywords": ["prioritization", "deadline", "time management", "communication", "deliverables"],
            "category": "Behavioral & Time Management"
        }
    ],
    "Hard": [
        {
            "question": "Give an example of a difficult decision you made that was met with pushback from team members or stakeholders. How did you align the team?",
            "target_keywords": ["decision", "leadership", "negotiation", "alignment", "data driven", "stakeholders"],
            "category": "Leadership & Influence"
        }
    ]
}

class InterviewEvaluator:
    def __init__(self):
        self.question_bank = QUESTION_BANK

    def generate_question(self, category, target_role="Professional", difficulty="Medium", asked_ids=None, resume_skills=None, candidate_name=None):
        """
        Dynamically generates interview questions tailored specifically to the candidate's uploaded resume skills and project stack.
        """
        asked_ids = asked_ids or []
        resume_skills = [s.strip() for s in (resume_skills or []) if s.strip()]

        # 1. RESUME-TAILORED DYNAMIC QUESTION GENERATION
        if resume_skills and len(resume_skills) >= 1:
            sample_skills = random.sample(resume_skills, min(3, len(resume_skills)))
            primary_skill = sample_skills[0]
            secondary_skill = sample_skills[1] if len(sample_skills) > 1 else primary_skill
            tertiary_skill = sample_skills[2] if len(sample_skills) > 2 else secondary_skill

            resume_tailored_pool = [
                {
                    "question": f"In your uploaded resume, you highlighted expertise in {primary_skill} and {secondary_skill}. Can you walk me through a major project where you implemented both {primary_skill} and {secondary_skill}?",
                    "target_keywords": [primary_skill.lower(), secondary_skill.lower(), "architecture", "project", "implementation", "code", "database"],
                    "category": f"Resume Deep-Dive: {primary_skill} & {secondary_skill}"
                },
                {
                    "question": f"Your resume lists {primary_skill} as a core competency. What are the best practices, performance optimization techniques, or design patterns you follow when developing with {primary_skill}?",
                    "target_keywords": [primary_skill.lower(), "optimization", "performance", "patterns", "best practices", "scaling"],
                    "category": f"Resume Deep-Dive: {primary_skill} Best Practices"
                },
                {
                    "question": f"Based on your resume background in {secondary_skill} and {tertiary_skill}, describe a complex technical bug or system bottleneck you encountered and how you resolved it.",
                    "target_keywords": [secondary_skill.lower(), tertiary_skill.lower(), "debugging", "root cause", "resolution", "logs", "performance"],
                    "category": f"Resume Debugging: {secondary_skill}"
                },
                {
                    "question": f"You mentioned {primary_skill} on your resume. How do you approach testing, security, and deployment for applications built with {primary_skill}?",
                    "target_keywords": [primary_skill.lower(), "testing", "security", "deployment", "ci/cd", "validation"],
                    "category": f"Resume Production Readiness: {primary_skill}"
                }
            ]

            available_resume_q = [q for q in resume_tailored_pool if q["question"] not in asked_ids]
            if available_resume_q:
                selected = random.choice(available_resume_q)
                return {
                    "question_id": selected["question"],
                    "question": selected["question"],
                    "difficulty": difficulty,
                    "category": selected.get("category", "Resume Skill Deep-Dive"),
                    "target_keywords": selected.get("target_keywords", [s.lower() for s in sample_skills])
                }

        # 2. CATEGORY QUESTION BANK FALLBACK
        cat_key = category.upper() if category.upper() in self.question_bank else "INFORMATION-TECHNOLOGY"
        diff_questions = self.question_bank.get(cat_key, {}).get(difficulty)
        if not diff_questions:
            diff_questions = GENERIC_QUESTIONS.get(difficulty, GENERIC_QUESTIONS["Medium"])

        available = [q for q in diff_questions if q["question"] not in asked_ids]
        if not available:
            available = diff_questions

        selected = random.choice(available)
        q_text = selected["question"]
        if target_role and target_role != "Professional":
            q_text = q_text.replace("this target role", f"the {target_role} position")

        return {
            "question_id": selected["question"],
            "question": q_text,
            "difficulty": difficulty,
            "category": selected.get("category", "General Professional"),
            "target_keywords": selected.get("target_keywords", [])
        }

    def evaluate_response(self, question_text, target_keywords, candidate_response, current_difficulty="Medium"):
        """
        Evaluates candidate answers using Deep Semantic Answer Evaluator & Vocal Delivery Metrics.
        """
        return deep_answer_evaluator.evaluate_candidate_answer(
            question=question_text,
            target_keywords=target_keywords,
            user_response=candidate_response,
            current_difficulty=current_difficulty
        )

interview_evaluator = InterviewEvaluator()
