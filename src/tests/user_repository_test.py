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
        self.assertEqual(result[1], self._user_a[0])

    def test_get_all_users(self):
        ur.add_user(self._user_a[0], self._user_a[1])
        ur.add_user(self._user_b[0], self._user_b[1])
        result = ur.get_all_users()
        self.assertEqual(len(result), 2)

    def test_get_id(self):
        ur.add_user(self._user_a[0], self._user_a[1])
        result = ur.get_id(self._user_a[0])
        self.assertEqual(result[0], 1)

    def test_get_id_none_existing_user(self):
        result = ur.get_id("nouser")
        self.assertIsNone(result)

    def test_get_user_by_id(self):
        ur.add_user("testuser", "1234")
        user_id = ur.get_id("testuser")[0]
        result = ur.get_user_by_id(user_id)
        self.assertEqual(result[1], "testuser")

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

    def test_init_new_user_stat(self):
        ur.add_user("testuser", "1234")
        user_id = ur.get_id("testuser")[0]
        ur.init_new_user_stat(user_id)
        user_stats = ur.get_user_stats(user_id)
        self.assertEqual(user_stats[4], "0;0;0;0;0;0;0;0;0;0")

    def test_user_hands_made(self):
        ur.add_user("testuser", "1234")
        user_id = ur.get_id("testuser")[0]
        ur.init_new_user_stat(user_id)
        ur.update_hands_made(user_id, "0;1;2;3;4;5;6;7;8;9")
        user_stats = ur.get_user_stats(user_id)
        self.assertEqual(user_stats[4], "0;1;2;3;4;5;6;7;8;9")

    def test_get_top_scores(self):
        ur.add_user("testuser", "1234")
        ur.add_user("testuser2", "1234")
        user_id = ur.get_id("testuser")[0]
        user_id2 = ur.get_id("testuser2")[0]
        ur.init_new_user_stat(user_id)
        ur.init_new_user_stat(user_id2)
        ur.update_top_score(user_id, 10)
        ur.update_top_score(user_id2, 20)
        result = ur.get_top_scores()
        self.assertEqual(result[0][1], 20)
        self.assertEqual(result[1][1], 10)

    def test_update_games_played(self):
        ur.add_user("testuser", "1234")
        user_id = ur.get_id("testuser")[0]
        ur.init_new_user_stat(user_id)
        ur.update_games_played(user_id, 1)
        user_stats = ur.get_user_stats(user_id)
        self.assertEqual(user_stats[3], 1)
