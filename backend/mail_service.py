from flask_mail import Message
from flask import render_template_string
from app import mail
from config import Config

def send_status_update_email(user_email, user_name, job_title, new_status):
    """
    Sends a high-end, branded HTML email notification to the user 
    when their application status changes.
    """
    
    # Define status-specific colors for the email
    status_colors = {
        'Accepted': '#50C878', # Emerald
        'Rejected': '#461D3A', # Brown Coffee
        'Verified': '#BA71A2', # Pearly Purple
        'Delivered': '#D183A9' # Middle Purple
    }
    
    accent_color = status_colors.get(new_status, '#BA71A2')

    subject = f"JOB SCOUT: Update for {job_title}"
    
    # High-end HTML Template for the Email
    html_content = f"""
    <div style="background-color: #3A345B; padding: 40px; font-family: 'Inter', sans-serif; color: white; text-align: center;">
        <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 20px; max-width: 500px; margin: 0 auto;">
            <h1 style="color: #F3C8DD; margin-bottom: 20px;">JOB SCOUT</h1>
            <p style="font-size: 1.1rem; line-height: 1.6;">Hello {user_name},</p>
            <p style="color: #D183A9;">The status of your application for <strong>{job_title}</strong> has been updated to:</p>
            
            <div style="display: inline-block; margin: 20px 0; padding: 10px 30px; background-color: {accent_color}; color: white; border-radius: 50px; font-weight: bold; text-transform: uppercase; letter-spacing: 2px;">
                {new_status}
            </div>
            
            <p style="font-size: 0.9rem; color: #71557A; margin-top: 20px;">
                Log in to your dashboard to view recruiter feedback and next steps.
            </p>
            
            <a href="http://127.0.0.1:5000/dashboard" style="display: inline-block; margin-top: 30px; padding: 12px 25px; background-color: #BA71A2; color: white; text-decoration: none; border-radius: 8px; font-weight: 600;">
                View Dashboard
            </a>
        </div>
        <p style="margin-top: 30px; color: #71557A; font-size: 0.8rem;">&copy; 2025 JOB SCOUT AI. Automated Priority Matching.</p>
    </div>
    """

    msg = Message(
        subject,
        sender=Config.MAIL_USERNAME,
        recipients=[user_email]
    )
    msg.html = html_content

    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Mail Error: {e}")
        return False