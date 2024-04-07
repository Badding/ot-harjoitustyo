class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.suit_symbols = {1: '♣', 2: '♠', 3: '♥', 4: '♦'} #class variable?
        self.rank_symbols = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        self.color = 'black' if self.suit < 3 else 'red'
        

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

    def get_rank_symbol(self):
        if self.rank in self.rank_symbols:
            return self.rank_symbols[self.rank]
        return str(self.rank)
    
    def get_suit_symbol(self):
        return self.suit_symbols[self.suit]
    
    def get_color(self):
        return self.color