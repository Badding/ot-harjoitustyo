from ui.gameview import GameView
from ui.loginview import LoginView
from ui.helpview import HelpView
from ui.gameoverview import GameoverView
from ui.createuserview import CreateUserView
from ui.selectgameview import SelectGameView


class UI:
    """Main class for the UI of the game

    Attributes:
        root (ctk.CTk):
            The root window of the application
        _current_view (object):
            The current view object
    """

    def __init__(self, root):
        """Constructor for the UI class

        Args:
            root (ctk.CTk):
                The root window of the application
        """
        self.root = root
        self.root.title("Poker Squares")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)
        self._current_view = None

    def run(self):
        """Start the UI"""
        self._show_login()

    def _handle_create_user(self):
        self._hide_current_view()

        self._current_view = CreateUserView(self.root, self._show_login)

    def _show_login(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self.root,
            self._show_select_game,
            self._handle_create_user
        )

    def _show_game(self):
        self._hide_current_view()

        self._current_view = GameView(
            self.root, self._show_help, self._show_game_over)

    def _show_select_game(self):
        self._hide_current_view()

        self._current_view = SelectGameView(self.root, self._show_game)

    def _show_help(self):
        self._hide_current_view()

        self._current_view = HelpView(
            self.root,
            self._show_game,
            self._show_login
        )

    def _show_game_over(self):
        self._hide_current_view()

        self._current_view = GameoverView(self.root, self._show_game)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def close(self):
        self.root.destroy()
