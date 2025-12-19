import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_jogo(client: AsyncClient, auth_headers):
    response = await client.post(
        "/api/jogos",
        headers=auth_headers,
        json={
            "nome": "God of War",
            "descricao": "Jogo de ação",
            "url": "https://example.com/game",
            "data_lancamento": "2020-01-01",
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert data["nome"] == "God of War"
    assert data["descricao"] == "Jogo de ação"
    assert data["url"] == "https://example.com/game"
    assert data["data_lancamento"] == "2020-01-01"
    assert "id_jogo" in data


@pytest.mark.asyncio
async def test_list_jogos(client: AsyncClient):
    response = await client.get("/api/jogos")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_update_jogo(client: AsyncClient, auth_headers):
    create = await client.post(
        "/api/jogos",
        headers=auth_headers,
        json={
            "nome": "FIFA",
            "descricao": "Futebol simulação",
            "url": "https://example.com/fifa",
            "data_lancamento": "2019-01-01",
        },
    )

    jogo_id = create.json()["id_jogo"]

    response = await client.put(
        f"/api/jogos/{jogo_id}",
        headers=auth_headers,
        json={
            "nome": "FIFA 23",
            "descricao": "Futebol atualizado jogo",
            "url": "https://example.com/fifa23",
            "data_lancamento": "2023-01-01",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "FIFA 23"


@pytest.mark.asyncio
async def test_delete_jogo(client: AsyncClient, auth_headers):
    create = await client.post(
        "/api/jogos",
        headers=auth_headers,
        json={
            "nome": "Minecraft",
            "descricao": "Sandbox game mundo aberto",
            "url": "https://example.com/mc",
            "data_lancamento": "2011-01-01",
        },
    )

    jogo_id = create.json()["id_jogo"]

    response = await client.delete(
        f"/api/jogos/{jogo_id}", headers=auth_headers
    )

    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_jogo_inexistente(client: AsyncClient, auth_headers):
    response = await client.delete(
        "/api/jogos/nao-existe", headers=auth_headers
    )

    assert response.status_code == 422
