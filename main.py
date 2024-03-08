from auth_service_py import auth_app, get_current_user

from datetime import date

from fastapi import FastAPI, Depends, HTTPException
from recommendation_service import app as recommendation_app


from PaymentMethods import PaymentMethodsTypes
from Person import UserModel, BenefitModel

app = FastAPI()


@app.get("/user_info")
def get_user_info():
    user_data = {"user_id": 1, "username": "donadoM", "name": "Mauricio Donado",
                 "email": "donadom@utb.edu.co"}
    user = UserModel(**user_data)
    return user.dict()


class CredictCard:
    def __init__(self, cvv, expiry_year, expiry_month, number, zip_code, expety_date):
        self.cvv = cvv
        self.expiry_year = expiry_year
        self.expiry_month = expiry_month
        self.number = number
        self.zip_code = zip_code
        self.expety_date = expety_date

    def __str__(self):
        return (f'CredictCard(cvv={self.cvv}, expiry_year={self.expiry_year}, expiry_month={self.expiry_month}, '
                f'number={self.number}, zip_code={self.zip_code}, expety_date={self.expety_date})')


card = CredictCard(cvv=123, expiry_year=2024, expiry_month=12, number=1234567890123456, zip_code=12345,
                   expety_date=date(2024, 12, 31))


@app.get("/credit_card_info")
async def get_credit_card_info():
    return card.__dict__


@app.get("/benefit_info")
def get_benefit_info():
    benefit_data = {"benefit_id": 1, "name": "Discount on purchases", "type": "Discount"}
    benefit = BenefitModel(**benefit_data)
    return benefit.dict()


@app.post("/process_payment/{payment_method}")
async def process_payment(payment_method: PaymentMethodsTypes):
    if payment_method == PaymentMethodsTypes.CREDIT:
        # Lógica para procesar el pago con tarjeta de crédito
        return {"message": "Pago con tarjeta de crédito procesado exitosamente"}
    elif payment_method == PaymentMethodsTypes.DEBIT:
        # Lógica para procesar el pago con tarjeta de débito
        return {"message": "Pago con tarjeta de débito procesado exitosamente"}
    elif payment_method == PaymentMethodsTypes.TRANSFER:
        # Lógica para procesar el pago por transferencia
        return {"message": "Pago por transferencia procesado exitosamente"}
    elif payment_method == PaymentMethodsTypes.CASH:
        # Lógica para procesar el pago en efectivo
        return {"message": "Pago en efectivo procesado exitosamente"}
    else:
        # En caso de que se proporcione un método de pago no válido
        raise HTTPException(status_code=400, detail="Método de pago no válido")


app.mount("/auth", auth_app)
app.mount("/recommendation", recommendation_app)

@app.get("/protected")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}! This route is protected."}



def SECRET_KEY():
    return None

def ALGORITHM():
    return None
