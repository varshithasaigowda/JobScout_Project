import re
import string

def clean_text(text):
    """
    Standardizes text for the Skill Matching algorithm.
    Converts to lowercase, removes punctuation, and strips whitespace.
    """
    if not text or not isinstance(text, str):
        return ""
    
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove URLs (common in project synopses)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # 3. Remove punctuation and special characters
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 4. Remove extra newlines and spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def calculate_trust_percentage(completed_fields, total_fields=10):
    """
    Helper to calculate a raw percentage for UI progress bars.
    """
    if total_fields == 0:
        return 0
    return round((completed_fields / total_fields) * 100)

def format_currency(value):
    """
    Formats the Salary Range for the "Very Large" homepage display.
    Example: 120000 -> $120,000
    """
    try:
        return f"${int(value):,}"
    except (ValueError, TypeError):
        return value

def extract_skills(text):
    """
    A simple logic to turn a comma-separated string from the 
    user profile into a clean list for the Skill Map.
    """
    if not text:
        return []
    return [clean_text(skill) for skill in text.split(',') if skill.strip()]