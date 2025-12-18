import pytest

from core.domain.use_cases.list_jogo import ListJogos
from core.domain.use_cases.register_jogo import RegisterJogo
from core.infra.mocks.mock_jogo_repository import MockJogoRepository


@pytest.mark.asyncio
async def test_should_find_jogo_by_id():
    repo = MockJogoRepository()
    register = RegisterJogo(repo)
    find = ListJogos(repo)

    jogo = await register.execute(
        nome="GTA",
        descricao="Ação",
        url="http://example.com",
        data_lancamento=2023,
    )

    found = await find.execute(jogo.id)

    assert found is not None
    assert found.id == jogo.id


@pytest.mark.asyncio
async def test_should_return_none_if_jogo_not_found():
    repo = MockJogoRepository()
    find = ListJogos(repo)

    found = await find.execute("non-existent-id")
    assert found is None
