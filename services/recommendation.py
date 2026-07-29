def recommend_jobs(user_skills, jobs, target_role=""):
    normalized_user_skills = {skill.lower() for skill in user_skills}
    ranked_jobs = []

    for job in jobs:
        required_skills = {skill.lower() for skill in job["skills"]}
        overlap = normalized_user_skills.intersection(required_skills)
        score = len(overlap) / max(len(required_skills), 1)
        if target_role and target_role.lower() in job["title"].lower():
            score += 0.2
        ranked_jobs.append({
            **job,
            "match_score": round(score * 100),
            "matched_skills": sorted(overlap),
            "missing_skills": sorted(required_skills - normalized_user_skills),
        })

    return sorted(ranked_jobs, key=lambda item: item["match_score"], reverse=True)[:3]
