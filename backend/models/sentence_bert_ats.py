import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    from sentence_transformers import SentenceTransformer, util
    SBERT_AVAILABLE = True
except Exception:
    SBERT_AVAILABLE = False

class SentenceBertATS:
    """
    Sentence-BERT & Sublinear Vector Transformer for Deep Semantic ATS Resume Matching.
    """
    def __init__(self):
        self.sbert_model = None
        if SBERT_AVAILABLE:
            try:
                self.sbert_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            except Exception:
                self.sbert_model = None
        
        self.fallback_vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
            stop_words='english',
            max_features=5000
        )

    def calculate_semantic_similarity(self, resume_text, job_text):
        """
        Computes deep semantic similarity between candidate resume and job description.
        Returns similarity score (0.0 to 100.0%).
        """
        if not resume_text or not job_text:
            return 0.0

        if self.sbert_model:
            try:
                emb_res = self.sbert_model.encode(resume_text, convert_to_tensor=True)
                emb_job = self.sbert_model.encode(job_text, convert_to_tensor=True)
                sim = float(util.cos_sim(emb_res, emb_job)[0][0])
                return round(max(0.0, min(100.0, sim * 100.0)), 1)
            except Exception as e:
                print(f"SBERT embedding evaluation fallback: {e}")

        # High-precision Sublinear TF Vectorizer Fallback
        try:
            tfidf = self.fallback_vectorizer.fit_transform([resume_text, job_text])
            sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
            return round(max(0.0, min(100.0, float(sim) * 100.0)), 1)
        except Exception:
            return 50.0

sentence_bert_ats = SentenceBertATS()
