from backend.models import db
from config import Config

def update_user_trust_score(user):
    """
    Calculates and updates the User's Trust Score (0-100)
    based on the weights defined in config.py.
    """
    score = 0
    weights = Config.TRUST_SCORE_WEIGHTS
    
    # 1. Profile Completeness (40 pts)
    # Check if essential bio fields are filled
    profile_fields = [user.study_history, user.skills, user.location_preference]
    completed_fields = [f for f in profile_fields if f and len(f) > 5]
    profile_ratio = len(completed_fields) / len(profile_fields)
    score += (profile_ratio * weights['profile_complete'])

    # 2. Projects & Synopsis (30 pts)
    # We look for a detailed synopsis (Professional DNA)
    if user.project_synopsis:
        if len(user.project_synopsis) > 200:
            score += weights['projects_added']  # Full points for deep detail
        elif len(user.project_synopsis) > 50:
            score += (weights['projects_added'] * 0.5) # Partial points

    # 3. External Validation (GitHub - 15 pts)
    if user.github_link and "github.com/" in user.github_link.lower():
        score += weights['github_linked']

    # 4. Professional Validation (LinkedIn - 15 pts)
    if user.linkedin_link and "linkedin.com/" in user.linkedin_link.lower():
        score += weights['linkedin_linked']

    # Final Adjustment: Round and Cap at 100
    user.trust_score = min(round(score), 100)
    db.session.commit()
    
    return user.trust_score

def get_score_color(score):
    """
    Returns the specific theme color associated with the score level.
    Used for the Trust Gauge animation.
    """
    if score >= 80:
        return "#50C878" # Emerald Success
    elif score >= 50:
        return "#BA71A2" # Pearly Purple (Theme Primary)
    else:
        return "#D183A9" # Middle Purple (Theme Secondary)