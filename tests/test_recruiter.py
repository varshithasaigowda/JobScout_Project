from backend.recruiter import update_application_status

def test_application_status_update():
    app = {"status": "APPLIED"}

    update_application_status(app, "ACCEPTED")

    assert app["status"] == "ACCEPTED"
