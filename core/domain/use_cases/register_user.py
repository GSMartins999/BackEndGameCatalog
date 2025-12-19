# domain/use_cases/register_user.py
import uuid
from typing import Optional

from ..entities.user import User
from ..repositories.i_user_repository import IUserRepository
from ..value_objects import Email, Password


class RegisterUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str, password: str, name: Optional[str] = None) -> User:
        user = await self.user_repository.find_by_email(email)
        if user:
            raise ValueError("User already exists")

        hashed_password = self._hash_password(password)

        user = User(
            id=str(uuid.uuid4()),
            email=Email(email),
            password=Password(hashed_password),
        )

        await self.user_repository.save(user)

        return user

    def _hash_password(self, password: str) -> str:
        return f"hashed_{password}"
