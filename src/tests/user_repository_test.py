import unittest
from repositories.user_repository import user_repository as ur
from db_init import init_db


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        init_db()
        self._user_a = ('molli', '1234')
        self._user_b = ('olli', '4321')

    def test_get_none_existing_user(self):
        result = ur.get_user(self._user_a[0])
        self.assertIsNone(result)

    def test_get_existing_user(self):
        ur.add_user(self._user_a[0], self._user_a[1])
        result = ur.get_user(self._user_a[0])
        self.assertEqual(result[0], self._user_a[0])

    def test_get_all_users(self):
        ur.add_user(self._user_a[0], self._user_a[1])
        ur.add_user(self._user_b[0], self._user_b[1])
        result = ur.get_all_users()
        self.assertEqual(len(result), 2)

    def test_get_id(self):
        ur.add_user(self._user_a[0], self._user_a[1])
        result = ur.get_id(self._user_a[0])
        self.assertEqual(result[0], 1)

    def test_check_password(self):
        ur.add_user(self._user_a[0], self._user_a[1])
        result = ur.check_password(self._user_a[0], self._user_a[1])
        self.assertTrue(result)

    def test_check_password_wrong_password(self):
        ur.add_user(self._user_a[0], self._user_a[1])
        result = ur.check_password(self._user_a[0], self._user_b[1])
        self.assertFalse(result)

    def test_check_password_none_existing_user(self):
        result = ur.check_password("nouser", self._user_a[1])
        self.assertFalse(result)
