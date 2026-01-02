from backend.trust_score import calculate_trust_score

def test_trust_score_range():
    user = {
        "full_name": "Test",
        "email": "t@test.com",
        "resume_path": "resume.pdf",
        "skills": "Python",
        "experience": "2 years"
    }

    applications = [
        {"status": "ACCEPTED"},
        {"status": "HOLD"},
        {"status": "REJECTED"}
    ]

    score = calculate_trust_score(user, applications)

    assert 0 <= score <= 100
