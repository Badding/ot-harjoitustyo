from random import shuffle
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = [n for n in range(1, 5)]
        ranks = [n for n in range(2, 15)]
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle_deck(self):       
        shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)