class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.suits = {1: 'Clubs', 2: 'Spades', 3: 'Hearts', 4: 'Diamonds'}
    def __str__(self):
        return str(self.rank) + str(self.suit)
    
    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, other):
        return self.rank < other.rank
    
    def get_card(self):
        return (self.rank, self.suit)

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit