import re

FILLER_WORDS = {"uh", "um", "like", "you know", "actually", "basically", "literally", "sort of", "kind of", "I mean"}

class VocalAnalyzer:
    """
    Vocal Tone, Speech Rate (WPM), and Filler Word Hesitation Analyzer.
    """
    def analyze_vocal_delivery(self, transcript_text, audio_duration_seconds=30.0):
        if not transcript_text or len(transcript_text.strip()) == 0:
            return {
                "wpm": 0,
                "speech_rate_status": "No Audio Speech",
                "filler_count": 0,
                "filler_ratio": 0.0,
                "vocal_tone": "Monotone / Inaudible",
                "fluency_score": 0.0,
                "hesitation_feedback": "No vocal response recorded."
            }

        words = transcript_text.strip().split()
        word_count = len(words)
        
        # Calculate Speech Rate (Words Per Minute)
        duration_minutes = max(0.1, audio_duration_seconds / 60.0)
        wpm = round(word_count / duration_minutes, 1)

        if 130 <= wpm <= 170:
            speech_rate_status = "Optimal Speaking Pace (130-170 WPM)"
        elif wpm > 170:
            speech_rate_status = "Fast-Paced Delivery (> 170 WPM)"
        elif 90 <= wpm < 130:
            speech_rate_status = "Moderate Deliberate Pace (90-130 WPM)"
        else:
            speech_rate_status = "Slow / Pausing Delivery (< 90 WPM)"

        # Count filler words
        text_lower = transcript_text.lower()
        filler_count = 0
        found_fillers = []

        for filler in FILLER_WORDS:
            pattern = r'\b' + re.escape(filler) + r'\b'
            matches = len(re.findall(pattern, text_lower))
            if matches > 0:
                filler_count += matches
                found_fillers.append(filler)

        filler_ratio = round((filler_count / max(1, word_count)) * 100, 1)

        # Classify Vocal Tone
        if filler_count <= 1 and 120 <= wpm <= 170 and word_count >= 15:
            vocal_tone = "Confident & Executive"
            fluency_score = 92.0
            hesitation_feedback = "Exceptional speech cadence. Clear articulation with zero hesitation pauses."
        elif filler_count <= 3 and 100 <= wpm <= 180:
            vocal_tone = "Steady & Technical"
            fluency_score = 80.0
            hesitation_feedback = f"Good delivery pace ({wpm} WPM). Minimal filler words detected."
        else:
            vocal_tone = "Hesitant / Anxious"
            fluency_score = max(40.0, 75.0 - (filler_count * 6.0))
            hesitation_feedback = f"Detected {filler_count} filler pause(s) ({', '.join(found_fillers[:3])}). Practice structured pausing."

        return {
            "wpm": wpm,
            "word_count": word_count,
            "speech_rate_status": speech_rate_status,
            "filler_count": filler_count,
            "filler_ratio": filler_ratio,
            "found_fillers": found_fillers,
            "vocal_tone": vocal_tone,
            "fluency_score": round(fluency_score, 1),
            "hesitation_feedback": hesitation_feedback
        }

vocal_analyzer = VocalAnalyzer()
