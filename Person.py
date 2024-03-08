from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class UserModel(BaseModel):
    user_id: int
    username: str
    name: str
    email: str


@app.get("/user_info")
def get_user_info():
    user_data = {"user_id": 1, "username": "donadoM", "name": "Mauricio Donado", "email": "donadom@utb.edu.co"}
    user = UserModel(**user_data)
    return user.dict()


class BenefitModel(BaseModel):
    benefit_id: int
    name: str
    type: str


@app.get("/benefit_info")
def get_benefit_info():
    benefit_data = {"benefit_id": 1, "name": "Discount on purchases", "type": "Discount"}
    benefit = BenefitModel(**benefit_data)
    return benefit.dict()
