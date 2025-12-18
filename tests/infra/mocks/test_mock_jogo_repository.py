import pytest

from core.domain.entities import Jogo
from core.domain.value_objects import nome_jogo, descricao, url
from core.infra.mocks.mock_jogo_repository import MockJogoRepository


def create_jogo(
    id: str = "1",
    nome: str = "FIFA",
    descricao_texto: str = "Futebol",
    url_texto: str = "http://example.com",
    data_lancamento: int = 2024,
) -> Jogo:
    return Jogo(
        id=id,
        nome=nome_jogo(nome),
        descricao=descricao(descricao_texto),
        url=url(url_texto),
        data_lancamento=data_lancamento,
    )


@pytest.mark.asyncio
async def test_save_and_find_jogo():
    repo = MockJogoRepository()
    jogo = create_jogo()

    await repo.save(jogo)

    found = await repo.find_by_id(jogo.id)
    assert found == jogo


@pytest.mark.asyncio
async def test_find_all():
    repo = MockJogoRepository()
    jogo1 = create_jogo(id="1")
    jogo2 = create_jogo(id="2", nome="GTA")

    await repo.save(jogo1)
    await repo.save(jogo2)

    jogos = await repo.find_all()
    assert len(jogos) == 2
    assert jogo1 in jogos
    assert jogo2 in jogos


@pytest.mark.asyncio
async def test_update():
    repo = MockJogoRepository()
    jogo = create_jogo()
    await repo.save(jogo)

    updated = create_jogo(id=jogo.id, nome="FIFA 25")
    await repo.update(updated)

    found = await repo.find_by_id(jogo.id)
    assert found.nome.value == "FIFA 25"


@pytest.mark.asyncio
async def test_delete():
    repo = MockJogoRepository()
    jogo1 = create_jogo(id="1")
    jogo2 = create_jogo(id="2")

    await repo.save(jogo1)
    await repo.save(jogo2)

    await repo.delete(jogo1.id)

    assert await repo.find_by_id(jogo1.id) is None
    assert await repo.find_by_id(jogo2.id) is not None
