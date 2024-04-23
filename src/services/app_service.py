from pokersquares import Game
from repository.user_repository import user_repository as ur


class AppService:
    def __init__(self):
        self.app = Game()
        self._user = None

    def login(self, username, password):
        success = ur.check_password(username, password)

        if not success:
            return False

        self._user = username

        return True

    def create_user(self, username, password):
        already_exists = ur.get_user(username)

        if not already_exists:
            ur.add_user(username, password)
            return True

        return False


app_service = AppService()
