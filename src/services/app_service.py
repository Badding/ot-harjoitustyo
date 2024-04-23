from repositories.user_repository import user_repository as ur
from repositories.game_repository import game


class AppService:
    def __init__(self):
        self._game = game
        self._user = None

    def login(self, username, password):
        success = ur.check_password(username, password)

        if not success:
            return False

        self._user = username

        return True

    def create_user(self, username, password):
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


app_service = AppService()
