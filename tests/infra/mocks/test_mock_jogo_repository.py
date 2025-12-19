import pytest

from core.infra.mocks.mock_jogo_repository import MockJogoRepository
from datetime import date
from core.domain.entities.jogo import Jogo
from core.domain.value_objects import NomeDoJogo, Descricao, URL, DataLancamento


def create_jogo(
    id_jogo: int = 1,
    nome: str = "FIFA",
    descricao_texto: str = "Um jogo de futebol completo e divertido.",
    url_texto: str = "https://example.com/photo.jpg",
    data_lancamento_value: date = date(2024, 1, 1),
) -> Jogo:
    return Jogo(
        id_jogo=id_jogo,
        nome_do_jogo=NomeDoJogo(nome),
        descricao=Descricao(descricao_texto),
        url=URL(url_texto),
        data_lancamento=DataLancamento(data_lancamento_value),
    )

@pytest.mark.asyncio
async def test_save_and_find_jogo():
    repo = MockJogoRepository()
    jogo = create_jogo()

    await repo.save(jogo)

    found = await repo.find_by_id(jogo.id_jogo)
    assert found == jogo


@pytest.mark.asyncio
async def test_find_all():
    repo = MockJogoRepository()
    jogo1 = create_jogo(id_jogo=1)
    jogo2 = create_jogo(id_jogo=2, nome="GTA")

    await repo.save(jogo1)
    await repo.save(jogo2)

    jogos = await repo.list_all()
    assert len(jogos) == 2
    assert jogo1 in jogos
    assert jogo2 in jogos


@pytest.mark.asyncio
async def test_update():
    repo = MockJogoRepository()
    jogo = create_jogo()
    await repo.save(jogo)

    updated = create_jogo(id_jogo=jogo.id_jogo, nome="FIFA 25")
    await repo.update(updated)

    found = await repo.find_by_id(jogo.id_jogo)
    assert found.nome_do_jogo.value == "FIFA 25"


@pytest.mark.asyncio
async def test_delete():
    repo = MockJogoRepository()
    jogo1 = create_jogo(id_jogo=1)
    jogo2 = create_jogo(id_jogo=2)

    await repo.save(jogo1)
    await repo.save(jogo2)

    await repo.delete(jogo1.id_jogo)

    assert await repo.find_by_id(jogo1.id_jogo) is None
    assert await repo.find_by_id(jogo2.id_jogo) is not None
