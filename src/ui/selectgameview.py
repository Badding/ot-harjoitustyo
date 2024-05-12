import customtkinter as ctk
from services.app_service import app_service


class SelectGameView:
    def __init__(self, root, handle_game):
        self._root = root
        self._handle_game = handle_game
        self._select_game_frame = None

        self._initialize()

    def _initialize(self):

        self._select_game_frame = ctk.CTkFrame(master=self._root)

        self._welcome_message_title = ctk.CTkLabel(master=self._select_game_frame, text="Welcome to Poker Squares",
                                                   font=("Lobster two", 50))

        self.message_label = ctk.CTkLabel(
            master=self._select_game_frame, text="Select game mode:", font=("Helvetica", 18))
        self._select_game_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self._radio_var = ctk.IntVar(value=0)
        self._select_game_button1 = ctk.CTkRadioButton(
            self._select_game_frame,
            text="Default rules",
            variable=self._radio_var,
            value=0,
        )
        self._select_game_button2 = ctk.CTkRadioButton(
            self._select_game_frame,
            text="Place cards anywhere",
            variable=self._radio_var,
            value=1,
        )

        self._start_game_button = ctk.CTkButton(
            self._select_game_frame,
            text="Start Game",
            command=self._play
        )

        self._welcome_message_title.place(relx=0.5, rely=0.1, anchor='center')
        self.message_label.place(relx=0.5, rely=0.2, anchor='center')
        self._select_game_button1.place(relx=0.45, rely=0.3, anchor='w')
        self._select_game_button2.place(relx=0.45, rely=0.4, anchor='w')
        self._start_game_button.place(relx=0.5, rely=0.5, anchor='center')

    def _play(self):
        game_mode = self._radio_var.get()
        app_service.set_game_mode(game_mode)
        self._handle_game()

    def destroy(self):
        """Destroy the select game view"""

        self._select_game_frame.destroy()
