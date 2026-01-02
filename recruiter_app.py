from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'jobscout.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Models (Fixed to match backend/models.py plural names) ---
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    skills = db.Column(db.Text)
    trust_score = db.Column(db.Integer)
    bio = db.Column(db.Text)
    github_link = db.Column(db.String(255))

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    company = db.Column(db.String(150))
    description = db.Column(db.Text)

class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    status = db.Column(db.String(50), default='Delivered')
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship backrefs
    applicant = db.relationship('User', backref='app_list')
    job_ref = db.relationship('Job', backref='app_list')

def send_background_email(target_email, subject, body):
    sender_email = "recruiter4812@gmail.com"
    app_password = "johomjbyjvxqjpfx" 
    msg = MIMEMultipart()
    msg['From'] = f"JobScout Recruitment <{sender_email}>"
    msg['To'] = target_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

@app.route('/')
def index():
    apps = Application.query.order_by(Application.applied_at.desc()).all()
    return render_template('recruiter_dashboard.html', apps=apps)

@app.route('/update_status', methods=['POST'])
def update_status():
    app_id = request.form.get('app_id')
    status = request.form.get('status')
    custom_message = request.form.get('message') 
    
    application = db.session.get(Application, app_id)
    if application:
        application.status = status
        db.session.commit()
        
        if application.applicant and application.applicant.email:
            subject = f"Application Update: {application.job_ref.title} at {application.job_ref.company}"
            send_background_email(application.applicant.email, subject, custom_message)
            
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print(f"--- Recruiter App Booting ---")
    print(f"Connecting to DB at: {db_path}")
    app.run(port=5001, debug=True)