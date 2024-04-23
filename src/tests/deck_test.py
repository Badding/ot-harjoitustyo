import unittest
from entities.deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_len_correct(self):
        self.assertEqual(len(self.deck), 52)

    def test_deal_card(self):
        card = self.deck.deal_card()
        self.assertEqual(len(self.deck), 51)

    def tert_deal_from_top(self):
        top = self.cards[-1]
        self.assertEqual(self.deck.deal_card, top)

    def test_shuffle_deck(self):
        order_before = self.deck.cards.copy()
        self.deck.shuffle_deck()

        self.assertNotEqual(order_before, self.deck.cards)

    def test_all_cards_in_deck(self):
        card = 2
        suit = 1
        for i in range(52):
            self.assertEqual(self.deck.cards[i].get_rank(), card)
            self.assertEqual(self.deck.cards[i].get_suit(), suit)

            card += 1
            if card == 15:
                card = 2
                suit += 1
