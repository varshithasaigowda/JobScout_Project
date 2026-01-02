from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from config import Config
from extensions import db, oauth 
from backend.models import User
import os

auth_bp = Blueprint('auth', __name__)

google = oauth.register(
    name='google',
    server_metadata_url=Config.GOOGLE_CONF_URL,
    client_kwargs={'scope': 'openid email profile'}
)

def calculate_trust(user):
    # Updated to remove profile picture points since we use Letter Avatars
    score = 15
    if user.bio: score += 20
    if user.skills: score += 25
    if user.resume_path: score += 25
    if user.github_link: score += 15
    return min(score, 100)

@auth_bp.route('/google')
def google_login():
    redirect_uri = url_for('auth.callback', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth_bp.route('/callback')
def callback():
    try:
        token = google.authorize_access_token()
        user_info = google.parse_id_token(token, nonce=None)
    except Exception as e:
        flash("Google authentication failed.", "error")
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        user = User(
            username=user_info.get('name', 'User'),
            email=user_info['email'],
            google_id=user_info.get('sub')
        )
        db.session.add(user)
        db.session.commit()
    
    login_user(user, remember=True)
    # Set this session flag so app.py knows to show the success message
    session['google_login_success'] = True
    return redirect(url_for('dashboard'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('dashboard'))
    if request.method == 'POST':
        # FIXED: Matching the new names from the login.html template
        email = request.form.get('user_email_login')
        password = request.form.get('user_password_login')
        
        user = User.query.filter_by(email=email).first()
        if user and user.password_hash and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            return redirect(url_for('dashboard'))
            
        flash('Invalid Email or Password', 'error')
    return render_template('login.html')

@auth_bp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.username = request.form.get('username')
        current_user.bio = request.form.get('bio')
        current_user.skills = request.form.get('skills')
        current_user.github_link = request.form.get('github_link')

        # File storage for Resume only (Profile Pic removed)
        if 'resume' in request.files:
            file = request.files['resume']
            if file and file.filename != '':
                base_dir = os.path.abspath(os.path.dirname(__file__))
                upload_folder = os.path.join(base_dir, 'static', 'uploads')
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)
                    
                filename = secure_filename(f"user_{current_user.id}_resume.pdf")
                file.save(os.path.join(upload_folder, filename))
                current_user.resume_path = filename

        current_user.trust_score = calculate_trust(current_user)
        db.session.commit()
        # Message changed from "DNA Updated" to "Profile Updated"
        flash("Profile Updated!", "success")
        return redirect(url_for('dashboard'))
    return render_template('edit_profile.html', user=current_user)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form.get('email')
        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'error')
            return redirect(url_for('auth.login'))
        
        user = User(
            username=request.form.get('username'), 
            email=email, 
            password_hash=generate_password_hash(request.form.get('password'), method='scrypt')
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))