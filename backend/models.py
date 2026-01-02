from extensions import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=True)
    google_id = db.Column(db.String(100), unique=True, nullable=True)
    profile_picture = db.Column(db.String(255), default='default_profile.png')
    bio = db.Column(db.Text, nullable=True)
    skills = db.Column(db.Text, nullable=True) 
    experience = db.Column(db.Text, nullable=True)
    study_history = db.Column(db.Text, nullable=True)
    github_link = db.Column(db.String(255), nullable=True)
    linkedin_link = db.Column(db.String(255), nullable=True)
    portfolio_link = db.Column(db.String(255), nullable=True)
    resume_path = db.Column(db.String(255), nullable=True)
    certificate_path = db.Column(db.String(255), nullable=True)
    trust_score = db.Column(db.Integer, default=10)
    
    # Relationship to applications
    applications = db.relationship('Application', backref='applicant', lazy=True, cascade="all, delete-orphan")

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    required_skills = db.Column(db.Text, nullable=False)
    experience_level = db.Column(db.String(50), nullable=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to applications
    apps = db.relationship('Application', backref='job', lazy=True, cascade="all, delete-orphan")

class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    status = db.Column(db.String(50), default='Delivered')
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)
    match_percentage = db.Column(db.Integer, default=0)