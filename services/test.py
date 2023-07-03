import unittest
import json
from app import app

class PhoneNumberLookupTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_phone_number_with_country_code(self):
        response = self.app.get('/v1/phone-numbers?phoneNumber=%2B12125690123')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['phoneNumber'], '+12125690123')
        self.assertEqual(data['countryCode'], 'US')
        self.assertEqual(data['areaCode'], '212')
        self.assertEqual(data['localPhoneNumber'], '5690123')

    def test_valid_phone_number_with_spaces(self):
        response = self.app.get('/v1/phone-numbers?phoneNumber=%2B52%20631%203118150')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['phoneNumber'], '+526313118150')
        self.assertEqual(data['countryCode'], 'MX')
        self.assertEqual(data['areaCode'], '631')
        self.assertEqual(data['localPhoneNumber'], '3118150')

    def test_valid_phone_number_without_plus_and_spaces(self):
        response = self.app.get('/v1/phone-numbers?phoneNumber=%2B34%20915%20872200')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['phoneNumber'], '+34915872200')
        self.assertEqual(data['countryCode'], 'ES')
        self.assertEqual(data['areaCode'], '915')
        self.assertEqual(data['localPhoneNumber'], '872200')

    def test_invalid_phone_number(self):
        response = self.app.get('/v1/phone-numbers?phoneNumber=%2B351%2021%20094%20%20%202000')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['phoneNumber'], '+351 21 094   2000')
        self.assertEqual(data['error']['message'], 'Invalid phone number format')

if __name__ == '__main__':
    unittest.main()
