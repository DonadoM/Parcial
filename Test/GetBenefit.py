import unittest
from fastapi.testclient import TestClient
from Benefit import app, BenefitModel


class TestBenefitInfo(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_benefit_info(self):
        response = self.client.get("/benefit_info")
        self.assertEqual(response.status_code, 200)

        
        benefit_info = BenefitModel(**response.json())

        self.assertEqual(benefit_info.benefit_id, 1)
        self.assertEqual(benefit_info.name, "Discount on purchases")
        self.assertEqual(benefit_info.type, "Discount")


if __name__ == '__main__':
    unittest.main()
