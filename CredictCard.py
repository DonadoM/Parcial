import datetime
import unittest

class CredictCard:
    def __init__(self, cvv, expiry_year, expiry_month, number, zip_code, expety_date):
        # Inicializa los atributos de la tarjeta de crédito con los valores proporcionados
        self.cvv = cvv
        self.expiry_year = expiry_year
        self.expiry_month = expiry_month
        self.number = number
        self.zip_code = zip_code
        self.expety_date = expety_date

    # Métodos de acceso y modificación para cada atributo
    def get_cvv(self):
        return self.cvv

    def set_cvv(self, cvv):
        self.cvv = cvv

    def get_expiry_year(self):
        return self.expiry_year

    def set_expiry_year(self, expiry_year):
        self.expiry_year = expiry_year

    def get_expiry_month(self):
        return self.expiry_month

    def set_expiry_month(self, expiry_month):
        self.expiry_month = expiry_month

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_zip_code(self):
        return self.zip_code

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def get_expety_date(self):
        return self.expety_date

    def set_expety_date(self, expety_date):
        self.expety_date = expety_date

    # Método para representar la tarjeta de crédito como una cadena de texto
    def __str__(self):
        return f"CredictCard(cvv={self.cvv}, expiry_year={self.expiry_year}, expiry_month={self.expiry_month}, number={self.number}, zip_code={self.zip_code}, expety_date={self.expety_date})"

    # Método de validación (aún no implementado)
    def validation(self):
        pass

# Crear una instancia de la clase CredictCard con valores de ejemplo
card = CredictCard(cvv=123, expiry_year=2024, expiry_month=12, number=1234567890123456, zip_code=12345,
                   expety_date=datetime.date(2024, 12, 31))

# Imprimir la representación de la tarjeta de crédito como una cadena de texto
print(card)
