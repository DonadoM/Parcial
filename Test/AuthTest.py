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
    # Configura el cliente HTTP para realizar solicitudes a la aplicación
    return AsyncClient(app=app, base_url="http://test")


async def test_login_and_get_user_info(client):
    # Realiza una solicitud de login
    login_data = {"username": "user", "password": "password"}
    response = await client.post("/token", data=login_data)

    # Asegúrate de que la solicitud sea exitosa
    assert response.status_code == 200

    # Obtiene el token del cuerpo de la respuesta
    token = response.json()["access_token"]

    # Realiza una solicitud a la ruta protegida "/user_info" con el token
    response = await client.get("/user_info", headers={"Authorization": f"Bearer {token}"})

    # Asegúrate de que la solicitud sea exitosa
    assert response.status_code == 200

    # Verifica que la información del usuario sea correcta
    assert response.json() == {"username": "user", "email": "user@example.com"}


async def test_invalid_credentials(client):
    # Intenta realizar una solicitud de login con credenciales incorrectas
    login_data = {"username": "invalid_user", "password": "invalid_password"}
    response = await client.post("/token", data=login_data)

    # Asegúrate de que la solicitud devuelva un código de estado 401
    assert response.status_code == 401


async def test_invalid_token(client):
    # Intenta realizar una solicitud a "/user_info" con un token inválido
    response = await client.get("/user_info", headers={"Authorization": "Bearer invalid_token"})

    # Asegúrate de que la solicitud devuelva un código de estado 401
    assert response.status_code == 401


if __name__ == "__main__":
    # Ejecuta los tests con pytest
    pytest.main()
