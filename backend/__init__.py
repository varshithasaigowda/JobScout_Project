# Backend package initializer
# Blueprints will be imported here in later phases

from flask import Blueprint

auth_bp = Blueprint("auth", __name__)
jobs_bp = Blueprint("jobs", __name__)
recruiter_bp = Blueprint("recruiter", __name__)
