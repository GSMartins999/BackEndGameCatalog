from core.domain.use_cases import RegisterUser
from core.factories.use_case_factory import UseCaseFactory
from core.infra.mocks import (
    MockUserRepository,
    MockJogoRepository,
)


def test_should_create_use_case_with_internal_mocks():
    factory = UseCaseFactory()
    register_user_use_case = factory.create_register_user()

    assert isinstance(register_user_use_case, RegisterUser)
    assert isinstance(register_user_use_case.user_repository, MockUserRepository)


def test_should_create_use_case_with_external_mocks():
    user_repo = MockUserRepository()
    jogo_repo = MockJogoRepository()

    factory = UseCaseFactory(
        user_repository=user_repo,
        jogo_repository=jogo_repo,
    )

    use_case = factory.create_register_jogo()

    assert use_case.user_repository is user_repo
    assert use_case.jogo_repository is jogo_repo
