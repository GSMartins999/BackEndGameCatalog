import pytest

from core.domain.use_cases.register_jogo import RegisterJogo
from core.domain.use_cases.edit_jogo import EditJogo
from core.infra.mocks.mock_jogo_repository import MockJogoRepository


@pytest.mark.asyncio
async def test_should_update_jogo():
    repo = MockJogoRepository()
    register = RegisterJogo(repo)
    update = EditJogo(repo)

    jogo = await register.execute(
        nome="FIFA",
        descricao="Futebol",
        url="http://example.com",
        data_lancamento=2024,
    )

    updated = await update.execute(
        jogo.id,
        nome="FIFA 25"
    )

    assert updated.nome.value == "FIFA 25"


@pytest.mark.asyncio
async def test_should_not_update_a_non_existent_jogo():
    repo = MockJogoRepository()
    update = EditJogo(repo)

    with pytest.raises(ValueError, match="Jogo not found"):
        await update.execute("non-existent-id", nome="Novo Nome")
