from backend.models import create_user, get_user_by_email

def test_create_and_fetch_user(db_connection):
    create_user(
        db_connection,
        "test@example.com",
        "password123",
        "Test User"
    )

    user = get_user_by_email(db_connection, "test@example.com")
    assert user is not None
    assert user["email"] == "test@example.com"
