from random import shuffle
from entities.card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = list(range(1, 5))
        ranks = list(range(2, 15))
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def get_top_card(self):
        return self.cards[-1]

    def __len__(self):
        return len(self.cards)
