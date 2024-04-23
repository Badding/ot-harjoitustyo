# from loginview import LoginView
from ui.gameview import GameView
from ui.loginview import LoginView
from ui.createuserview import CreateUserView


class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Squares")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)
        self._current_view = None

    def run(self):

        self._show_login()

    def _handle_login(self):
        self._show_login()

    def _handle_quickplay(self):
        self._show_game()

    def _handle_create_user(self):
        self._hide_current_view()

        self._current_view = CreateUserView(self.root, self._handle_login)

    def _show_login(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self.root,
            self._handle_quickplay,
            self._handle_create_user
        )

    def _show_game(self):
        self._hide_current_view()

        self._current_view = GameView(self.root)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def close(self):
        self.root.destroy()
