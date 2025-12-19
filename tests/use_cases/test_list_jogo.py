import pytest
from datetime import date

from core.domain.use_cases.list_jogo import ListJogos
from core.domain.use_cases.register_jogo import RegisterJogo
from core.infra.mocks.mock_jogo_repository import MockJogoRepository

@pytest.mark.asyncio
async def test_should_find_jogo_by_id():
    repo = MockJogoRepository()
    register = RegisterJogo(repo)
    list_jogos = ListJogos(repo)

    jogo = await register.execute(
        nome="GTA",
        descricao="Jogo de ação e aventura.",
        url="https://example.com",
        data_lancamento=date(2023, 6, 15),
    )

    found_list = await list_jogos.execute()

    assert found_list is not None
    assert len(found_list) > 0
    assert found_list[0].id_jogo == jogo.id_jogo


@pytest.mark.asyncio
async def test_should_return_none_if_jogo_not_found():
    repo = MockJogoRepository()
    list_jogos = ListJogos(repo)

    found_list = await list_jogos.execute()
    assert found_list == []
