from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from core.domain.entities import User
from core.domain.repositories import IUserRepository
from core.infra.orm.user import User as UserModel


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, user: User) -> None:
        user_model = UserModel(
            id=user.id,
            name=user.name.value,
            email=user.email.value,
            password=user.password.value,
        )
        self.session.add(user_model)
        await self.session.commit()

    async def find_by_email(self, email: str) -> Optional[User]:
        return next((user for user in self.users if user.email.value == email), None)

    async def find_by_id(self, id: str) -> Optional[User]:
        return next((user for user in self.users if user.id == id), None)

    async def update(self, user: User) -> None:
        index = next((i for i, u in enumerate(self.users) if u.id == user.id), None)
        if index is not None:
            self.users[index] = user

    async def delete(self, id: str) -> None:
        self.users = [user for user in self.users if user.id != id]
