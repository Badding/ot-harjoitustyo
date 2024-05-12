class Scores:
    """Class for keeping the scores"""

    def __init__(self):
        self._score = 0
        self.scoreboard_rows = [0, 0, 0, 0, 0]
        self.scoreboard_columns = [0, 0, 0, 0, 0]

    def reset(self):
        self._score = 0
        self.scoreboard_rows = [0, 0, 0, 0, 0]
        self.scoreboard_columns = [0, 0, 0, 0, 0]

    def get_score(self, hand):
        """Get the score for the hand

        Args:
            hand (int): The hand to get the score for

        Returns:
            int: The score for the hand
        """

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

    def get_total_score(self):
        return self._score

    def set_total_score(self, score):
        self._score = score

    def get_scoreboard_rows(self):
        return self.scoreboard_rows

    def get_scoreboard_columns(self):
        return self.scoreboard_columns

    def set_scoreboard_rows(self, row, score):
        self.scoreboard_rows[row] = score

    def set_scoreboard_columns(self, column, score):
        self.scoreboard_columns[column] = score
