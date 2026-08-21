import os
import sys

# Ensure root workspace directory is in python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from flask import Flask, jsonify
from flask_cors import CORS
from backend.database import init_db
from backend.routes_auth import auth_bp
from backend.routes_resume import resume_bp
from backend.routes_jobs import jobs_bp
from backend.routes_interview import interview_bp
from backend.routes_dashboard import dashboard_bp

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Register API blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(resume_bp, url_prefix="/api/resume")
app.register_blueprint(jobs_bp, url_prefix="/api/jobs")
app.register_blueprint(interview_bp, url_prefix="/api/interview")
app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "online",
        "service": "PrepWise AI Backend REST API",
        "version": "1.0.0"
    }), 200

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting PrepWise AI Flask server on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
