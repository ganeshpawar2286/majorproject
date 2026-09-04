"""
PrepWise AI - Unified Career Intelligence Platform
Root Application Entry Point
Author: Ganesh Pawar

Starts the Flask REST API server for backend services.
"""

import os
import sys

# Ensure backend package and workspace root are in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
for path in [BASE_DIR, BACKEND_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

from backend.database import init_db
from backend.app import app
from backend.config import config

if __name__ == "__main__":
    init_db()
    port = config.PORT
    print("=" * 60)
    print(f" PrepWise AI Platform - Backend REST API Server")
    print(f" Environment : {config.FLASK_ENV}")
    print(f" Listening   : http://localhost:{port}")
    print(f" Health Check: http://localhost:{port}/api/health")
    print("=" * 60)
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
