
import unittest
from unittest.mock import patch

from app import get_doc_owner_name, get_all_doc_owners_names, check_document_existance, get_doc_shelf, \
    add_new_shelf, add_new_doc, delete_doc


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass create user')

    def setUp(self):
        print('setUp')

    def test_check_document_existance(self):

        self.assertEqual(check_document_existance('11-2'), True)

    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_owner_name(self):

        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')

    def test_remove_get_all_doc_owners_names(self):

        self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Аристарх Павлов', 'Геннадий Покемонов'})

    @patch('builtins.input', lambda *args: '10006')
    def test_get_doc_shelf(self):

        self.assertEqual(get_doc_shelf(), '2')

    @patch('builtins.input', lambda *args: '3')
    def test_add_new_shelf(self):

        self.assertEqual(add_new_shelf(), ('3', False))

    @patch('builtins.input', side_effect=['1006', 'report', 'Jo', '3'])
    def test_add_new_doc(self, data):

        self.assertEqual(add_new_doc(), '3')

    @patch('builtins.input', lambda *args: '1006')
    def test_delete_doc(self):

        self.assertEqual(delete_doc(), ('1006', True))

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass delete user")
    def tearDown(self):
        print('tearDown')




if __name__ == '__main__':
    unittest.main()
