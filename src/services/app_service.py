from repositories.user_repository import user_repository as ur
from repositories.game_repository import game


class AppService:
    """Service class for the application

    This class handles all the application logic and acts
    as a bridge between the UI and the repositories.

    Attributes:
        _game (Game):
            The game repository
        _user (str):
            The current user
    """

    def __init__(self):
        """Constructor for the AppService class"""

        self._game = game
        self._user = None

    def login(self, username, password):
        """Login a user

        Checks if the username and password match and logs the user in

        Args:
            username (str):
                The username to log in
            password (str):
                The password to log in

        Returns:
            True if the user was logged in, False if the username and password do not match
        """

        success = ur.check_password(username, password)

        if not success:
            return False

        self._user = username

        return True

    def logout(self):
        """Logout the current user"""
        self._user = None

    def create_user(self, username, password):
        """Create a new user

        Checks if the user already exists and if not, adds the user to the database

        Args:
            username (str):
                The username of the new user
            password (str):
                The password of the new user

        Returns:
            True if the user was created, False if the user already exists
        """

        already_exists = ur.get_user(username)

        if already_exists:
            return False

        ur.add_user(username, password)
        user_id = ur.get_id(username)[0]

        ur.init_new_user_stat(user_id)

        return True

    def save_stats(self):
        """Save the user stats to the database"""

        if not self._user:
            return

        user_id = ur.get_id(self._user)[0]
        stats = ur.get_user_stats(user_id)
        score = self._game.get_total_score()

        if score > stats[2]:
            ur.update_top_score(user_id, score)

        ur.update_games_played(user_id, stats[3] + 1)

        best_on_rows = self.get_best_hand_rows()
        best_on_columns = self.get_best_hand_columns()
        hands_made = stats[4].split(';')

        for i in range(10):
            last = int(hands_made[i])
            row_count = best_on_rows.count(i)
            column_count = best_on_columns.count(i)
            hands_made[i] = str(last + row_count + column_count)

        hands_made = ';'.join(hands_made)
        ur.update_hands_made(user_id, hands_made)

    # Game related methods

    def new_game(self):
        self._game.new_game()

    def get_delt_card(self):
        return self._game.get_delt_card()

    def get_board(self):
        return self._game.get_board()

    def place_card(self, row):
        return self._game.place_card(row)

    def is_game_over(self):
        return self._game.is_game_over()

    def get_score_rows(self):
        return self._game.get_score_rows()

    def get_score_columns(self):
        return self._game.get_score_columns()

    def get_total_score(self):
        return self._game.get_total_score()

    def get_best_hand_rows(self):
        return self._game.get_best_hand_rows()

    def get_best_hand_columns(self):
        return self._game.get_best_hand_columns()

    def get_hand_name(self, hand):
        return self._game.get_hand_name(hand)

    def get_hand_score(self, hand):
        return self._game.get_score(hand)

    def get_user(self):
        return self._user

    def get_id(self, user):
        return ur.get_id(user)

    def get_user_stats(self, user_id):
        return ur.get_user_stats(user_id)

    def get_top_scores(self):
        return ur.get_top_scores()

    def get_user_by_id(self, user_id):
        return ur.get_user_by_id(user_id)


app_service = AppService()
