from flask import Flask, render_template, redirect, url_for, session, flash
from config import Config
import os, pandas as pd
from extensions import db, login_manager, oauth 
from flask_login import login_required, current_user
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    oauth.init_app(app)  
    
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = "info"

    @app.before_request
    def make_session_permanent():
        session.permanent = True

    @login_manager.user_loader
    def load_user(user_id):
        from backend.models import User
        return db.session.get(User, int(user_id))

    from backend.auth import auth_bp
    from backend.jobs import jobs_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(jobs_bp, url_prefix='/jobs')

    @app.route('/')
    def home():
        if current_user.is_authenticated:
            if session.get('google_login_success'):
                flash("Logged in successfully via Google!", "success")
                session.pop('google_login_success', None)
            return redirect(url_for('dashboard'))
        return render_template('index.html')

    @app.route('/dashboard')
    @login_required  
    def dashboard():
        from backend.models import Application
        user_apps = Application.query.filter_by(user_id=current_user.id).order_by(Application.applied_at.desc()).all()
        # FIX: Added 'now' so user_dashboard.html can calculate application time
        return render_template('user_dashboard.html', user=current_user, apps=user_apps, now=datetime.utcnow())

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        from backend.models import Job
        if Job.query.count() == 0:
            csv_path = 'data/jobs_dataset.csv'
            if os.path.exists(csv_path):
                try:
                    df = pd.read_csv(csv_path, quotechar='"', skipinitialspace=True, on_bad_lines='skip')
                    df.columns = df.columns.str.strip().str.lower()
                    
                    for _, row in df.iterrows():
                        new_job = Job(
                            title=str(row.get('title', 'Unknown Role')), 
                            company=str(row.get('company', 'Unknown Company')),
                            location=str(row.get('location', 'Remote')), 
                            description=str(row.get('description', 'No description.')),
                            required_skills=str(row.get('required_skills', '')),
                            experience_level=str(row.get('experience_level', 'Entry'))
                        )
                        db.session.add(new_job)
                    db.session.commit()
                    print("✅ Database seeded successfully with jobs.")
                except Exception as e:
                    print(f"❌ CSV Seeding Error: {e}")
        
        print("🧬 JOB SCOUT Engine Started.")

    app.run(debug=True, port=5000)