import re
import os
import io
import PyPDF2
import docx
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from models.dataset_loader import dataset_loader
from models.external_parsers import external_parsers

# Comprehensive 200+ Skill Taxonomy across Technical & Non-Technical domains
SKILL_TAXONOMY = {
    # Full-Stack & Web Development
    "python", "java", "c++", "c#", "javascript", "typescript", "react", "react.js", "angular", "vue", "vue.js",
    "next.js", "nuxt.js", "node.js", "express", "express.js", "django", "flask", "fastapi", "spring boot",
    "html", "html5", "css", "css3", "tailwind", "tailwind css", "bootstrap", "sass", "less", "redux", "zustand",
    "git", "github", "gitlab", "bitbucket", "docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "rest api",
    "graphql", "soap", "webhooks", "microservices", "webassembly", "webpack", "vite", "babel",
    
    # Databases & Cloud Architecture
    "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch", "sqlite", "oracle", "dynamodb",
    "cassandra", "neo4j", "firebase", "supabase", "snowflake", "bigquery", "redshift", "database design",
    
    # Data Science, AI & Machine Learning
    "machine learning", "deep learning", "nlp", "natural language processing", "computer vision",
    "tensorflow", "pytorch", "keras", "scikit-learn", "sklearn", "pandas", "numpy", "spacy", "nltk",
    "opencv", "data analytics", "data mining", "power bi", "tableau", "matplotlib", "seaborn",
    "hadoop", "spark", "pyspark", "data engineering", "feature engineering", "statistics", "time series",
    "neural networks", "transformers", "llm", "generative ai", "langchain", "prompt engineering",
    
    # Mobile Development
    "flutter", "react native", "swift", "kotlin", "android", "ios", "xcode", "android studio", "dart",
    
    # DevOps, Testing & Cybersecurity
    "agile", "scrum", "jira", "devops", "linux", "unix", "bash", "shell scripting", "system architecture",
    "unit testing", "pytest", "jest", "cypress", "selenium", "postman", "cybersecurity", "networking",
    "penetration testing", "ethical hacking", "terraform", "ansible", "jenkins",
    
    # Business, Management & Product
    "project management", "product management", "leadership", "team management", "strategic planning",
    "business analysis", "financial modeling", "budgeting", "accounting", "risk management",
    "operations management", "supply chain", "vendor management", "scrum master", "stakeholder management",
    
    # Marketing, Sales & HR
    "recruitment", "talent acquisition", "employee engagement", "payroll", "performance management",
    "human resources", "hris", "sales", "b2b sales", "marketing", "digital marketing", "seo", "sem",
    "content strategy", "crm", "salesforce", "hubspot", "copywriting", "social media marketing",
    
    # UI/UX & Design
    "ui/ux", "figma", "adobe xd", "photoshop", "illustrator", "wireframing", "prototyping", "user research",
    
    # Soft Skills
    "communication", "problem solving", "critical thinking", "time management", "collaboration",
    "negotiation", "presentation skills", "customer service", "adaptability", "creativity"
}

DEGREE_PATTERNS = [
    r"\b(b\.?e\.?|b\.?tech|bachelor\s+of\s+technology|bachelor\s+of\s+engineering)\b",
    r"\b(m\.?e\.?|m\.?tech|master\s+of\s+technology|master\s+of\s+engineering)\b",
    r"\b(b\.?s\.?|b\.?sc|bachelor\s+of\s+science)\b",
    r"\b(m\.?s\.?|m\.?sc|master\s+of\s+science)\b",
    r"\b(b\.?a\.?|bachelor\s+of\s+arts)\b",
    r"\b(m\.?a\.?|master\s+of\s+arts)\b",
    r"\b(m\.?b\.?a\.?|master\s+of\s+business\s+administration)\b",
    r"\b(b\.?c\.?a\.?|bachelor\s+of\s+computer\s+applications)\b",
    r"\b(m\.?c\.?a\.?|master\s+of\s+computer\s+applications)\b",
    r"\b(ph\.?d\.?|doctorate|doctor\s+of\s+philosophy)\b",
    r"\b(diploma|associate\s+degree)\b"
]

NON_NAME_KEYWORDS = {
    "resume", "curriculum", "vitae", "profile", "summary", "objective", "experience", "education",
    "skills", "projects", "developer", "engineer", "analyst", "manager", "consultant", "architect",
    "specialist", "contact", "email", "phone", "address", "details", "personal", "work", "history"
}

class ResumeParser:
    def __init__(self):
        self.loader = dataset_loader
        self._init_category_classifier()

    def _init_category_classifier(self):
        """Initializes high-precision TF-IDF category predictor (unigrams + bigrams)"""
        self.vectorizer = TfidfVectorizer(max_features=2500, ngram_range=(1, 2), sublinear_tf=True, stop_words='english')
        self.category_centroids = {}
        
        if self.loader.resumes_df is not None and not self.loader.resumes_df.empty:
            df = self.loader.resumes_df.dropna(subset=['Resume_str', 'Category'])
            if not df.empty:
                try:
                    tfidf_matrix = self.vectorizer.fit_transform(df['Resume_str'])
                    df_cats = df['Category'].values
                    
                    unique_cats = df['Category'].unique()
                    for cat in unique_cats:
                        indices = (df_cats == cat)
                        cat_matrix = tfidf_matrix[indices]
                        centroid = np.asarray(cat_matrix.mean(axis=0))
                        self.category_centroids[cat] = centroid
                except Exception as e:
                    print(f"Error building category centroids: {e}")

    def train_on_input(self, text, category=None):
        """Dynamically retrains/updates the TF-IDF model on new input text"""
        if not text or len(text.strip()) < 20:
            return
        
        cat = category or self._predict_category(text)
        try:
            vec = self.vectorizer.transform([text]).toarray()
            if cat in self.category_centroids:
                self.category_centroids[cat] = 0.85 * self.category_centroids[cat] + 0.15 * vec
            else:
                self.category_centroids[cat] = vec
        except Exception as e:
            print(f"Online training update error: {e}")

    def extract_text_from_file(self, file_bytes, filename):
        """Extracts raw text from PDF or DOCX file bytes with robust fallbacks"""
        filename_lower = filename.lower()
        extracted_text = ""

        if filename_lower.endswith(".pdf"):
            try:
                reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        extracted_text += text + "\n"
            except Exception as e:
                print(f"PyPDF2 error: {e}")

        elif filename_lower.endswith(".docx") or filename_lower.endswith(".doc"):
            try:
                doc = docx.Document(io.BytesIO(file_bytes))
                for para in doc.paragraphs:
                    extracted_text += para.text + "\n"
            except Exception as e:
                print(f"DOCX error: {e}")

        # Fallback if PDF/DOCX reader produced no text
        if not extracted_text or len(extracted_text.strip()) < 5:
            try:
                raw = file_bytes.decode('utf-8', errors='ignore')
                clean = re.sub(r'[^\x20-\x7E\n\r\t]', ' ', raw)
                words = [w for w in clean.split() if len(w) > 1]
                extracted_text = " ".join(words)
            except Exception:
                extracted_text = ""

        return extracted_text.strip()

    def _extract_candidate_name(self, text):
        """Intelligent Name Extraction (NER) ignoring title keywords"""
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for line in lines[:8]:
            words = line.split()
            if 2 <= len(words) <= 4:
                clean_words = [w.strip(':,.-') for w in words]
                words_lower = [w.lower() for w in clean_words]
                
                if any(w in NON_NAME_KEYWORDS for w in words_lower):
                    continue
                if re.search(r'@|phone|mobile|email|http|\d', line.lower()):
                    continue
                
                if all(w[0].isupper() for w in clean_words if len(w) > 1):
                    return " ".join(clean_words).title()
        
        return "Candidate"

    def parse_resume(self, text, engine="local", file_bytes=None, filename="resume.pdf", api_key=None):
        """
        Parses resume text or file bytes using either Local High-Precision Engine or External APIs.
        Calculates dynamic ATS score and generates actionable score improvement steps.
        """
        self.train_on_input(text)

        if engine in ["affinda", "rchilli", "textkernel"] and file_bytes:
            try:
                if engine == "affinda":
                    ext_data = external_parsers.parse_with_affinda(file_bytes, filename, api_key=api_key)
                elif engine == "rchilli":
                    ext_data = external_parsers.parse_with_rchilli(file_bytes, filename, user_key=api_key)
                elif engine == "textkernel":
                    ext_data = external_parsers.parse_with_textkernel(file_bytes, filename, service_key=api_key)
                
                combined_text = f"{' '.join(ext_data.get('skills', []))} {ext_data.get('raw_text_snippet', '')} {text}"
                predicted_category = self._predict_category(combined_text)
                ats_result = self._calculate_ats_score(combined_text, ext_data.get('skills', []), ext_data.get('education', []), ext_data.get('email'), ext_data.get('phone'))

                return {
                    "engine_used": ext_data.get("engine", engine.title()),
                    "candidate_name": ext_data.get("candidate_name") or self._extract_candidate_name(text),
                    "email": ext_data.get("email"),
                    "phone": ext_data.get("phone"),
                    "skills": ext_data.get("skills", []),
                    "education": ext_data.get("education", ["Degree"]),
                    "experience_years": 3,
                    "predicted_category": predicted_category,
                    "ats_score": ats_result["ats_score"],
                    "section_breakdown": ats_result["section_breakdown"],
                    "missing_sections": ats_result["missing_sections"],
                    "weak_keywords": ats_result["weak_keywords"],
                    "formatting_suggestions": ats_result["formatting_suggestions"],
                    "actionable_improvements": ats_result["actionable_improvements"],
                    "raw_text_snippet": text[:500] + "..." if len(text) > 500 else text
                }
            except Exception as e:
                print(f"External API '{engine}' failed ({e}). Falling back to Local Engine.")

        # High-Precision Local Engine
        text_lower = text.lower()
        
        emails = re.findall(r'[a-zA-Z0-9%._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        phones = re.findall(r'[\+\(]?[0-9]{1,4}[\)]?[-\s\./0-9]{7,15}', text)
        
        email = emails[0] if emails else None
        phone = phones[0].strip() if phones else None
        
        candidate_name = self._extract_candidate_name(text)

        extracted_skills = set()
        for skill in SKILL_TAXONOMY:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                extracted_skills.add(skill.title())

        education_matches = []
        for pattern in DEGREE_PATTERNS:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            for m in matches:
                degree_str = m[0] if isinstance(m, tuple) else m
                if degree_str.upper() not in [e.upper() for e in education_matches]:
                    education_matches.append(degree_str.upper())

        exp_years = 0
        exp_matches = re.findall(r'(\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s*)?(?:experience|exp)?', text_lower)
        if exp_matches:
            try:
                exp_years = max([int(x) for x in exp_matches])
            except ValueError:
                exp_years = 1
        elif "senior" in text_lower or "lead" in text_lower or "manager" in text_lower:
            exp_years = 5
        elif "junior" in text_lower or "intern" in text_lower or "fresher" in text_lower:
            exp_years = 1
        else:
            exp_years = 2

        predicted_category = self._predict_category(text)
        ats_result = self._calculate_ats_score(text, list(extracted_skills), education_matches, email, phone)

        return {
            "engine_used": "Local High-Precision Engine",
            "candidate_name": candidate_name,
            "email": email,
            "phone": phone,
            "skills": sorted(list(extracted_skills)),
            "education": education_matches if education_matches else ["Bachelor Degree / General Education"],
            "experience_years": exp_years,
            "predicted_category": predicted_category,
            "ats_score": ats_result["ats_score"],
            "section_breakdown": ats_result["section_breakdown"],
            "missing_sections": ats_result["missing_sections"],
            "weak_keywords": ats_result["weak_keywords"],
            "formatting_suggestions": ats_result["formatting_suggestions"],
            "actionable_improvements": ats_result["actionable_improvements"],
            "raw_text_snippet": text[:500] + "..." if len(text) > 500 else text
        }

    def _predict_category(self, text):
        if not self.category_centroids:
            return "INFORMATION-TECHNOLOGY"
        try:
            vec = self.vectorizer.transform([text]).toarray()
            best_cat = "INFORMATION-TECHNOLOGY"
            best_sim = -1.0
            
            for cat, centroid in self.category_centroids.items():
                sim = cosine_similarity(vec, centroid)[0][0]
                if sim > best_sim:
                    best_sim = sim
                    best_cat = cat
            return best_cat
        except Exception:
            return "INFORMATION-TECHNOLOGY"

    def _calculate_ats_score(self, text, skills, education, email, phone):
        """
        Dynamic Fine-Grained Quantifiable ATS Scoring Engine with Actionable Improvement Recommendations.
        """
        text_lower = text.lower()
        score = 0.0
        breakdown = {}
        missing_sections = []
        weak_keywords = []
        formatting_suggestions = []
        actionable_improvements = []

        # 1. Contact Info & Portfolio URLs (Max 10 Pts)
        contact_pts = 0.0
        if email:
            contact_pts += 4.0
        else:
            missing_sections.append("Email Address")
            actionable_improvements.append({
                "title": "Add Email Address Header",
                "description": "Add your primary email address (e.g. alex@example.com) at the top of your resume.",
                "potential_gain": "+4%",
                "priority": "High"
            })

        if phone:
            contact_pts += 3.0
        else:
            missing_sections.append("Phone Number")
            actionable_improvements.append({
                "title": "Add Phone Number",
                "description": "Include your phone number with country code (e.g. +91 9876543210).",
                "potential_gain": "+3%",
                "priority": "High"
            })
        
        urls = re.findall(r'(?:linkedin\.com|github\.com|portfolio|[a-z0-9\-]+\.dev|[a-z0-9\-]+\.io)', text_lower)
        if urls:
            contact_pts += 3.0
        else:
            formatting_suggestions.append("Add your LinkedIn, GitHub, or Online Portfolio URL for ATS credibility.")
            actionable_improvements.append({
                "title": "Include LinkedIn & GitHub / Portfolio URL",
                "description": "Add direct clickable links to your LinkedIn profile and GitHub or Portfolio website.",
                "potential_gain": "+3%",
                "priority": "Medium"
            })
            
        score += contact_pts
        breakdown["Contact & Online Links"] = f"{round(contact_pts, 1)}/10"

        # 2. Skill Density & Versatility (Max 30 Pts)
        skill_count = len(skills)
        if skill_count >= 16:
            skill_pts = 30.0
        elif skill_count >= 12:
            skill_pts = 26.0
            actionable_improvements.append({
                "title": "Expand Technical Skills to 16+ Keywords",
                "description": f"Currently found {skill_count} skills. Add 4 more frameworks, libraries, or tools to reach 30/30 skill score.",
                "potential_gain": "+4%",
                "priority": "Medium"
            })
        elif skill_count >= 8:
            skill_pts = 21.0
            actionable_improvements.append({
                "title": "Add 5+ Technical Keywords & Frameworks",
                "description": f"Currently found {skill_count} skills. List specific technologies (e.g. React, Node.js, SQL, AWS, Docker).",
                "potential_gain": "+9%",
                "priority": "High"
            })
        elif skill_count >= 5:
            skill_pts = 16.0
            actionable_improvements.append({
                "title": "Significantly Increase Technical Skill Density",
                "description": f"Only {skill_count} skills detected. Add a dedicated 'TECHNICAL SKILLS' section with tools, databases, and languages.",
                "potential_gain": "+14%",
                "priority": "High"
            })
        elif skill_count >= 2:
            skill_pts = 10.0
            weak_keywords.append("Low technical skill density (< 5 skills). Add relevant frameworks, tools, or domain keywords.")
            actionable_improvements.append({
                "title": "Add Dedicated Skills & Core Competencies Section",
                "description": f"Only {skill_count} skills found. ATS scanners look for 12+ technical domain keywords.",
                "potential_gain": "+20%",
                "priority": "High"
            })
        else:
            skill_pts = 4.0
            weak_keywords.append("Low technical skill density (< 5 skills). Add relevant frameworks, tools, or domain keywords.")
            actionable_improvements.append({
                "title": "Add Skills & Core Competencies Section",
                "description": "No technical skills detected. Create a bulleted list of 10+ software tools, languages, and frameworks.",
                "potential_gain": "+26%",
                "priority": "High"
            })
        
        score += skill_pts
        breakdown["Skill Keyword Density"] = f"{round(skill_pts, 1)}/30"

        # 3. Action Verbs & Measurable Metrics (Max 25 Pts)
        action_verbs_dict = {
            "engineered", "built", "developed", "architected", "spearheaded", "optimized", "implemented",
            "designed", "reduced", "increased", "accelerated", "scaled", "automated", "created", "led",
            "managed", "orchestrated", "deployed", "transformed", "streamlined", "enhanced", "resolved"
        }
        found_verbs = [v for v in action_verbs_dict if re.search(r'\b' + v + r'\b', text_lower)]
        verb_pts = min(15.0, len(found_verbs) * 1.5)

        if len(found_verbs) < 5:
            actionable_improvements.append({
                "title": "Use High-Impact Action Verbs",
                "description": "Start bullet points with strong engineering verbs: 'Engineered', 'Architected', 'Spearheaded', 'Optimized'.",
                "potential_gain": f"+{round(15.0 - verb_pts, 1)}%",
                "priority": "High"
            })

        # Scans for metrics: percentages, dollar values, multipliers (45%, $50k, 10x, 50,000+ users, 99.9%)
        metrics = re.findall(r'\b(?:\d+%(?:\.\d+)?|\$\d+(?:\,\d+)*(?:\.\d+)?[kM]?|\d+x|\d+,\d+|\d+\s*\+\s*(?:users|clients|projects|queries))\b', text)
        metric_pts = min(10.0, len(metrics) * 2.5)

        if len(metrics) < 3:
            weak_keywords.append("No quantifiable metrics found (e.g. 'reduced latency by 40%', 'managed 50k+ users'). Add data-backed metrics.")
            actionable_improvements.append({
                "title": "Add Measurable Metrics & Percentage Outcomes",
                "description": "Include 3+ quantified achievements (e.g., 'reduced API response time by 35%', 'managed 50,000+ users', 'increased sales by 20%').",
                "potential_gain": f"+{round(10.0 - metric_pts, 1)}%",
                "priority": "High"
            })

        impact_pts = verb_pts + metric_pts
        score += impact_pts
        breakdown["Action Verbs & Impact Metrics"] = f"{round(impact_pts, 1)}/25"

        # 4. Education & Credentials (Max 15 Pts)
        edu_pts = 0.0
        if education:
            edu_pts = 12.0
            if any(deg in str(education).upper() for deg in ["M.TECH", "MASTER", "PH.D", "MBA"]):
                edu_pts += 3.0
            else:
                actionable_improvements.append({
                    "title": "Highlight Specializations & Certifications",
                    "description": "List professional certifications (AWS, PMP, Scrum Master, Google AI) to maximize education credentials.",
                    "potential_gain": "+3%",
                    "priority": "Low"
                })
        elif "education" in text_lower or "university" in text_lower or "college" in text_lower:
            edu_pts = 8.0
            actionable_improvements.append({
                "title": "Specify Degree Name Explicitly",
                "description": "Explicitly state your degree (e.g., Bachelor of Technology, Master of Computer Applications).",
                "potential_gain": "+7%",
                "priority": "Medium"
            })
        else:
            edu_pts = 4.0
            missing_sections.append("Education & Degree Details")
            actionable_improvements.append({
                "title": "Add Education Section",
                "description": "Include a dedicated 'EDUCATION' section specifying your university, degree, and graduation year.",
                "potential_gain": "+11%",
                "priority": "High"
            })
            
        score += edu_pts
        breakdown["Education & Credentials"] = f"{round(edu_pts, 1)}/15"

        # 5. Experience Depth & Structure (Max 20 Pts)
        exp_pts = 10.0
        exp_matches = re.findall(r'(\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s*)?(?:experience|exp)?', text_lower)
        if exp_matches:
            try:
                years = max([int(x) for x in exp_matches])
                if years >= 5:
                    exp_pts = 20.0
                elif years >= 3:
                    exp_pts = 16.0
                    actionable_improvements.append({
                        "title": "Highlight Seniority & Leadership Roles",
                        "description": "Emphasize project leadership, architecture design, and mentoring junior team members.",
                        "potential_gain": "+4%",
                        "priority": "Low"
                    })
                elif years >= 1:
                    exp_pts = 13.0
            except ValueError:
                exp_pts = 12.0
        elif "senior" in text_lower or "lead" in text_lower or "manager" in text_lower:
            exp_pts = 18.0
        elif "experience" in text_lower or "work history" in text_lower:
            exp_pts = 12.0
            actionable_improvements.append({
                "title": "Quantify Years of Experience in Summary",
                "description": "State your experience duration in your profile summary (e.g., 'Software Engineer with 3+ years of experience').",
                "potential_gain": "+8%",
                "priority": "Medium"
            })
        else:
            missing_sections.append("Work Experience Section")
            exp_pts = 6.0
            actionable_improvements.append({
                "title": "Add Work Experience / Projects Section",
                "description": "Include a dedicated 'WORK EXPERIENCE' or 'MAJOR PROJECTS' header with bulleted achievements.",
                "potential_gain": "+14%",
                "priority": "High"
            })

        score += exp_pts
        breakdown["Experience & Structure"] = f"{round(exp_pts, 1)}/20"

        # 6. Cliché Phrases & Word Count Penalties
        cliches = ["responsible for", "worked on", "team player", "hard worker", "detail oriented", "self starter"]
        found_cliches = [c for c in cliches if c in text_lower]
        for c in found_cliches:
            score -= 2.0
            weak_keywords.append(f"Replace generic passive phrase '{c}' with active accomplishments.")
            actionable_improvements.append({
                "title": f"Replace Cliché Phrase '{c.title()}'",
                "description": f"Replace generic phrase '{c}' with active engineering verbs like 'Architected', 'Spearheaded', or 'Optimized'.",
                "potential_gain": "+2%",
                "priority": "Medium"
            })

        word_count = len(text.split())
        if word_count < 150:
            score -= 8.0
            formatting_suggestions.append("Resume content is too brief (< 150 words). Add details on projects and responsibilities.")
            actionable_improvements.append({
                "title": "Expand Resume Depth (Low Word Count)",
                "description": f"Resume is only {word_count} words. Expand project descriptions and technical accomplishments to 300-600 words.",
                "potential_gain": "+8%",
                "priority": "High"
            })
        elif word_count > 1000:
            score -= 4.0
            formatting_suggestions.append("Resume is over 1000 words. Keep it concise (1 to 2 pages max).")
            actionable_improvements.append({
                "title": "Trim Resume Length (< 1000 words)",
                "description": f"Resume is {word_count} words. Consolidate older experience and focus on high-impact bullet points.",
                "potential_gain": "+4%",
                "priority": "Low"
            })

        final_score = round(max(15.0, min(99.0, score)), 1)

        return {
            "ats_score": final_score,
            "section_breakdown": breakdown,
            "missing_sections": missing_sections,
            "weak_keywords": weak_keywords,
            "formatting_suggestions": formatting_suggestions,
            "actionable_improvements": actionable_improvements
        }

resume_parser = ResumeParser()
