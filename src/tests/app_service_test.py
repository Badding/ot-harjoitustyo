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
        result = ur.get_user_stats(1, 0)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 0)
        self.assertEqual(result[4], 0)
        self.assertEqual(result[5], '0;0;0;0;0;0;0;0;0;0')

    def test_get_user_by_id(self):
        result = ur.get_user_by_id(1)
        self.assertEqual(result[1], "testuser")


class TestGameAppService(unittest.TestCase):
    def setUp(self):
        init_db()
        self._app_service = app_service
        self._app_service.create_user("testuser", "1234")

    def test_save_stats(self):
        self._app_service.logout()
        self._app_service.login("testuser", "1234")
        self._app_service.new_game()
        self._app_service.set_game_mode(0)
        for i in range(5):
            for j in range(4):
                self._app_service.place_card(i, j)

        self._app_service.save_stats()
        result = ur.get_user_stats(1, 0)
        self.assertNotEqual(result[5], "0;0;0;0;0;0;0;0;0;0")

    def test_save_stats_quickgame(self):
        self._app_service.new_game()
        self._app_service.logout()
        self._app_service.save_stats()
        self.assertIsNone(self._app_service.get_user())

    def test_get_game_mode_name(self):
        self._app_service.new_game()
        self._app_service.set_game_mode(1)
        result = self._app_service.get_game_mode_name()
        self.assertEqual(result, "Place cards anywhere")

    def test_is_game_over_false(self):
        self._app_service.new_game()
        self.assertFalse(self._app_service.is_game_over())

    def test_is_game_over_true(self):
        self._app_service.new_game()
        for i in range(5):
            for j in range(5):
                self._app_service.place_card(i, j)
        self.assertTrue(self._app_service.is_game_over())

    def get_game_mode(self):
        self._app_service.new_game()
        self._app_service.set_game_mode(1)
        result = self._app_service.get_game_mode()
        self.assertEqual(result, 1)

    def test_hand_name(self):
        self.assertEqual(self._app_service.get_hand_name(0), "No Hand")
        self.assertEqual(self._app_service.get_hand_name(1), "One Pair")
        self.assertEqual(self._app_service.get_hand_name(2), "Two Pairs")
        self.assertEqual(self._app_service.get_hand_name(3), "Three of a Kind")
        self.assertEqual(self._app_service.get_hand_name(4), "Straight")
        self.assertEqual(self._app_service.get_hand_name(5), "Flush")
        self.assertEqual(self._app_service.get_hand_name(6), "Full House")
        self.assertEqual(self._app_service.get_hand_name(7), "Four of a Kind")
        self.assertEqual(self._app_service.get_hand_name(8), "Straight Flush")
        self.assertEqual(self._app_service.get_hand_name(9), "Royal Flush")