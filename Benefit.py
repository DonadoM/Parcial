# Importa las clases necesarias de Pydantic y FastAPI
from pydantic import BaseModel
from fastapi import FastAPI

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Define un modelo de datos utilizando la clase BaseModel de Pydantic
class BenefitModel(BaseModel):
    benefit_id: int
    name: str
    type: str

# Define un endpoint para obtener información sobre beneficios
# Utiliza el decorador @app.get para indicar que responde a solicitudes HTTP GET
# response_model=BenefitModel especifica el modelo de datos de la respuesta
# summary proporciona una descripción breve de la funcionalidad del endpoint
@app.get("/benefit_info", response_model=BenefitModel, summary="Get information about a benefit")
def get_benefit_info():
    # Datos simulados de un beneficio
    benefit_data = {"benefit_id": 1, "name": "Discount on purchases", "type": "Discount"}
    
    # Crea una instancia de BenefitModel a partir de los datos simulados y la devuelve
    return BenefitModel(**benefit_data)
