# test_utils.py
from backend.utils import validate_email, format_date, calculate_match_score, allowed_file

# Test email validation
print(validate_email("test@example.com"))  # True
print(validate_email("invalid_email"))     # False

# Test date formatting
from datetime import datetime
print(format_date(datetime.now()))

# Test match score
user = {"skills": "python,sql,flask", "experience": 2}
job = {"skills_required": "python,flask,django", "min_experience": 1}
print(calculate_match_score(user, job))  # Should print a number between 0-100

# Test file check
print(allowed_file("resume.pdf"))   # True
print(allowed_file("resume.exe"))   # False
