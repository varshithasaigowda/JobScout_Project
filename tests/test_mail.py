from backend.mail_service import format_email_body

def test_email_body_format():
    body = format_email_body("ACCEPTED", "Congrats")

    assert "ACCEPTED" in body
    assert "Congrats" in body
