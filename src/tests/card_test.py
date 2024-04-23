import unittest
from entities.card import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        pass

    def test_card_str(self):
        card = Card(5, 1)
        self.assertEqual(str(card), '51')

        card = Card(11, 2)
        self.assertEqual(str(card), '112')

        card = Card(14, 3)
        self.assertEqual(str(card), '143')

    def test_get_card(self):
        card = Card(5, 1)
        self.assertEqual(card.get_card(), (5, 1))

    def test_get_rank(self):
        card = Card(9, 4)
        self.assertEqual(card.get_rank(), 9)

    def test_get_suit(self):
        card = Card(9, 4)
        self.assertEqual(card.get_suit(), 4)

    def test_get_rank_symbol(self):
        card = Card(11, 2)
        self.assertEqual(card.get_rank_symbol(), 'J')

        card = Card(12, 3)
        self.assertEqual(card.get_rank_symbol(), 'Q')

        card = Card(13, 4)
        self.assertEqual(card.get_rank_symbol(), 'K')

        card = Card(14, 3)
        self.assertEqual(card.get_rank_symbol(), 'A')

        card = Card(5, 1)
        self.assertEqual(card.get_rank_symbol(), '5')

    def test_get_suit_symbol_club(self):
        card = Card(5, 1)
        self.assertEqual(card.get_suit_symbol(), '♣')

    def test_get_suit_symbol_spade(self):
        card = Card(5, 2)
        self.assertEqual(card.get_suit_symbol(), '♠')

    def test_get_suit_symbol_heart(self):
        card = Card(5, 3)
        self.assertEqual(card.get_suit_symbol(), '♥')

    def test_get_suit_symbol_diamond(self):
        card = Card(5, 4)
        self.assertEqual(card.get_suit_symbol(), '♦')

    def test_get_color_black(self):
        card = Card(5, 1)
        self.assertEqual(card.get_color(), 'black')

        card = Card(5, 2)
        self.assertEqual(card.get_color(), 'black')

    def test_get_color_red(self):
        card = Card(5, 3)
        self.assertEqual(card.get_color(), 'red')

        card = Card(5, 4)
        self.assertEqual(card.get_color(), 'red')

    def test_lt_smaller(self):
        card1 = Card(5, 1)
        card2 = Card(6, 1)
        self.assertTrue(card1 < card2)

    def test_lt_larger(self):
        card1 = Card(6, 1)
        card2 = Card(5, 1)
        self.assertFalse(card1 < card2)
