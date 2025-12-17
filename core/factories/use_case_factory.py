from typing import Optional

from core.domain.repositories import (
    IJogoRepository,
    IUserRepository,
)
from core.domain.use_cases import (
    RegisterJogo,
    UpdateJogo,
    DeleteJogo,
    FindJogo,
    FindAllJogos,
    RegisterUser,
    LoginUser,
    FindUserByEmail,
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

    def create_find_jogo(self) -> FindJogo:
        return FindJogo(jogo_repository=self.jogo_repository)

    def create_find_all_jogos(self) -> FindAllJogos:
        return FindAllJogos(jogo_repository=self.jogo_repository)

    def create_update_jogo(self) -> UpdateJogo:
        return UpdateJogo(jogo_repository=self.jogo_repository)

    def create_delete_jogo(self) -> DeleteJogo:
        return DeleteJogo(jogo_repository=self.jogo_repository)

    # User
    def create_register_user(self) -> RegisterUser:
        return RegisterUser(user_repository=self.user_repository)

    def create_login_user(self) -> LoginUser:
        return LoginUser(user_repository=self.user_repository)

    def create_find_user_by_email(self) -> FindUserByEmail:
        return FindUserByEmail(user_repository=self.user_repository)
