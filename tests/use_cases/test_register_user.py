import pytest

from core.domain.use_cases.register_user import RegisterUser
from core.infra.mocks.mock_user_repository import MockUserRepository


@pytest.mark.asyncio
async def test_should_register_a_new_user():
    user_repository = MockUserRepository()
    register_user = RegisterUser(user_repository)

    user = await register_user.execute(email="test@example.com", password="ValidPass1!", name="Test User")

    assert user.email.value == "test@example.com"
    assert len(user_repository.users) == 1


@pytest.mark.asyncio
async def test_should_not_register_an_existing_user():
    user_repository = MockUserRepository()
    register_user = RegisterUser(user_repository)

    await register_user.execute(email="test@example.com", password="ValidPass1!", name="Test User")

    with pytest.raises(ValueError, match="User already exists"):
        await register_user.execute(email="test@example.com", password="ValidPass1!", name="Another User")
