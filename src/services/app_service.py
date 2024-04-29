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
        success = ur.check_password(username, password)

        if not success:
            return False

        self._user = username

        return True

    def logout(self):
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
        return True

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


app_service = AppService()
