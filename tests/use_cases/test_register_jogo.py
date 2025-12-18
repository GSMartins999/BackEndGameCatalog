import pytest

from core.domain.use_cases.register_jogo import RegisterJogo
from core.infra.mocks.mock_jogo_repository import MockJogoRepository


@pytest.mark.asyncio
async def test_should_register_a_jogo():
    repo = MockJogoRepository()
    use_case = RegisterJogo(repo)

    jogo = await use_case.execute(
        nome="Need for Speed",
        descricao="Corrida",
        url="http://example.com",
        data_lancamento=2025,
    )

    assert jogo.nome.value == "Need for Speed"
    assert len(repo.jogos) == 1
