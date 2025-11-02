import pytest

from domain.use_cases.login_user import LoginUser
from domain.use_cases.register_user import RegisterUser
from tests.mocks.mock_user_repository import MockUserRepository


@pytest.mark.asyncio
async def test_should_login_a_user():
    user_repository = MockUserRepository()
    register_user = RegisterUser(user_repository)
    login_user = LoginUser(user_repository)

    await register_user.execute("Test User", "test@example.com", "ValidPass1!")
    user = await login_user.execute("test@example.com", "ValidPass1!")

    assert user.name.value == "Test User"


@pytest.mark.asyncio
async def test_should_not_login_with_invalid_email():
    user_repository = MockUserRepository()
    login_user = LoginUser(user_repository)

    with pytest.raises(ValueError, match="Invalid credentials"):
        await login_user.execute("wrong@example.com", "ValidPass1!")


@pytest.mark.asyncio
async def test_should_not_login_with_invalid_password():
    user_repository = MockUserRepository()
    register_user = RegisterUser(user_repository)
    login_user = LoginUser(user_repository)

    await register_user.execute("Test User", "test@example.com", "ValidPass1!")

    with pytest.raises(ValueError, match="Invalid credentials"):
        await login_user.execute("test@example.com", "wrong_password")
