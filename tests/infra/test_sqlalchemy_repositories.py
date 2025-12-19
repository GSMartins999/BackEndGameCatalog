import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from core.domain.entities.user import User
from core.domain.entities.jogo import Jogo
from core.domain.value_objects import (
    Email,
    Password,
    NomeDoJogo,
    Descricao,
    URL,
    DataLancamento,
)
from core.infra.sqlalchemy.user_repository import UserRepository
from core.infra.sqlalchemy.jogo_repository import JogoRepository


@pytest.mark.asyncio
async def test_user_repository_save(db_session: AsyncSession):
    repository = UserRepository(db_session)
    
    user = User(
        id="test-id",
        email=Email("test@example.com"),
        password=Password("SecurePass123!"),
    )
    
    await repository.save(user)
    
    found = await repository.find_by_id("test-id")
    assert found is not None
    assert found.email.value == "test@example.com"


@pytest.mark.asyncio
async def test_user_repository_find_by_email(db_session: AsyncSession):
    repository = UserRepository(db_session)
    
    user = User(
        id="test-id-2",
        email=Email("findme@example.com"),
        password=Password("SecurePass123!"),
    )
    
    await repository.save(user)
    
    found = await repository.find_by_email("findme@example.com")
    assert found is not None
    assert found.email.value == "findme@example.com"


@pytest.mark.asyncio
async def test_user_repository_find_by_email_not_found(db_session: AsyncSession):
    repository = UserRepository(db_session)
    
    found = await repository.find_by_email("nonexistent@example.com")
    assert found is None


@pytest.mark.asyncio
async def test_user_repository_update(db_session: AsyncSession):
    repository = UserRepository(db_session)
    
    user = User(
        id="test-id-3",
        email=Email("original@example.com"),
        password=Password("SecurePass123!"),
    )
    
    await repository.save(user)
    
    updated_user = User(
        id="test-id-3",
        email=Email("updated@example.com"),
        password=Password("NewPass123!"),
    )
    
    await repository.update(updated_user)
    
    found = await repository.find_by_id("test-id-3")
    assert found is not None
    assert found.email.value == "updated@example.com"


@pytest.mark.asyncio
async def test_user_repository_delete(db_session: AsyncSession):
    repository = UserRepository(db_session)
    
    user = User(
        id="test-id-4",
        email=Email("delete@example.com"),
        password=Password("SecurePass123!"),
    )
    
    await repository.save(user)
    await repository.delete("test-id-4")
    
    found = await repository.find_by_id("test-id-4")
    assert found is None


@pytest.mark.asyncio
async def test_jogo_repository_save(db_session: AsyncSession):
    repository = JogoRepository(db_session)
    
    jogo = Jogo(
        id_jogo=1,
        nome_do_jogo=NomeDoJogo("Test Game"),
        descricao=Descricao("This is a test game description"),
        url=URL("https://example.com/game"),
        data_lancamento=DataLancamento("2020-01-01"),
    )
    
    await repository.save(jogo)
    
    found = await repository.find_by_id(1)
    assert found is not None
    assert found.nome_do_jogo.value == "Test Game"


@pytest.mark.asyncio
async def test_jogo_repository_find_by_id_not_found(db_session: AsyncSession):
    repository = JogoRepository(db_session)
    
    found = await repository.find_by_id(9999)
    assert found is None


@pytest.mark.asyncio
async def test_jogo_repository_find_all(db_session: AsyncSession):
    repository = JogoRepository(db_session)
    
    jogo1 = Jogo(
        id_jogo=2,
        nome_do_jogo=NomeDoJogo("Game One"),
        descricao=Descricao("First game description"),
        url=URL("https://example.com/game1"),
        data_lancamento=DataLancamento("2020-01-01"),
    )
    
    jogo2 = Jogo(
        id_jogo=3,
        nome_do_jogo=NomeDoJogo("Game Two"),
        descricao=Descricao("Second game description"),
        url=URL("https://example.com/game2"),
        data_lancamento=DataLancamento("2021-01-01"),
    )
    
    await repository.save(jogo1)
    await repository.save(jogo2)
    
    all_jogos = await repository.find_all()
    assert len(all_jogos) >= 2


@pytest.mark.asyncio
async def test_jogo_repository_update(db_session: AsyncSession):
    repository = JogoRepository(db_session)
    
    jogo = Jogo(
        id_jogo=4,
        nome_do_jogo=NomeDoJogo("Original Name"),
        descricao=Descricao("Original description here"),
        url=URL("https://example.com/original"),
        data_lancamento=DataLancamento("2020-01-01"),
    )
    
    await repository.save(jogo)
    
    updated_jogo = Jogo(
        id_jogo=4,
        nome_do_jogo=NomeDoJogo("Updated Name"),
        descricao=Descricao("Updated description text"),
        url=URL("https://example.com/updated"),
        data_lancamento=DataLancamento("2021-01-01"),
    )
    
    await repository.update(updated_jogo)
    
    found = await repository.find_by_id(4)
    assert found is not None
    assert found.nome_do_jogo.value == "Updated Name"


@pytest.mark.asyncio
async def test_jogo_repository_delete(db_session: AsyncSession):
    repository = JogoRepository(db_session)
    
    jogo = Jogo(
        id_jogo=5,
        nome_do_jogo=NomeDoJogo("Delete Me"),
        descricao=Descricao("This will be deleted soon"),
        url=URL("https://example.com/delete"),
        data_lancamento=DataLancamento("2020-01-01"),
    )
    
    await repository.save(jogo)
    await repository.delete(5)
    
    found = await repository.find_by_id(5)
    assert found is None
