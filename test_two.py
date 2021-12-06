

import requests
import unittest
from unittest.mock import patch

URL = "https://cloud-api.yandex.net/v1/disk/resources?path=RomarioMusic"
TOKEN = " "


def create_folder(href, TOK):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOK}'}
    response = requests.put(href, headers=headers)
    response.raise_for_status()
    return response.status_code


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass create user')

    def setUp(self):
        print('setUp')

    def test_check_create_folder(self):

        self.assertEqual(create_folder(URL, TOKEN), 201)

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass delete user")
    def tearDown(self):
        print('tearDown')

if __name__ == '__main__':
    unittest.main()