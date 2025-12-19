from __future__ import annotations
from typing import List, Optional

from core.domain.entities.user import User
from core.domain.repositories.i_user_repository import IUserRepository
from core.domain.value_objects import Email, Password


class MockUserRepository(IUserRepository):
    _instance: "MockUserRepository" | None = None

    def __init__(self):
        self.users: List[User] = []

    @classmethod
    def get_instance(cls) -> "MockUserRepository":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # ---------------- Repositório ----------------

    async def save(self, user: User) -> None:
        self.users.append(user)

    async def find_by_email(self, email: str) -> Optional[User]:
        return next(
            (u for u in self.users if u.email.value == email),
            None,
        )

    async def find_by_id(self, id: str) -> Optional[User]:
        return next(
            (u for u in self.users if u.id == id),
            None,
        )

    async def update(self, user: User) -> None:
        for index, u in enumerate(self.users):
            if u.id == user.id:
                self.users[index] = user
                break

    async def delete(self, id: str) -> None:
        self.users = [u for u in self.users if u.id != id]

    # ---------------- Utilitário ----------------

    def reset(self) -> None:
        self.users = []
