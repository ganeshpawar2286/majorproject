import os
import sys

# Ensure root workspace directory and backend package are in python path
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BACKEND_DIR)
for path in [BASE_DIR, BACKEND_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

from config import config
from flask import Flask, jsonify
from flask_cors import CORS
from backend.database import init_db
from backend.routes_auth import auth_bp
from backend.routes_resume import resume_bp
from backend.routes_jobs import jobs_bp
from backend.routes_interview import interview_bp
from backend.routes_dashboard import dashboard_bp
from backend.routes_coding import coding_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Register API blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(resume_bp, url_prefix="/api/resume")
app.register_blueprint(jobs_bp, url_prefix="/api/jobs")
app.register_blueprint(interview_bp, url_prefix="/api/interview")
app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
app.register_blueprint(coding_bp, url_prefix="/api/coding")


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "online",
        "service": "PrepWise AI Backend REST API",
        "version": "1.0.0",
        "environment": config.FLASK_ENV
    }), 200

if __name__ == "__main__":
    init_db()
    port = config.PORT
    print(f"Starting PrepWise AI Flask server on http://localhost:{port} (Env: {config.FLASK_ENV})")
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
