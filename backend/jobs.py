import random
from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from extensions import db
from backend.models import Job, Application

jobs_bp = Blueprint('jobs', __name__)

def calculate_match(user_skills_raw, job_skills_raw):
    if not user_skills_raw or not job_skills_raw: return 0
    u_set = set([s.strip().lower() for s in user_skills_raw.split(',') if s.strip()])
    j_list = [s.strip().lower() for s in job_skills_raw.split(',') if s.strip()]
    if not j_list: return 0
    matches = sum(1 for s in j_list if s in u_set)
    score = int((matches / len(j_list)) * 100)
    return min(score, 100)

@jobs_bp.route('/discover')
@login_required
def discover():
    sort_priority = request.args.get('sort', 'off')
    all_jobs = Job.query.all()
    applied_job_ids = [app.job_id for app in current_user.applications]
    
    job_matches = []
    for job in all_jobs:
        score = calculate_match(current_user.skills or "", job.required_skills)
        if score >= 50:
            job_matches.append({
                'job': job, 
                'score': score, 
                'applied': job.id in applied_job_ids
            })
    
    if sort_priority == 'on':
        job_matches = sorted(job_matches, key=lambda x: x['score'], reverse=True)
    else:
        random.shuffle(job_matches)
        
    return render_template('discover.html', jobs=job_matches, sort_state=sort_priority)

@jobs_bp.route('/apply/<int:job_id>', methods=['POST'])
@login_required
def apply(job_id):
    # 1. Check existing applications
    user_apps = Application.query.filter_by(user_id=current_user.id).all()
    
    if len(user_apps) >= 15:
        # 2. Calculate Response Rate (Status must not be 'Delivered')
        responded_apps = [a for a in user_apps if a.status != 'Delivered']
        # 80% of 15 is 12
        if len(responded_apps) < 12:
            return jsonify({
                "status": "limit_reached", 
                "message": f"Application Limit Reached (15/15). You need 80% responses (currently {len(responded_apps)}/12 required) to unlock more slots."
            })

    existing = Application.query.filter_by(user_id=current_user.id, job_id=job_id).first()
    if not existing:
        job = Job.query.get_or_404(job_id)
        score = calculate_match(current_user.skills or "", job.required_skills)
        new_app = Application(user_id=current_user.id, job_id=job_id, match_percentage=score)
        db.session.add(new_app)
        db.session.commit()
        return jsonify({"status": "applied", "message": "Applied for this job"})
    return jsonify({"status": "already_applied"})

@jobs_bp.route('/cancel/<int:job_id>', methods=['POST'])
@login_required
def cancel(job_id):
    app = Application.query.filter_by(user_id=current_user.id, job_id=job_id).first()
    if app:
        time_limit = app.applied_at + timedelta(hours=24)
        if datetime.utcnow() > time_limit:
            return jsonify({"status": "blocked", "message": "Cancellation period expired (24h limit)."})
            
        db.session.delete(app)
        db.session.commit()
        return jsonify({"status": "cancelled"})
    return jsonify({"status": "not_found"})

@jobs_bp.route('/api/get-all-skills')
@login_required
def get_all_skills():
    all_jobs = Job.query.all()
    unique_skills = set()
    for job in all_jobs:
        if job.required_skills:
            parts = [s.strip() for s in job.required_skills.split(',') if s.strip()]
            unique_skills.update(parts)
    return jsonify(sorted(list(unique_skills)))