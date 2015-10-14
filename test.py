from unittest import TestCase
import json


class IntegrationTest(TestCase):

    def setUp(self):
        self.data = json.load(open('data.json', 'r'))

    def test_data_type(self):
        self.assertIsInstance(self.data, dict)

    def test_data_true(self):
        self.assertTrue(self.data)
