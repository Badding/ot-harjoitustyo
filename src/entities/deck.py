from random import shuffle
from entities.card import Card


class Deck:
    """A class to represent a deck of cards

    Attributes:
        cards (list): A list of Card objects
    """

    def __init__(self):
        """Constructor for the Deck class"""

        self.cards = []
        self.create_deck()

    def create_deck(self):
        """Create a deck of cards

        Creates a deck of 52 cards, one of each rank and suit
        """

        suits = list(range(1, 5))
        ranks = list(range(2, 15))
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        """Randomize the card deck order"""

        shuffle(self.cards)

    def deal_card(self):
        """Deal a card from the deck"""

        return self.cards.pop()

    def get_top_card(self):
        """Get the top card of the deck"""

        return self.cards[-1]

    def __len__(self):
        return len(self.cards)
