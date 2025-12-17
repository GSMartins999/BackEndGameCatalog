from ..entities.user import User
from ..repositories.i_user_repository import IUserRepository
from ..value_objects import Email


class UpdateUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, *, id: str, email: str | None = None) -> User:
        user = self.user_repository.find_by_id(id)

        if not user:
            raise ValueError("Usuário não encontrado.")

        new_email = Email(email) if email else user.email

        updated_user = User(
            id=user.id,
            email=new_email,
            password=user.password,
        )

        self.user_repository.update(updated_user)

        return updated_user
