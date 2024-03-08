import unittest
import datetime

from CredictCard import CredictCard


class TestCreditCard(unittest.TestCase):
    def setUp(self):
        self.card = CredictCard(cvv=123, expiry_year=2024, expiry_month=12,
                                number=1234567890123456, zip_code=12345,
                                expety_date=datetime.date(2024, 12, 31))

    def test_getters_and_setters(self):
        self.assertEqual(self.card.get_cvv(), 123)
        self.card.set_cvv(456)
        self.assertEqual(self.card.get_cvv(), 456)

        self.assertEqual(self.card.get_expiry_year(), 2024)
        self.card.set_expiry_year(2025)
        self.assertEqual(self.card.get_expiry_year(), 2025)

        self.assertEqual(self.card.get_expiry_month(), 12)
        self.card.set_expiry_month(6)
        self.assertEqual(self.card.get_expiry_month(), 6)

        self.assertEqual(self.card.get_number(), 1234567890123456)
        self.card.set_number(9876543210987654)
        self.assertEqual(self.card.get_number(), 9876543210987654)

        self.assertEqual(self.card.get_zip_code(), 12345)
        self.card.set_zip_code(54321)
        self.assertEqual(self.card.get_zip_code(), 54321)

        self.assertEqual(self.card.get_expety_date(), datetime.date(2024, 12, 31))
        new_expiry_date = datetime.date(2025, 6, 30)
        self.card.set_expety_date(new_expiry_date)
        self.assertEqual(self.card.get_expety_date(), new_expiry_date)

    def test_str_representation(self):
        expected_str = "CredictCard(cvv=123, expiry_year=2024, expiry_month=12, " \
                       "number=1234567890123456, zip_code=12345, expety_date=2024-12-31)"
        self.assertEqual(str(self.card), expected_str)

    def test_validation(self):
        # Implement your validation tests here
        pass

if __name__ == '__main__':
    unittest.main()
