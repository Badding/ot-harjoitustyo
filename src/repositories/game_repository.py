from entities.deck import Deck


class Game:
    def __init__(self):
        self.deck = None
        self.board = []
        self.scoreboard_rows = []
        self.scoreboard_columns = []
        self.best_hand_row = []
        self.best_hand_columns = []
        self.score = 0

        self.poker_hands = {
            0: 'No Hand',
            1: 'One Pair',
            2: 'Two Pair',
            3: 'Three of a Kind',
            4: 'Straight',
            5: 'Flush',
            6: 'Full House',
            7: 'Four of a Kind',
            8: 'Straight Flush',
            9: 'Royal Flush'
        }

    def new_game(self):
        self.deck = Deck()
        self.deck.shuffle_deck()

        self.score = 0
        self.board = [[None for _ in range(5)] for _ in range(5)]
        self.scoreboard_rows = [0, 0, 0, 0, 0]
        self.scoreboard_columns = [0, 0, 0, 0, 0]
        self.best_hand_row = [0, 0, 0, 0, 0]
        self.best_hand_columns = [0, 0, 0, 0, 0]

        self.initialize_board()

    def initialize_board(self):
        for i in range(5):
            self.board[i][0] = self.deck.deal_card()

    def get_board(self):
        return self.board

    def place_card(self, row):
        if 0 <= row <= 5 and None in self.board[row]:
            index = self.board[row].index(None)
            self.board[row][index] = self.deck.get_top_card()  # virhe?
            self.deck.deal_card()
            self.calculate_score()
            return True
        return False

    def calculate_score(self):
        self.score = 0

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
        freq = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,
                9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        suits = {1: 0, 2: 0, 3: 0, 4: 0}

        if None in row:
            straight = False
        else:
            straight = self.check_for_straight(row)

        for i, item in enumerate(row, 0):
            if not row[i]:
                continue

            freq[item.get_rank()] += 1
            suits[item.get_suit()] += 1

        return self.best_hand(freq, suits, straight)

    def best_hand(self, freq, suits, straight):
        hand = 0

        max_freq = max(freq.values())
        max_suit = max(suits.values())

        if max_suit == 5 and straight:
            hand = 9 if freq[13] and freq[14] else 8

        elif max_freq == 4:
            hand = 7

        elif max_freq == 3 and 2 in freq.values():
            hand = 6

        elif max_suit == 5:
            hand = 5

        elif straight:
            hand = 4

        elif max_freq == 3:
            hand = 3

        elif max_freq == 2:
            hand = 2 if list(freq.values()).count(2) == 2 else 1

        return hand

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
        score_dict = {
            9: 100,  # Royal Flush
            8: 75,   # Straight Flush
            7: 50,   # Four of a Kind
            6: 25,   # Full House
            5: 20,   # Flush
            4: 15,   # Straight
            3: 10,   # Three of a Kind
            2: 5,    # Two Pair
            1: 2,    # One Pair
            0: 0     # No Hand
        }
        return score_dict.get(hand)

    def is_game_over(self):
        game_over = True

        for row in self.board:
            if None in row:
                game_over = False
                break

        return game_over

    def get_hand_name(self, hand):
        return self.poker_hands.get(hand)

    def get_delt_card(self):
        return self.deck.get_top_card()

    def get_score_rows(self):
        return self.scoreboard_rows

    def get_score_columns(self):
        return self.scoreboard_columns

    def get_total_score(self):
        return self.score

    def get_best_hand_rows(self):
        return self.best_hand_row

    def get_best_hand_columns(self):
        return self.best_hand_columns


game = Game()
