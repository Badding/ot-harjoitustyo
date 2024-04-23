import unittest
from repositories.game_repository import Game
from repositories.user_repository import user_repository as ur
from services.app_service import app_service
from db_init import init_db


class TestUserAppService(unittest.TestCase):
    def setUp(self):
        init_db()
        self._user_a = ('molli', '1234')
        self._user_b = ('olli', '4321')
        self._app_service = app_service

    def test_create_user(self):
        self._app_service.create_user(self._user_a[0], self._user_a[1])
        result = ur.get_user(self._user_a[0])
        self.assertEqual(result[0], self._user_a[0])

    def test_create_user_already_exists(self):
        self._app_service.create_user(self._user_a[0], self._user_a[1])
        result = self._app_service.create_user(
            self._user_a[0], self._user_a[1])
        self.assertFalse(result)

    def test_login(self):
        self._app_service.create_user(self._user_a[0], self._user_a[1])
        result = self._app_service.login(self._user_a[0], self._user_a[1])
        self.assertTrue(result)

    def test_login_wrong_password(self):
        self._app_service.create_user(self._user_a[0], self._user_a[1])
        result = self._app_service.login(self._user_a[0], self._user_b[1])
        self.assertFalse(result)
