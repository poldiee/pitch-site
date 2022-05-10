import unittest

from models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='nana',password='qwerty')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password is not None)