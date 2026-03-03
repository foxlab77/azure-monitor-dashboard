import os
from flask import Blueprint, jsonify
from .log_client import send_log

main = Blueprint("main", __name__)

@main.route('/')
def home():
    return "Azure Monitor Dashboard Started 🚀"

@main.route('/api/health')
def health():
    return jsonify({
        "status": "running",
        "message": "API is healthy"
    })

@main.route("/env")
def show_env():
    return os.environ.get("ENVIRONMENT", "not set")

@main.route("/api/log-test")
def log_test():
    success = send_log("Test log from Flask app")
    return {"status": "success" if success else "failed"}