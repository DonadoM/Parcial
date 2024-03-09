# Importa las clases FastAPI y HTTPException de FastAPI, y la clase BaseModel de Pydantic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Define un modelo de datos llamado UserModel utilizando la clase BaseModel de Pydantic
class UserModel(BaseModel):
    user_id: int
    username: str
    name: str
    email: str

# Define un endpoint para obtener información de usuario utilizando el método HTTP GET
@app.get("/user_info")
def get_user_info():
    # Datos simulados de un usuario
    user_data = {"user_id": 1, "username": "donadoM", "name": "Mauricio Donado", "email": "donadom@utb.edu.co"}
    # Crea una instancia de UserModel a partir de los datos simulados
    user = UserModel(**user_data)
    # Devuelve los datos del usuario en formato de diccionario
    return user.dict()

# Define un modelo de datos llamado BenefitModel utilizando la clase BaseModel de Pydantic
class BenefitModel(BaseModel):
    benefit_id: int
    name: str
    type: str

# Define un endpoint para obtener información sobre beneficios utilizando el método HTTP GET
@app.get("/benefit_info")
def get_benefit_info():
    # Datos simulados de un beneficio
    benefit_data = {"benefit_id": 1, "name": "Discount on purchases", "type": "Discount"}
    # Crea una instancia de BenefitModel a partir de los datos simulados
    benefit = BenefitModel(**benefit_data)
    # Devuelve los datos del beneficio en formato de diccionario
    return benefit.dict()
