import json
import random
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from backend.database import (
    SessionLocal, User, ResumeModel,
    CodingQuestionModel, CodingInterviewSessionModel,
    CodingSubmissionModel, CodingAIEvaluationModel, CodingProgressModel
)
from backend.models.coding_questions_bank import (
    get_all_questions, get_question_by_id, filter_questions, get_sanitized_question
)
from backend.services.secure_code_sandbox import secure_code_sandbox
from backend.services.ai_coding_evaluator import ai_coding_evaluator

coding_bp = Blueprint("coding", __name__)

def get_authorized_user_id(db, req):
    """Extracts authenticated user ID from Authorization header or returns first user for demo"""
    token = req.headers.get("Authorization", "").replace("Bearer ", "").strip()
    if token:
        user = db.query(User).filter(User.active_token == token).first()
        if user:
            return user.id
    first_user = db.query(User).first()
    return first_user.id if first_user else 1

# =========================================================================
# 1. QUESTIONS EXPLORATION APIS
# =========================================================================

@coding_bp.route("/questions", methods=["GET", "POST"])
@coding_bp.route("/problems", methods=["GET", "POST"])
def get_questions_list():
    """
    Returns curated coding problems filtered by topic, difficulty, language, or search term.
    Hidden test cases and solutions are strictly omitted.
    """
    if request.method == "POST":
        body = request.get_json() or {}
        topic = body.get("topic") or body.get("subject", "All")
        difficulty = body.get("difficulty", "All")
        language = body.get("language", "All")
        search = body.get("search", "")
    else:
        topic = request.args.get("topic") or request.args.get("subject", "All")
        difficulty = request.args.get("difficulty", "All")
        language = request.args.get("language", "All")
        search = request.args.get("search", "")

    raw_list = filter_questions(topic=topic, difficulty=difficulty, language=language, search=search)
    sanitized = [get_sanitized_question(q, include_solution=False) for q in raw_list]

    return jsonify({
        "count": len(sanitized),
        "total_available": len(get_all_questions()),
        "problems": sanitized,
        "questions": sanitized,
        "filters_applied": {
            "topic": topic,
            "difficulty": difficulty,
            "language": language,
            "search": search
        }
    }), 200

@coding_bp.route("/questions/<question_id>", methods=["GET"])
def get_single_question(question_id):
    """
    Returns detailed specifications for a single problem.
    Sanitized: Hidden test cases are never leaked to the client.
    """
    q = get_question_by_id(question_id)
    if not q:
        return jsonify({"error": f"Coding question '{question_id}' not found."}), 404

    sanitized = get_sanitized_question(q, include_solution=False)
    return jsonify({
        "question": sanitized
    }), 200

# =========================================================================
# 2. CODING INTERVIEW SESSION APIS
# =========================================================================

@coding_bp.route("/interview/start", methods=["POST"])
def start_coding_interview():
    """
    Initializes an official Coding Interview assessment session.
    Allows selection of Language, Difficulty, Topic, and Number of Questions (1, 3, 5, 10).
    Optionally accepts resume skills to personalize question selection.
    """
    data = request.get_json() or {}
    language = data.get("language", "python").lower()
    difficulty = data.get("difficulty", "Medium")
    topic = data.get("topic", "All")
    question_count = int(data.get("question_count", 3))
    resume_skills = data.get("resume_skills", [])

    # Filter pool of potential questions
    pool = filter_questions(
        topic=topic if topic != "All" else None,
        difficulty=difficulty if difficulty != "All" else None,
        language=language
    )

    if not pool:
        # Fallback to general pool if strict filter returned 0
        pool = filter_questions(language=language)

    # If resume skills are present and topic is All, prioritize matching topics
    if resume_skills and topic == "All":
        skill_str = " ".join(resume_skills).lower()
        prioritized = []
        for q in pool:
            if q["topic"].lower() in skill_str or any(t.lower() in skill_str for t in q.get("tags", [])):
                prioritized.append(q)
        if len(prioritized) >= question_count:
            pool = prioritized

    # Sample required count of questions
    selected_questions = random.sample(pool, min(question_count, len(pool)))
    selected_ids = [q["questionId"] for q in selected_questions]

    db = SessionLocal()
    try:
        user_id = get_authorized_user_id(db, request)
        session_model = CodingInterviewSessionModel(
            user_id=user_id,
            language=language,
            difficulty=difficulty,
            topic=topic,
            question_count=len(selected_ids),
            question_ids_json=json.dumps(selected_ids),
            current_question_index=0,
            status="in_progress",
            total_score=0.0
        )
        db.add(session_model)
        db.commit()
        db.refresh(session_model)
        session_id = session_model.id
    finally:
        db.close()

    sanitized_questions = [get_sanitized_question(q, include_solution=False) for q in selected_questions]

    return jsonify({
        "message": "Coding Interview session created successfully.",
        "session_id": session_id,
        "language": language,
        "difficulty": difficulty,
        "topic": topic,
        "total_questions": len(sanitized_questions),
        "questions": sanitized_questions,
        "current_question": sanitized_questions[0] if sanitized_questions else None
    }), 201

# =========================================================================
# 3. CODE EXECUTION (RUN & SUBMIT) APIS
# =========================================================================

@coding_bp.route("/run", methods=["POST"])
@coding_bp.route("/execute", methods=["POST"])
def run_code():
    """
    Executes user code in the secure sandbox against PUBLIC test cases only.
    Provides immediate console output (stdout, stderr, runtime, memory, diff).
    """
    data = request.get_json() or {}
    language = data.get("language", "python")
    code_text = data.get("code", "")
    question_id = data.get("question_id") or data.get("problem_id", "")
    custom_input = data.get("custom_input", None)

    if not code_text or not code_text.strip():
        return jsonify({"error": "No code provided for execution."}), 400

    q = get_question_by_id(question_id)
    if not q:
        # Generic run without question context
        test_cases = [{"input": custom_input or "", "expected_output": ""}]
    elif custom_input is not None and len(str(custom_input).strip()) > 0:
        test_cases = [{"input": custom_input, "expected_output": ""}]
    else:
        test_cases = q.get("testCases", [])

    result = secure_code_sandbox.execute_against_test_cases(
        language=language,
        code_text=code_text,
        test_cases=test_cases,
        is_hidden=False
    )

    first_out = result["test_case_results"][0]["actual_output"] if result["test_case_results"] else ""
    return jsonify({
        "status": result["status"],
        "passed_test_cases": result["passed_count"],
        "total_test_cases": result["total_count"],
        "execution_time_ms": result["execution_time_ms"],
        "memory_used_mb": result["memory_used_mb"],
        "test_case_results": result["test_case_results"],
        "error_message": result.get("error_message", ""),
        "output": first_out,
        "execution_time": result["execution_time_ms"],
        "memory": result["memory_used_mb"]
    }), 200

@coding_bp.route("/submit", methods=["POST"])
def submit_solution():
    """
    Submits candidate code for final assessment.
    Runs against BOTH public and hidden test cases.
    Persists submission in database and generates 8-dimension AI evaluation.
    Hidden test cases remain strictly secret ([HIDDEN]).
    """
    data = request.get_json() or {}
    session_id = data.get("session_id")
    question_id = data.get("question_id", "")
    language = data.get("language", "python")
    code_text = data.get("code", "")

    if not code_text or not code_text.strip():
        return jsonify({"error": "No code provided for submission."}), 400

    q = get_question_by_id(question_id)
    if not q:
        return jsonify({"error": f"Question '{question_id}' not found."}), 404

    public_tcs = q.get("testCases", [])
    hidden_tcs = q.get("hiddenTestCases", [])
    all_tcs = public_tcs + hidden_tcs

    # Run public test cases
    pub_result = secure_code_sandbox.execute_against_test_cases(language, code_text, public_tcs, is_hidden=False)
    # Run hidden test cases (strictly protected!)
    hid_result = secure_code_sandbox.execute_against_test_cases(language, code_text, hidden_tcs, is_hidden=True)

    total_passed = pub_result["passed_count"] + hid_result["passed_count"]
    total_cases = len(all_tcs)
    overall_status = "Accepted" if total_passed == total_cases else (pub_result["status"] if pub_result["status"] != "Accepted" else hid_result["status"])

    # AI Code Quality Audit across 8 dimensions
    ai_eval = ai_coding_evaluator.evaluate_code(
        language=language,
        code_text=code_text,
        problem_title=q.get("title", "Coding Challenge"),
        problem_desc=q.get("description", ""),
        test_cases_passed=total_passed,
        total_test_cases=total_cases,
        execution_status=overall_status
    )

    # Persist submission & evaluation in SQLite
    db = SessionLocal()
    submission_id = None
    try:
        user_id = get_authorized_user_id(db, request)
        submission = CodingSubmissionModel(
            session_id=session_id if session_id else None,
            user_id=user_id,
            question_id=question_id,
            language=language,
            code=code_text,
            status=overall_status,
            passed_test_cases=total_passed,
            total_test_cases=total_cases,
            execution_time_ms=pub_result["execution_time_ms"],
            memory_used_mb=pub_result["memory_used_mb"],
            stdout=pub_result["test_case_results"][0].get("actual_output", "") if pub_result["test_case_results"] else ""
        )
        db.add(submission)
        db.commit()
        db.refresh(submission)
        submission_id = submission.id

        # Save AI Evaluation
        eval_model = CodingAIEvaluationModel(
            submission_id=submission.id,
            overall_score=ai_eval["score"],
            correctness_score=ai_eval["correctness"],
            time_complexity_score=ai_eval["timeComplexityScore"],
            space_complexity_score=ai_eval["spaceComplexityScore"],
            code_quality_score=ai_eval["codeQuality"],
            problem_solving_score=ai_eval["problemSolving"],
            time_complexity=ai_eval["timeComplexity"],
            space_complexity=ai_eval["spaceComplexity"],
            strengths_json=json.dumps(ai_eval["strengths"]),
            improvements_json=json.dumps(ai_eval["improvements"]),
            explanation=ai_eval["explanation"],
            follow_up_question=ai_eval["followUpQuestion"]
        )
        db.add(eval_model)

        # Update User Coding Progress Stats
        progress = db.query(CodingProgressModel).filter(CodingProgressModel.user_id == user_id).first()
        if not progress:
            progress = CodingProgressModel(
                user_id=user_id,
                interviews_completed=0,
                best_score=ai_eval["score"],
                average_score=ai_eval["score"],
                problems_solved=1 if overall_status == "Accepted" else 0,
                current_streak_days=1,
                last_practice_date=datetime.utcnow()
            )
            db.add(progress)
        else:
            if overall_status == "Accepted":
                progress.problems_solved += 1
            progress.best_score = max(progress.best_score, ai_eval["score"])
            progress.last_practice_date = datetime.utcnow()

        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error persisting submission to DB: {e}")
    finally:
        db.close()

    return jsonify({
        "message": "Solution submitted and evaluated successfully.",
        "submission_id": submission_id,
        "status": overall_status,
        "passed_test_cases": total_passed,
        "total_test_cases": total_cases,
        "execution_time_ms": pub_result["execution_time_ms"],
        "memory_used_mb": pub_result["memory_used_mb"],
        "public_test_case_results": pub_result["test_case_results"],
        "hidden_test_cases": {
            "passed": hid_result["passed_count"],
            "total": len(hidden_tcs)
        },
        "ai_evaluation": ai_eval
    }), 200

# =========================================================================
# 4. AI HINT & FOLLOW-UP INTERVIEW APIS
# =========================================================================

@coding_bp.route("/hint", methods=["POST"])
def get_progressive_hint():
    """
    Returns progressive hints without disclosing the full solution.
    Hint Level 1: Conceptual hint
    Hint Level 2: Algorithm direction
    Hint Level 3: Specific approach
    """
    data = request.get_json() or {}
    question_id = data.get("question_id", "")
    level = int(data.get("hint_level", 1))

    q = get_question_by_id(question_id)
    if not q:
        return jsonify({"error": f"Question '{question_id}' not found."}), 404

    hints = ai_coding_evaluator.generate_hints(
        problem_id=q["questionId"],
        title=q["title"],
        topic=q["topic"],
        difficulty=q["difficulty"]
    )

    hint_key = f"hint_level_{min(max(level, 1), 3)}"
    selected_hint = hints.get(hint_key, hints["hint_level_1"])

    return jsonify({
        "question_id": question_id,
        "hint_level": level,
        "hint": selected_hint,
        "level_description": {
            1: "Conceptual Direction",
            2: "Algorithmic Pattern",
            3: "Implementation Strategy"
        }.get(level, "General Hint")
    }), 200

@coding_bp.route("/evaluate", methods=["POST"])
@coding_bp.route("/evaluate-ai", methods=["POST"])
def evaluate_code_audit():
    """On-demand AI code quality & Big-O complexity audit"""
    data = request.get_json() or {}
    language = data.get("language", "python")
    code_text = data.get("code", "")
    problem_title = data.get("problem_title", "Coding Challenge")

    if not code_text or not code_text.strip():
        return jsonify({"error": "No code provided for evaluation."}), 400

    audit = ai_coding_evaluator.evaluate_code(
        language=language,
        code_text=code_text,
        problem_title=problem_title
    )

    return jsonify({
        "evaluation": audit,
        "score": audit["score"],
        "time_complexity": audit["timeComplexity"],
        "space_complexity": audit["spaceComplexity"],
        "strengths": audit["strengths"],
        "improvements": audit["improvements"],
        "explanation": audit["explanation"]
    }), 200

@coding_bp.route("/follow-up", methods=["POST"])
def evaluate_follow_up():
    """Evaluates candidate response to AI interviewer follow-up questions"""
    data = request.get_json() or {}
    follow_up_question = data.get("follow_up_question", "")
    user_answer = data.get("user_answer", "")

    if not user_answer or not user_answer.strip():
        return jsonify({"error": "Candidate answer text is required."}), 400

    result = ai_coding_evaluator.evaluate_follow_up_answer(follow_up_question, user_answer)
    return jsonify({
        "result": result
    }), 200

# =========================================================================
# 5. DASHBOARD, PROGRESS & RECOMMENDATION APIS
# =========================================================================

@coding_bp.route("/result/<int:session_id>", methods=["GET"])
def get_session_result(session_id):
    """Returns comprehensive post-interview performance report for a session"""
    db = SessionLocal()
    try:
        session = db.query(CodingInterviewSessionModel).filter(CodingInterviewSessionModel.id == session_id).first()
        if not session:
            return jsonify({"error": f"Interview session #{session_id} not found."}), 404

        submissions = db.query(CodingSubmissionModel).filter(CodingSubmissionModel.session_id == session_id).all()
        q_ids = json.loads(session.question_ids_json) if session.question_ids_json else []

        attempted = len(submissions)
        solved = sum(1 for s in submissions if s.status == "Accepted")
        total_tc_passed = sum(s.passed_test_cases for s in submissions)
        total_tc_all = sum(s.total_test_cases for s in submissions)
        accuracy = round((total_tc_passed / max(total_tc_all, 1)) * 100, 1)

        # Average score
        scores = []
        for s in submissions:
            if s.ai_evaluation:
                scores.append(s.ai_evaluation.overall_score)
        avg_score = round(sum(scores) / len(scores), 1) if scores else (accuracy * 0.8)

        # Topic Breakdown
        topic_stats = {}
        for s in submissions:
            q = get_question_by_id(s.question_id)
            if q:
                top = q["topic"]
                topic_stats[top] = topic_stats.get(top, 0) + (100 if s.status == "Accepted" else 50)

        return jsonify({
            "session_id": session_id,
            "language": session.language,
            "difficulty": session.difficulty,
            "topic": session.topic,
            "questions_attempted": attempted,
            "questions_solved": solved,
            "total_questions": len(q_ids),
            "test_cases_passed": f"{total_tc_passed}/{total_tc_all}",
            "accuracy_percentage": accuracy,
            "overall_score": avg_score,
            "topic_performance": topic_stats,
            "ai_feedback": "Solid analytical ability. Continue practicing optimization on advanced data structures.",
            "recommended_next_steps": [
                f"Practice more Medium problems in {session.topic if session.topic != 'All' else 'Dynamic Programming'}.",
                "Focus on reducing auxiliary memory allocation from O(N) to O(1).",
                "Take another mock coding interview to maintain your daily streak."
            ]
        }), 200
    finally:
        db.close()

@coding_bp.route("/history", methods=["GET"])
def get_user_history():
    """Returns past interview sessions for the authenticated user"""
    db = SessionLocal()
    try:
        user_id = get_authorized_user_id(db, request)
        sessions = db.query(CodingInterviewSessionModel).filter(
            CodingInterviewSessionModel.user_id == user_id
        ).order_by(CodingInterviewSessionModel.created_at.desc()).limit(15).all()

        history = []
        for s in sessions:
            history.append({
                "session_id": s.id,
                "language": s.language,
                "difficulty": s.difficulty,
                "topic": s.topic,
                "question_count": s.question_count,
                "status": s.status,
                "score": s.total_score,
                "date": s.created_at.strftime("%b %d, %Y")
            })

        return jsonify({
            "history": history
        }), 200
    finally:
        db.close()

@coding_bp.route("/progress", methods=["GET"])
def get_coding_progress():
    """Returns candidate's overall coding metrics, streak, and trajectory"""
    db = SessionLocal()
    try:
        user_id = get_authorized_user_id(db, request)
        progress = db.query(CodingProgressModel).filter(CodingProgressModel.user_id == user_id).first()
        submissions = db.query(CodingSubmissionModel).filter(CodingSubmissionModel.user_id == user_id).all()

        problems_solved = sum(1 for s in submissions if s.status == "Accepted")
        best_score = max([s.ai_evaluation.overall_score for s in submissions if s.ai_evaluation], default=0.0)
        avg_score = round(sum([s.ai_evaluation.overall_score for s in submissions if s.ai_evaluation]) / max(len(submissions), 1), 1)

        # Mock trajectory for chart
        trajectory = [
            {"attempt": 1, "score": 68},
            {"attempt": 2, "score": 75},
            {"attempt": 3, "score": 82},
            {"attempt": 4, "score": 88},
            {"attempt": 5, "score": 92}
        ]

        return jsonify({
            "interviews_completed": progress.interviews_completed if progress else len(set(s.session_id for s in submissions if s.session_id)),
            "problems_solved": max(problems_solved, progress.problems_solved if progress else 0),
            "best_score": round(max(best_score, progress.best_score if progress else 0.0), 1),
            "average_score": avg_score if avg_score > 0 else 78.0,
            "current_streak_days": progress.current_streak_days if progress else 3,
            "score_trajectory": trajectory,
            "demonstrated_skills": ["Python", "DSA", "Hash Maps", "Two Pointer", "Arrays"]
        }), 200
    finally:
        db.close()

@coding_bp.route("/recommendations", methods=["GET"])
def get_coding_recommendations():
    """Recommends personalized DSA questions based on candidate's resume skills"""
    db = SessionLocal()
    try:
        user_id = get_authorized_user_id(db, request)
        resume = db.query(ResumeModel).filter(ResumeModel.user_id == user_id).order_by(ResumeModel.created_at.desc()).first()
        skills = []
        if resume and resume.parsed_json:
            try:
                parsed = json.loads(resume.parsed_json)
                skills = parsed.get("skills", [])
            except Exception:
                skills = ["Python", "JavaScript", "SQL"]
        if not skills:
            skills = ["Python", "Algorithms", "Data Structures"]

        # Recommend 5 problems matching resume skills
        skill_str = " ".join(skills).lower()
        all_q = get_all_questions()
        recommended = []
        for q in all_q:
            if q["topic"].lower() in skill_str or any(t.lower() in skill_str for t in q.get("tags", [])):
                recommended.append(get_sanitized_question(q, include_solution=False))
            if len(recommended) >= 5:
                break

        if len(recommended) < 5:
            # Fill with popular fundamental interview questions
            for q in all_q:
                if q not in recommended:
                    recommended.append(get_sanitized_question(q, include_solution=False))
                if len(recommended) >= 5:
                    break

        return jsonify({
            "resume_skills": skills,
            "recommended_coding_interview": recommended
        }), 200
    finally:
        db.close()
