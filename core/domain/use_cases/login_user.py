from ..entities.user import User
from ..repositories.i_user_repository import IUserRepository


class LoginUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, *, email: str, password: str) -> User:
        user = self.user_repository.find_by_email(email)

        if not user:
            raise ValueError("Credenciais inválidas.")

        if not self._compare_password(password, user.password.value):
            raise ValueError("Credenciais inválidas.")

        return user

    def _compare_password(self, password: str, hashed_password: str) -> bool:
        return f"hashed_{password}" == hashed_password
