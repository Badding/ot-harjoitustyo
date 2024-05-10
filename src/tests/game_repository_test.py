import unittest
from repositories.game_repository import Game
import entities.card as card


class TestPokerSquares(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    # game setup tests
    def test_each_row_has_one_card(self):
        self.game.new_game()
        board = self.game.get_board()
        one_card_in_each_row = True

        for i in range(5):
            if board[i][0] is None:
                one_card_in_each_row = False
            if type(board[i][0]) != card.Card:
                one_card_in_each_row = False
            if board[i].count(None) != 4:
                one_card_in_each_row = False

        self.assertTrue(one_card_in_each_row)

    # game play tests
    def test_place_card_full_row(self):
        self.game.new_game()
        for i in range(5):
            self.game.place_card(0)
        self.assertFalse(self.game.place_card(0))

    def test_is_game_over_false(self):
        self.game.new_game()
        self.assertFalse(self.game.is_game_over())

    def test_is_game_over_not_started(self):
        self.assertTrue(self.game.is_game_over())

    def test_is_game_over_true(self):
        self.game.new_game()
        for i in range(5):
            for j in range(5):
                self.game.place_card(i)
        self.assertTrue(self.game.is_game_over())

    # straight checks tests
    def test_check_for_straight(self):
        row = [card.Card(2, 1), card.Card(4, 2), card.Card(
            6, 3), card.Card(5, 4), card.Card(3, 1)]
        self.assertTrue(self.game.check_for_straight(row))

    def test_check_for_straight_end_from_ace(self):
        row = [card.Card(14, 1), card.Card(13, 2), card.Card(
            12, 3), card.Card(11, 4), card.Card(10, 1)]
        self.assertTrue(self.game.check_for_straight(row))

    def test_check_for_straight_start_from_ace(self):
        row = [card.Card(14, 1), card.Card(3, 2), card.Card(
            5, 4), card.Card(2, 3), card.Card(4, 1)]
        self.assertTrue(self.game.check_for_straight(row))

    def test_check_for_straight_false(self):
        row = [card.Card(2, 1), card.Card(4, 2), card.Card(
            6, 3), card.Card(5, 4), card.Card(7, 1)]
        self.assertFalse(self.game.check_for_straight(row))

    # row checks tests

    def test_check_row_nothing(self):
        row = [card.Card(2, 1), card.Card(4, 2), card.Card(
            6, 3), card.Card(5, 4), card.Card(7, 1)]
        self.assertEqual(self.game._check_row(row), 0)

    def test_check_row_none_in_row(self):
        row = [card.Card(2, 1), card.Card(
            4, 2), card.Card(6, 3), card.Card(5, 4), None]
        self.assertEqual(self.game._check_row(row), 0)

    def test_check_row_pair(self):
        row = [card.Card(2, 1), card.Card(2, 2), card.Card(
            3, 3), card.Card(4, 4), card.Card(5, 1)]
        self.assertEqual(self.game._check_row(row), 1)

    def test_check_row_two_pair(self):
        row = [card.Card(2, 1), card.Card(2, 2), card.Card(
            3, 3), card.Card(3, 4), card.Card(5, 1)]
        self.assertEqual(self.game._check_row(row), 2)

    def test_check_row_three_of_a_kind(self):
        row = [card.Card(2, 1), card.Card(2, 2), card.Card(
            2, 3), card.Card(3, 4), card.Card(5, 1)]
        self.assertEqual(self.game._check_row(row), 3)

    def test_check_row_straight(self):
        row = [card.Card(2, 1), card.Card(3, 2), card.Card(
            6, 1), card.Card(5, 4), card.Card(4, 3)]
        self.assertEqual(self.game._check_row(row), 4)

    def test_check_row_straight_start_from_ace(self):
        row = [card.Card(14, 1), card.Card(2, 2), card.Card(
            4, 4), card.Card(3, 3),  card.Card(5, 1)]
        self.assertEqual(self.game._check_row(row), 4)

    def test_check_row_straight_end_from_ace(self):
        row = [card.Card(10, 1), card.Card(14, 1), card.Card(
            13, 4), card.Card(12, 3), card.Card(11, 2)]
        self.assertEqual(self.game._check_row(row), 4)

    def test_check_row_flush(self):
        row = [card.Card(2, 1), card.Card(10, 1), card.Card(
            6, 1), card.Card(5, 1), card.Card(4, 1)]
        self.assertEqual(self.game._check_row(row), 5)

    def test_check_row_full_house(self):
        row = [card.Card(2, 1), card.Card(2, 2), card.Card(
            2, 3), card.Card(3, 4), card.Card(3, 1)]
        self.assertEqual(self.game._check_row(row), 6)

    def test_check_row_four_of_a_kind(self):
        row = [card.Card(2, 1), card.Card(2, 2), card.Card(
            2, 3), card.Card(2, 4), card.Card(5, 1)]
        self.assertEqual(self.game._check_row(row), 7)

    def test_check_row_straight_flush(self):
        row = [card.Card(2, 1), card.Card(3, 1), card.Card(
            4, 1), card.Card(5, 1), card.Card(6, 1)]
        self.assertEqual(self.game._check_row(row), 8)

    def test_check_row_royal_flush(self):
        row = [card.Card(10, 1), card.Card(11, 1), card.Card(
            12, 1), card.Card(13, 1), card.Card(14, 1)]
        self.assertEqual(self.game._check_row(row), 9)

    # score tests from poker hand
    def test_get_score_nothing(self):
        self.assertEqual(self.game.get_score(0), 0)

    def test_get_score_pair(self):
        self.assertEqual(self.game.get_score(1), 2)

    def test_get_score_two_pair(self):
        self.assertEqual(self.game.get_score(2), 5)

    def test_get_score_three_of_a_kind(self):
        self.assertEqual(self.game.get_score(3), 10)

    def test_get_score_straight(self):
        self.assertEqual(self.game.get_score(4), 15)

    def test_get_score_flush(self):
        self.assertEqual(self.game.get_score(5), 20)

    def test_get_score_full_house(self):
        self.assertEqual(self.game.get_score(6), 25)

    def test_get_score_four_of_a_kind(self):
        self.assertEqual(self.game.get_score(7), 50)

    def test_get_score_straight_flush(self):
        self.assertEqual(self.game.get_score(8), 75)

    def test_get_score_royal_flush(self):
        self.assertEqual(self.game.get_score(9), 100)

    # calculate score tests
    # refactor calculate_score so it can be tested

    # get tests
    def test_get_board(self):
        self.game.new_game()
        self.assertEqual(type(self.game.get_board()), list)

    # refactor for better tests, new game always deals first column, that can have a poker hand
    def test_get_score_rows(self):
        self.game.new_game()
        self.assertEqual(type(self.game.get_score_rows()), list)

    def test_get_delt_columns(self):
        self.game.new_game()
        self.assertEqual(type(self.game.get_score_columns()), list)

    def test_get_hand_name(self):
        self.assertEqual(self.game.get_hand_name(0), "No Hand")
        self.assertEqual(self.game.get_hand_name(1), "One Pair")
        self.assertEqual(self.game.get_hand_name(2), "Two Pairs")
        self.assertEqual(self.game.get_hand_name(3), "Three of a Kind")
        self.assertEqual(self.game.get_hand_name(4), "Straight")
        self.assertEqual(self.game.get_hand_name(5), "Flush")
        self.assertEqual(self.game.get_hand_name(6), "Full House")
        self.assertEqual(self.game.get_hand_name(7), "Four of a Kind")
        self.assertEqual(self.game.get_hand_name(8), "Straight Flush")
        self.assertEqual(self.game.get_hand_name(9), "Royal Flush")

    def test_get_delt_card(self):
        self.game.new_game()
        # no good way to test this, since it is random
        self.assertEqual(type(self.game.get_delt_card()), card.Card)

    def test_get_total_score(self):
        self.game.new_game()
        self.assertEqual(self.game.get_total_score(), 0)

    def test_get_hand_score(self):
        self.game.new_game()
        self.assertEqual(self.game.get_hand_score(0), 0)
        self.assertEqual(self.game.get_hand_score(1), 2)
        self.assertEqual(self.game.get_hand_score(2), 5)
        self.assertEqual(self.game.get_hand_score(3), 10)
        self.assertEqual(self.game.get_hand_score(4), 15)
        self.assertEqual(self.game.get_hand_score(5), 20)
        self.assertEqual(self.game.get_hand_score(6), 25)
        self.assertEqual(self.game.get_hand_score(7), 50)
        self.assertEqual(self.game.get_hand_score(8), 75)
        self.assertEqual(self.game.get_hand_score(9), 100)

    def test_get_best_hand_rows_newgame(self):
        self.game.new_game()
        self.assertEqual(self.game.get_best_hand_rows(), [0, 0, 0, 0, 0])

    def test_get_best_hand_columns_newgame(self):
        self.game.new_game()
        self.assertEqual(self.game.get_best_hand_columns(), [0, 0, 0, 0, 0])
