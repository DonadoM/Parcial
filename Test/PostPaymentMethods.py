from fastapi.testclient import TestClient
from PaymentMethods import PaymentMethodsTypes, app

client = TestClient(app)


def test_process_payment_credit():
    response = client.post("/process_payment/CREDIT")
    assert response.status_code == 200
    assert response.json() == {"message": "Pago con tarjeta de crédito procesado exitosamente"}


def test_process_payment_debit():
    response = client.post("/process_payment/DEBIT")
    assert response.status_code == 200
    assert response.json() == {"message": "Pago con tarjeta de débito procesado exitosamente"}


def test_process_payment_transfer():
    response = client.post("/process_payment/TRANSFER")
    assert response.status_code == 200
    assert response.json() == {"message": "Pago por transferencia procesado exitosamente"}


def test_process_payment_cash():
    response = client.post("/process_payment/CASH")
    assert response.status_code == 200
    assert response.json() == {"message": "Pago en efectivo procesado exitosamente"}

