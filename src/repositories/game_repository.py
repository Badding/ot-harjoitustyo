from entities.deck import Deck
from entities.scores import Scores


class Game:
    """Class for the game logic"""

    def __init__(self):
        """Constructor for the Game class"""
        self.deck = None
        self.board = []
        """
        self.scoreboard_rows = []
        self.scoreboard_columns = []
        self.score = 0
        """
        self._scores = Scores()
        self.best_hand_row = []
        self.best_hand_columns = []

        self.game_mode = 0

        self.poker_hands = {
            0: 'No Hand',
            1: 'One Pair',
            2: 'Two Pairs',
            3: 'Three of a Kind',
            4: 'Straight',
            5: 'Flush',
            6: 'Full House',
            7: 'Four of a Kind',
            8: 'Straight Flush',
            9: 'Royal Flush'
        }

    def new_game(self):
        """Start a new game

            Initializes the deck, shuffles it and resets the lists
        """

        self.deck = Deck()
        self.deck.shuffle_deck()
        self._scores.reset()

        self.board = [[None for _ in range(5)] for _ in range(5)]

        self.best_hand_row = [0, 0, 0, 0, 0]
        self.best_hand_columns = [0, 0, 0, 0, 0]

        if self.game_mode == 0:
            self._initialize_board()

    def _initialize_board(self):
        """Initialize the board with 5 cards in the first column"""

        for i in range(5):
            self.board[i][0] = self.deck.deal_card()

    def place_card(self, row, column):
        """Place a card on the board

        Args:
            row (int): The row to place the card on

        Returns:
            bool: True if the card was placed on the board
        """
        if 0 <= row <= 4 and 0 <= column <= 4:
            if self.board[row][column] is not None:
                return False

            self.board[row][column] = self.deck.get_top_card()
            self.deck.deal_card()
            self.calculate_score()
            return True
        return False

    def calculate_score(self):
        """Calculate the total score for the rows and columns"""

        score = 0

        for i in range(5):
            column = [self.board[j][i] for j in range(5)]
            row = self.board[i]

            hand_from_row = self._check_row(row)
            hand_from_column = self._check_row(column)

            self.best_hand_row[i] = hand_from_row
            self.best_hand_columns[i] = hand_from_column

            row_score = self._scores.get_score(hand_from_row)
            column_score = self._scores.get_score(hand_from_column)

            self._scores.set_scoreboard_rows(i, row_score)
            self._scores.set_scoreboard_columns(i, column_score)

            score += row_score + column_score

        self._scores.set_total_score(score)

    def _check_row(self, row):
        """Check the row for the best possible poker hand

        Calculates the occurences of each rank and suit in the row.
        If the row is full, calls the check_for_straight function to check for a straight.
        Calls the best_hand function to determine the best hand for the row.

        Args:
            row (list): A list of cards in the row

        Returns:
            int: The best poker hand on the row
        """

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
        """Helper function for check_row to determine the best hand

        Args:
            freq (dict): The frequency of each rank in the row
            suits (dict): The frequency of each suit in the row
            straight (bool): True if the row is a straight

        Returns:
            int: The best poker hand on the row
        """

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
        """helper function for check_row

        Works with ace as highest or lowest card in the straight

        Args:
            row (list): A list of cards in the row
        """

        sorted_row = sorted(row)
        in_a_row = 1

        for i in range(4):
            if sorted_row[i].get_rank() + 1 == sorted_row[i + 1].get_rank():
                in_a_row += 1

        if in_a_row == 4 and sorted_row[0].get_rank() == 2 and sorted_row[-1].get_rank() == 14:
            in_a_row = 5

        return in_a_row == 5

    def get_game_mode_name(self):
        game_mode_names = {
            0: "Default rules",
            1: "Place cards anywhere"
        }
        return game_mode_names.get(self.game_mode)

    def is_game_over(self):
        if self.deck is None:
            return True

        game_over = True

        for row in self.board:
            if None in row:
                game_over = False
                break

        return game_over

    def end_game(self):
        """End the game"""

        self.deck = None

    def set_game_mode(self, mode):
        self.game_mode = mode

    def get_game_mode(self):
        return self.game_mode

    def get_board(self):
        return self.board

    def get_hand_name(self, hand):
        return self.poker_hands.get(hand)

    def get_hand_score(self, hand):
        return self._scores.get_score(hand)

    def get_delt_card(self):
        return self.deck.get_top_card()

    def get_score_rows(self):
        return self._scores.get_scoreboard_rows()

    def get_score_columns(self):
        return self._scores.get_scoreboard_columns()

    def get_total_score(self):
        return self._scores.get_total_score()

    def get_best_hand_rows(self):
        return self.best_hand_row

    def get_best_hand_columns(self):
        return self.best_hand_columns


game = Game()
