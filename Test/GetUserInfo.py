import unittest
from fastapi.testclient import TestClient
from main import app, UserModel  # Reemplaza 'your_main_module' con el nombre real de tu módulo principal


###
class TestYourFastAPIApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_user_info(self):
        response = self.client.get("/user_info")

        self.assertEqual(response.status_code, 200)

        expected_data = {"user_id": 1, "username": "donadoM", "name": "Mauricio Donado", "email": "donadom@utb.edu.co"}
        self.assertEqual(response.json(), expected_data)





###


if __name__ == '__main__':
    unittest.main()
