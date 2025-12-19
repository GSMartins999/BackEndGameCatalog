import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    response = await client.post(
        "/api/users",
        json={
            "email": "new@example.com",
            "password": "Password123!",
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["email"] == "new@example.com"


@pytest.mark.asyncio
async def test_login_user(client: AsyncClient):
    await client.post(
        "/api/users",
        json={
            "email": "login@example.com",
            "password": "Password123!",
        },
    )

    response = await client.post(
        "/api/token",
        data={
            "username": "login@example.com",
            "password": "Password123!",
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert data["token_type"] == "bearer"
    assert "access_token" in data


@pytest.mark.asyncio
async def test_get_me(client: AsyncClient, auth_headers):
    response = await client.get("/api/me", headers=auth_headers)

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert "email" in data
