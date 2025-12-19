from typing import Optional

from core.domain.repositories import (
    IJogoRepository,
    IUserRepository,
)
from core.domain.use_cases import (
    RegisterJogo,
    EditJogo,
    RemoveJogo,
    ListJogos,
    DeleteUser,
    RegisterUser,
    LoginUser,
    FindUserByEmail,
    UpdateUser,
)
from core.infra.mocks import (
    MockJogoRepository,
    MockUserRepository,
)


class UseCaseFactory:
    def __init__(
        self,
        jogo_repository: Optional[IJogoRepository] = None,
        user_repository: Optional[IUserRepository] = None,
    ):
        self.jogo_repository = jogo_repository or MockJogoRepository()
        self.user_repository = user_repository or MockUserRepository()

    # Jogo
    def create_register_jogo(self) -> RegisterJogo:
        return RegisterJogo(jogo_repository=self.jogo_repository)

    def create_list_jogos(self) -> ListJogos:
        return ListJogos(jogo_repository=self.jogo_repository)

    def create_find_jogo(self) -> ListJogos:
        return ListJogos(jogo_repository=self.jogo_repository)

    def create_update_jogo(self) -> EditJogo:
        return EditJogo(jogo_repository=self.jogo_repository)

    def create_delete_jogo(self) -> RemoveJogo:
        return RemoveJogo(jogo_repository=self.jogo_repository)

    # User
    def create_register_user(self) -> RegisterUser:
        return RegisterUser(user_repository=self.user_repository)

    def create_login_user(self) -> LoginUser:
        return LoginUser(user_repository=self.user_repository)

    def create_find_user_by_email(self) -> FindUserByEmail:
        return FindUserByEmail(user_repository=self.user_repository)

    def create_delete_user(self) -> DeleteUser:
        return DeleteUser(user_repository=self.user_repository)

    def create_update_user(self) -> UpdateUser:
        return UpdateUser(user_repository=self.user_repository)
