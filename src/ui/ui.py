# from loginview import LoginView
from ui.gameview import GameView
from ui.loginview import LoginView
from pokersquares import Game


class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Squares")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)
        self._current_view = None

        # for testing
        self._game = Game()
        self._game.new_game()

    def run(self):

        self._show_login()
        # self._show_game()

    def _handle_login(self):
        pass

    def _handle_quickplay(self):
        self._show_game()

    def _handle_create_user(self):
        pass

    def _show_login(self):
        self._hide_current_view()

        self._current_view = LoginView(self.root, self._handle_quickplay)

        # self._current_view.pack()

    def _show_game(self):
        self._hide_current_view()

        self._current_view = GameView(self.root, self._game)

        # self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def close(self):
        self.root.destroy()
