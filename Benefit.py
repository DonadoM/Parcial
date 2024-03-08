from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class BenefitModel(BaseModel):
    benefit_id: int
    name: str
    type: str


@app.get("/benefit_info", response_model=BenefitModel,
         summary="Get information about a benefit")
def get_benefit_info():
    benefit_data = {"benefit_id": 1, "name": "Discount on purchases", "type": "Discount"}
    return BenefitModel(**benefit_data)
