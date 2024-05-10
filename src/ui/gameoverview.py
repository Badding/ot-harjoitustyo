import customtkinter as ctk
from services.app_service import app_service


class GameoverView:
    """View for the gameover screen"""

    def __init__(self, root, handle_new_game):
        """Constructor for the GameView class

        Args:
            root (ctk.CTk):
                The root window of the application
            handle_help (function):
                The function to call when the help button is clicked
        """
        self._root = root
        self._app_service = app_service
        self._handle_new_game = handle_new_game
        self._gameover_frame = ctk.CTkFrame(master=self._root)
        self._gameover_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self._gameover_frame.rowconfigure((0, 1, 2), weight=1)
        self._gameover_frame.columnconfigure((0, 1, 2), weight=1)

        self._welcome_message_title = ctk.CTkLabel(
            self._gameover_frame, text="Gameover",
            font=("Lobster two", 40))

        self._user_stats = ctk.CTkLabel(
            self._gameover_frame, text="", font=("Helvetica", 18))

        self._last_game_stats = ctk.CTkLabel(
            self._gameover_frame, text="", font=("Helvetica", 18))

        self._topscores = ctk.CTkLabel(
            self._gameover_frame, text="", font=("Helvetica", 18))

        self._handle_new_game = ctk.CTkButton(
            master=self._gameover_frame,
            text="New Game",
            command=self._handle_new_game
        )

        self._initialize()

    def _initialize(self):
        """Initialize the help view"""
        
        self._update_user_stats()
        self._update_last_game_stats()
        self._update_top_scores()

        """
        self._welcome_message_title.grid(row=0, column=0, expand = True, fill = True, columnspan=4)
        self._user_stats.grid(row=2, column=0, columnspan=1)
        self._last_game_stats.grid(row=1, column=1, columnspan=1)
        self._topscores.grid(row=1, column=2, columnspan=1)
        self._handle_new_game.grid(row=2, column=1)
        """
        self._welcome_message_title.pack(side="top", fill="both")
        self._handle_new_game.pack(pady=30, side="bottom")
        self._user_stats.pack(side="left", expand=True, fill="both")
        self._last_game_stats.pack(side="left", expand=True, fill="both")
        self._topscores.pack(side="left", expand=True, fill="both")

    def destroy(self):
        """Destroy the game view"""

        self._gameover_frame.destroy()

    def _update_user_stats(self):
        """Update the user stats"""

        user = self._app_service.get_user()
        if not user:
            return

        user_id = self._app_service.get_id(user)[0]
        user_stats = self._app_service.get_user_stats(user_id)
        top_scores = user_stats[2]
        games_played = user_stats[3]

        hands_played = user_stats[4]

        hands_played_split = hands_played.split(';')
        hands = "Hands made\n\n"

        for i in range(8, -1, -1):
            name = self._app_service.get_hand_name(i)
            hands += f"{name} : {hands_played_split[i]}\n"

        text = f"{user}'s all time stats\n\nTop score : {top_scores}\n\ngames : {games_played}\n\n{hands}"

        self._user_stats.configure(text=text)

    def _update_last_game_stats(self):
        """Update the last game played stats"""

        best_on_rows = self._app_service.get_best_hand_rows()
        best_on_columns = self._app_service.get_best_hand_columns()
        score = self._app_service.get_total_score()

        text = f"Score: {score}\n\nHands made in last game\n\n"

        for i in range(9, -1, -1):
            row_count = best_on_rows.count(i)
            column_count = best_on_columns.count(i)
            sum = row_count + column_count

            if sum:
                name = self._app_service.get_hand_name(i)
                text += f"{name} : {sum}\n"

        self._last_game_stats.configure(text=text)

    def _update_top_scores(self):
        """Update the top scores"""

        top_scores = self._app_service.get_top_scores()
        text = "Top scores:\n\n"

        for row in top_scores:
            user_id = row[0]
            score = row[1]
            user = self._app_service.get_user_by_id(user_id)[1]
            text += f"{user} : {score}\n"

        self._topscores.configure(text=text)
