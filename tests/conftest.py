import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.pool import StaticPool

from api.database import get_db
from core.infra.orm.base import Base
from api.main import app

# URL do banco de testes
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

# 1. FIXTURE DA ENGINE (Scope = Session)
# Cria a engine uma vez para todos os testes e garante o fechamento no final via dispose()
@pytest_asyncio.fixture(scope="session")
async def db_engine():
    engine = create_async_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    
    yield engine
    
    # ESTA É A LINHA MÁGICA QUE EVITA O TRAVAMENTO NO GITHUB ACTIONS
    await engine.dispose()

# 2. FIXTURE DA SESSÃO (Scope = Function)
# Cria as tabelas antes de cada teste e apaga depois
@pytest_asyncio.fixture(scope="function")
async def db_session(db_engine):
    # Cria as tabelas no banco em memória
    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Cria a fábrica de sessões usando a engine da fixture
    SessionLocal = async_sessionmaker(
        bind=db_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
        autocommit=False
    )

    async with SessionLocal() as session:
        yield session

    # Limpa as tabelas após o teste
    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# 3. FIXTURE DO CLIENT
@pytest_asyncio.fixture(scope="function")
async def client(db_session):
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()

# 4. FIXTURE DE TOKEN (Usuário Helper)
@pytest_asyncio.fixture(scope="function")
async def token(client):
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "Password123!",
    }
    # Cria usuário
    await client.post("/api/users", json=user_data)

    # Faz login
    response = await client.post(
        "/api/token",
        data={"username": user_data["email"], "password": user_data["password"]},
    )
    return response.json()["access_token"]

@pytest_asyncio.fixture(scope="function")
async def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}
