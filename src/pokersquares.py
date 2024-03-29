from deck import Deck

class Game:
    def __init__(self):
        pass

    def new_game(self):
        self.deck = Deck()
        self.deck.shuffle_deck()

        self.board = [[None for _ in range(5)] for _ in range(5)]
        self.scoreboard_rows = [0, 0, 0, 0, 0]
        self.scoreboard_columns = [0, 0, 0, 0, 0]
        self.best_hand_row = [0, 0, 0, 0, 0]
        self.best_hand_columns = [0, 0, 0, 0, 0]
        self.score = 0
        self.initialize_board()
        self.game_loop()

        self.poker_hands = {
            'No Hand': 0,
            'One Pair': 1,
            'Two Pair': 2,
            'Three of a Kind': 3,
            'Straight': 4,
            'Flush': 5,
            'Full House': 6,
            'Four of a Kind': 7,
            'Straight Flush': 8,
            'Royal Flush': 9
        }

    def game_loop(self):
        #self.print_board()
        #'''
        while len(self.deck) > 27: # refactor this
            self.calculate_score()
            self.print_score()
            self.print_board()
            self.play()
            self.score = 0

        self.calculate_score()
        self.print_board()
        print('Game over! Your score is:', self.score)
        #'''

    def initialize_board(self):
        for i in range(5):
            self.board[i][0] = self.deck.deal_card()
    
    def print_board(self):
        for row in self.board:
            for card in row:
                print(card, end=' ')
            print()    

    def print_score(self):
        print('rows:')
        print(self.scoreboard_rows)
        print('columns:')
        print(self.scoreboard_columns)
        print('Your best hand in each row:')
        print(self.best_hand_row)
        print('Your best hand in each column:')
        print(self.best_hand_columns)
        print('Your score is:', self.score)

    def play(self):
        card = self.deck.deal_card()

        print('You drew the', card, 'Place it in row 1-5')
        
        success = False
        while not success:
            row = int(input())
            success = self.place_card(card, row)
            if not success:
                print('Row', row, 'is full. Try again.')

    def place_card(self, card, row):
        if row >= 1 and row <= 5 and None in self.board[row - 1]:
            index = self.board[row - 1].index(None)
            self.board[row - 1][index] = card
            return True
        return False

    def calculate_score(self):       
        for i in range(5):
            column = [self.board[j][i] for j in range(5)]
            row = self.board[i]

            hand_from_row = self.check_row(row)
            hand_from_column = self.check_row(column)

            self.best_hand_row[i] = hand_from_row
            self.best_hand_columns[i] = hand_from_column

            row_score = self.get_score(hand_from_row)
            column_score = self.get_score(hand_from_column)

            self.scoreboard_rows[i] = row_score
            self.scoreboard_columns[i] = column_score

            self.score += row_score + column_score

    def check_row(self, row):
        freq = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        suits = {1: 0, 2: 0, 3: 0, 4: 0}

        if None in row:
            straight = False
        else:
            straight = self.check_for_straight(row)

        for i in range(len(row)):
            if not row[i]: continue

            freq[row[i].get_rank()] += 1
            suits[row[i].get_suit()] += 1

        max_freq = max(freq.values())
        max_suit = max(suits.values())

        # Check for best poker hands
        if max_suit == 5 and straight:
            if 13 in freq and 14 in freq:
                return 9
            return 8
            
        elif max_freq == 4:
            return 7

        elif max_freq == 3 and 2 in freq.values():
            return 6
        
        elif max_suit == 5:
            return 5

        elif straight:
            return 4
        
        elif max_freq == 3:
            return 3
        
        elif max_freq == 2:
            if list(freq.values()).count(2) == 2:
                return 2
            else:
                return 1  
        else:
            return 0

    def check_for_straight(self, row):
        sorted_row = sorted(row)
        in_a_row = 1
                
        for i in range(4):
            if sorted_row[i].get_rank() + 1 == sorted_row[i + 1].get_rank():
                in_a_row += 1
        
        
        if in_a_row == 4 and sorted_row[0].get_rank() == 2 and sorted_row[-1].get_rank() == 14:
            in_a_row = 5

        return in_a_row == 5

    def get_score(self, hand):
        if hand == 9:  # Royal Flush
            score = 100
        elif hand == 8:  # Straight Flush
            score = 75
        elif hand == 7:  # Four of a Kind
            score = 50
        elif hand == 6:  # Full House
            score = 25
        elif hand == 5:  # Flush
            score = 20
        elif hand == 4:  # Straight
            score = 15
        elif hand == 3:  # Three of a Kind
            score = 10
        elif hand == 2:  # Two Pair
            score = 5
        elif hand == 1:  # One Pair
            score = 2
        else:
            score = 0
        return score
