from backend.auth import is_valid_login

def test_valid_login():
    user = {
        "email": "user@test.com",
        "password": "hashed_password"
    }

    assert is_valid_login("hashed_password", user["password"]) is True


def test_invalid_login():
    assert is_valid_login("wrong", "hashed_password") is False
