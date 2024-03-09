# recommendation_service.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from auth_service_py import get_current_user

# Crea una instancia de la aplicación FastAPI para el servicio de recomendación
app = FastAPI()

# Esquema OAuth2 para manejar tokens de contraseña
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función para obtener productos recomendados para un usuario
def get_recommended_products(user_id: int = Depends(get_current_user), limit: int = 5):
    # Lista simulada de productos recomendados (limitada por el parámetro 'limit')
    recommended_products = [
        {"id": 1, "name": "Product A"},
        {"id": 2, "name": "Product B"},
        {"id": 3, "name": "Product C"},
        {"id": 4, "name": "Product D"},
        {"id": 5, "name": "Product E"},
    ][:limit]

    return recommended_products

# Ruta para obtener recomendaciones
@app.get("/recommendations", response_model=list)
async def get_recommendations(
    limit: int = 5, user_id: int = Depends(get_current_user, use_cache=True)
):
    # Llama a la función que obtiene los productos recomendados
    return get_recommended_products(user_id=user_id, limit=limit)
