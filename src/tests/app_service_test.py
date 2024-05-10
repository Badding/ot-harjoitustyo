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
        self._app_service.create_user("testuser", "1234")

    def test_create_user(self):
        self._app_service.create_user(self._user_a[0], self._user_a[1])
        result = ur.get_user(self._user_a[0])
        self.assertEqual(result[1], self._user_a[0])

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

    def test_logout(self):
        self._app_service.create_user(self._user_a[0], self._user_a[1])
        self._app_service.login(self._user_a[0], self._user_a[1])
        self._app_service.logout()
        self.assertIsNone(self._app_service.get_user())

    def test_get_id(self):
        result = ur.get_id("testuser")
        self.assertEqual(result[0], 1)

    def test_get_user_stats(self):
        result = ur.get_user_stats(1)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 0)
        self.assertEqual(result[4], '0;0;0;0;0;0;0;0;0;0')

    def test_get_user_by_id(self):
        result = ur.get_user_by_id(1)
        self.assertEqual(result[1], "testuser")


class TestGameAppService(unittest.TestCase):
    def setUp(self):
        init_db()
        self._app_service = app_service
        self._app_service.create_user("testuser", "1234")

    def test_save_stats(self):
        self._app_service.login("testuser", "1234")
        self._app_service.new_game()
        for i in range(5):
            for j in range(4):
                self._app_service.place_card(i)

        self._app_service.save_stats()
        result = ur.get_user_stats(1)
        self.assertNotEqual(result[4], "0;0;0;0;0;0;0;0;0;0")
