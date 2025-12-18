from core.domain.entities import User
from core.domain.value_objects import Email, Password


def test_should_create_a_valid_user():
    user = User(
        id=1,
        email=Email("test@example.com"),
        password=Password("ValidPass1!"),
    )
    assert user.id == 1
    assert user.email.value == "test@example.com"
    assert user.password.value == "ValidPass1!"