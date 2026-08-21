# PrepWise AI - Integrated AI Career Preparation Platform

PrepWise AI is a unified career preparation platform that seamlessly integrates Resume Analysis, Job Recommendations, AI-powered Mock Interviewing, and Performance Analytics.

## Key Features
1. **Resume Analysis Module**:
   - Parses PDF & DOCX resumes.
   - Extracts skills, education, experience, and contact details using NLP (spaCy / NLTK).
   - Computes ATS (Applicant Tracking System) compatibility scores (0–100%).
   - Highlights missing resume sections, weak formatting, and skill gaps.

2. **Job Recommendation Module**:
   - Compares parsed candidate resume features against a dataset of real job postings (`jobs_dataset.csv`).
   - Uses TF-IDF and Cosine Similarity vector matching to calculate relevance scores.
   - Ranks top matching jobs and highlights missing required skills.

3. **AI Mock Interview Module**:
   - Dynamically generates role-based interview questions adapted to candidate resume category & experience level.
   - Supports candidate responses in both Text and Voice/Audio (using native browser Speech-to-Text).
   - Evaluates responses based on Keyword Coverage, Coherence Index, Fluency, and Speech Confidence.
   - Dynamically adjusts question difficulty (Adaptive Questioning).

4. **Performance & Analytics Dashboard**:
   - Tracks session scores and performance over time with interactive charts.
   - Categorizes user readiness (Low / Medium / High).
   - Provides actionable feedback and downloadable progress reports.

## Project Structure
```
majorproject/
├── archive (2)/           # Job listings dataset (jobs_dataset.csv, jobs_dataset.json)
├── archive (3)/           # Resume dataset (Resume.csv & 24 category folders)
├── backend/               # Flask REST API backend & database setup
│   ├── app.py
│   ├── database.py
│   ├── routes_auth.py
│   ├── routes_resume.py
│   ├── routes_jobs.py
│   ├── routes_interview.py
│   └── routes_dashboard.py
├── models/                # ML / NLP engine pipelines
│   ├── dataset_loader.py
│   ├── resume_parser.py
│   ├── job_matcher.py
│   └── interview_evaluator.py
├── frontend/              # Modern React + Vite frontend application
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── index.css
│   └── package.json
├── requirements.txt
└── README.md
```

## Quick Setup Instructions

### Backend Setup
1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask backend server:
   ```bash
   python backend/app.py
   ```
   Backend API runs on `http://localhost:5000`.

### Frontend Setup
1. Navigate to frontend directory and install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the Vite development server:
   ```bash
   npm run dev
   ```
   Frontend runs on `http://localhost:5173`.
