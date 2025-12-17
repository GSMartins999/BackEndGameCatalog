from ..repositories.i_user_repository import IUserRepository


class DeleteUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, *, id: str) -> None:
        user = self.user_repository.find_by_id(id)
        if not user:
            return

        self.user_repository.delete(id)
