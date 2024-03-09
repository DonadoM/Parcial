import pytest
from httpx import AsyncClient
from fastapi import FastAPI

from main import app, SECRET_KEY, ALGORITHM

def SECRET_KEY():
    return None

def ALGORITHM():
    return None

@pytest.fixture
def client():
 
    return AsyncClient(app=app, base_url="http://test")


async def test_login_and_get_user_info(client):
   
    login_data = {"username": "user", "password": "password"}
    response = await client.post("/token", data=login_data)

    assert response.status_code == 200

    
    token = response.json()["access_token"]

    
    response = await client.get("/user_info", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"username": "user", "email": "user@example.com"}
async def test_invalid_credentials(client):
    # Intenta realizar una solicitud de login con credenciales incorrectas
    login_data = {"username": "invalid_user", "password": "invalid_password"}
    response = await client.post("/token", data=login_data)

   
    assert response.status_code == 401
async def test_invalid_token(client):
    response = await client.get("/user_info", headers={"Authorization": "Bearer invalid_token"})
    assert response.status_code == 401

if __name__ == "__main__":
    pytest.main()
