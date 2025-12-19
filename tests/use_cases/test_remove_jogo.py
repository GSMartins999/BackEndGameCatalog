import pytest
from datetime import date

from core.domain.use_cases.remove_jogo import RemoveJogo
from core.domain.use_cases.register_jogo import RegisterJogo
from core.infra.mocks.mock_jogo_repository import MockJogoRepository

@pytest.mark.asyncio
async def test_should_delete_a_jogo():
    repo = MockJogoRepository()
    register = RegisterJogo(repo)
    delete = RemoveJogo(repo)

    jogo = await register.execute(
        nome="FIFA",
        descricao="Um jogo de futebol completo.",
        url="https://example.com",
        data_lancamento=date(2024, 1, 1),
    )

    await delete.execute(jogo.id_jogo)

    assert len(repo.jogos) == 0


@pytest.mark.asyncio
async def test_should_not_delete_a_non_existent_jogo():
    repo = MockJogoRepository()
    delete = RemoveJogo(repo)

    with pytest.raises(ValueError, match="Jogo not found"):
        await delete.execute("non-existent-id")
