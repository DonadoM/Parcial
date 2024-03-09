# Importa la clase Enum de la biblioteca enum y las clases FastAPI y HTTPException de FastAPI
from enum import Enum
from fastapi import FastAPI, HTTPException

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Define una enumeración llamada PaymentMethodsTypes que hereda de str y Enum
class PaymentMethodsTypes(str, Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    TRANSFER = "TRANSFER"
    CASH = "CASH"

# Define un endpoint para procesar pagos utilizando el método HTTP POST
# El parámetro path payment_method es validado con la enumeración PaymentMethodsTypes
@app.post("/process_payment/{payment_method}")
async def process_payment(payment_method: PaymentMethodsTypes):
    # Verifica el tipo de método de pago y responde en consecuencia
    if payment_method == PaymentMethodsTypes.CREDIT:
        return {"message": "Pago con tarjeta de crédito procesado exitosamente"}
    elif payment_method == PaymentMethodsTypes.DEBIT:
        return {"message": "Pago con tarjeta de débito procesado exitosamente"}
    elif payment_method == PaymentMethodsTypes.TRANSFER:
        return {"message": "Pago por transferencia procesado exitosamente"}
    elif payment_method == PaymentMethodsTypes.CASH:
        return {"message": "Pago en efectivo procesado exitosamente"}
    else:
        # Si el método de pago no es válido, devuelve un error HTTP 400
        raise HTTPException(status_code=400, detail="Método de pago no válido")
