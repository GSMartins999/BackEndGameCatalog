from abc import ABC, abstractmethod
from typing import Optional
from core.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> None: ...

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]: ...

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[User]: ...

    @abstractmethod
    def update(self, user: User) -> None: ...

    @abstractmethod
    def delete(self, id: str) -> None: ...
