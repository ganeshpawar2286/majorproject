import re
from models.vocal_analyzer import vocal_analyzer
from models.sentence_bert_ats import sentence_bert_ats

class DeepAnswerEvaluator:
    """
    Deep Semantic NLP Answer Evaluator integrating Concept Coverage, Sentence Transformer Embeddings & Vocal Delivery.
    """
    def evaluate_candidate_answer(self, question, target_keywords, user_response, current_difficulty="Medium"):
        if not user_response or len(user_response.strip()) == 0:
            return {
                "overall_score": 0.0,
                "keyword_score": 0.0,
                "coherence_score": 0.0,
                "fluency_score": 0.0,
                "confidence_score": 0.0,
                "vocal_metrics": vocal_analyzer.analyze_vocal_delivery(""),
                "feedback": "No answer provided.",
                "strengths": [],
                "areas_for_improvement": ["Provide a response explaining your solution approach."],
                "next_difficulty": "Easy",
                "performance_tier": "Low"
            }

        text_lower = user_response.lower()
        words = text_lower.split()
        word_count = len(words)

        # 1. Keyword & Concept Coverage Score (Max 100)
        found_keywords = []
        for kw in target_keywords:
            pattern = r'\b' + re.escape(kw.lower()) + r'\b'
            if re.search(pattern, text_lower):
                found_keywords.append(kw)

        if target_keywords:
            keyword_score = round((len(found_keywords) / len(target_keywords)) * 100.0, 1)
        else:
            keyword_score = 75.0

        # Semantic Similarity to Question Prompt
        semantic_sim = sentence_bert_ats.calculate_semantic_similarity(user_response, question)
        concept_coverage_score = round((keyword_score * 0.6) + (semantic_sim * 0.4), 1)

        # 2. Logical Coherence Index
        # Reward transitions: 'because', 'therefore', 'furthermore', 'for example', 'specifically', 'resulted in'
        transitions = ["because", "therefore", "for example", "specifically", "resulted in", "however", "implemented", "engineered"]
        found_trans = [t for t in transitions if t in text_lower]
        
        coherence_base = min(100.0, (word_count / 40.0) * 50.0 + len(found_trans) * 12.0)
        coherence_score = round(max(30.0, min(98.0, coherence_base)), 1)

        # 3. Speech & Vocal Delivery Metrics (WPM, Hesitations, Vocal Tone)
        vocal_res = vocal_analyzer.analyze_vocal_delivery(user_response)
        fluency_score = vocal_res["fluency_score"]

        # 4. Confidence Heuristic (Action verbs + word depth)
        action_verbs = ["engineered", "built", "spearheaded", "developed", "architected", "optimized", "managed", "delivered"]
        found_verbs = [v for v in action_verbs if v in text_lower]
        
        confidence_base = min(100.0, 45.0 + len(found_verbs) * 12.0 + min(35.0, word_count * 0.8))
        confidence_score = round(max(35.0, min(98.0, confidence_base)), 1)

        # 5. Composite Overall Score (35% Keyword/Concept + 25% Coherence + 20% Fluency + 20% Confidence)
        overall_score = round(
            (concept_coverage_score * 0.35) +
            (coherence_score * 0.25) +
            (fluency_score * 0.20) +
            (confidence_score * 0.20), 1
        )

        # Determine Tier & Adaptive Difficulty
        if overall_score >= 78:
            performance_tier = "High"
            next_difficulty = "Hard" if current_difficulty == "Medium" else "Medium"
        elif overall_score >= 55:
            performance_tier = "Medium"
            next_difficulty = "Medium"
        else:
            performance_tier = "Low"
            next_difficulty = "Easy"

        # Generate Feedback
        strengths = []
        areas = []

        if found_keywords:
            strengths.append(f"Demonstrated concept knowledge by incorporating key domain terms: {', '.join(found_keywords[:4])}.")
        if vocal_res["vocal_tone"] == "Confident & Executive":
            strengths.append("Paced voice delivery at optimal rate with strong executive confidence.")

        missing_kw = [kw for kw in target_keywords if kw not in found_keywords]
        if missing_kw:
            areas.append(f"Incorporate missing core concepts: {', '.join(missing_kw[:3])}.")
        if vocal_res["filler_count"] > 2:
            areas.append(f"Reduce filler pauses ({', '.join(vocal_res['found_fillers'][:2])}) to project higher authority.")
        if word_count < 30:
            areas.append("Elaborate on your architectural design choices and project outcomes.")

        feedback = f"Response Score: {overall_score}%. Delivery tone: '{vocal_res['vocal_tone']}' ({vocal_res['wpm']} WPM). {vocal_res['hesitation_feedback']}"

        return {
            "overall_score": overall_score,
            "keyword_score": concept_coverage_score,
            "coherence_score": coherence_score,
            "fluency_score": fluency_score,
            "confidence_score": confidence_score,
            "vocal_metrics": vocal_res,
            "feedback": feedback,
            "strengths": strengths if strengths else ["Good effort on initiating answer response."],
            "areas_for_improvement": areas if areas else ["Maintain this high standard of technical response."],
            "next_difficulty": next_difficulty,
            "performance_tier": performance_tier
        }

deep_answer_evaluator = DeepAnswerEvaluator()
