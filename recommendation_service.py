# recommendation_service.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from auth_service_py import get_current_user

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_recommended_products(user_id: int = Depends(get_current_user), limit: int = 5):
    # Lógica para generar recomendaciones basadas en preferencias del usuario
    # Aquí puedes usar algoritmos de recomendación, consultar una base de datos, etc.
    recommended_products = [
        {"id": 1, "name": "Product A"},
        {"id": 2, "name": "Product B"},
        {"id": 3, "name": "Product C"},
        {"id": 4, "name": "Product D"},
        {"id": 5, "name": "Product E"},
    ][:limit]

    return recommended_products


@app.get("/recommendations", response_model=list)
async def get_recommendations(
    limit: int = 5, user_id: int = Depends(get_current_user, use_cache=True)
):
    return get_recommended_products(user_id=user_id, limit=limit)
