from enum import Enum
from fastapi import FastAPI, HTTPException

app = FastAPI()


class PaymentMethodsTypes(str, Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    TRANSFER = "TRANSFER"
    CASH = "CASH"


@app.post("/process_payment/{payment_method}")
async def process_payment(payment_method: PaymentMethodsTypes):
    if payment_method == PaymentMethodsTypes.CREDIT:

        return {"message": "Pago con tarjeta de crédito procesado exitosamente"}
    elif payment_method == PaymentMethodsTypes.DEBIT:
        return {"message": "Pago con tarjeta de débito procesado exitosamente"}
    elif payment_method == PaymentMethodsTypes.TRANSFER:
        return {"message": "Pago por transferencia procesado exitosamente"}
    elif payment_method == PaymentMethodsTypes.CASH:
        return {"message": "Pago en efectivo procesado exitosamente"}
    else:
        raise HTTPException(status_code=400, detail="Método de pago no válido")
