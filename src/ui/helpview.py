import customtkinter as ctk
from services.app_service import app_service


class HelpView:
    """View for the help screen"""

    def __init__(self, root, handle_back, handle_logout):
        """Constructor for the HelpView class

        setting up the help view, creating the widgets

        Args:
            root (ctk.CTk):
                The root window of the application
            handle_back (function):
                The function to call when the back button is clicked
            handle_logout (function):
                The function to call when the logout button is clicked
        """

        self._root = root
        self._app_service = app_service
        self._handle_back = handle_back
        self._handle_logout = handle_logout
        self._help_frame = ctk.CTkFrame(master=self._root)
        self._help_frame.place(x=0, y=0, relwidth=1, relheight=1)

        self._help_frame.rowconfigure((1, 2, 3, 4), weight=1)
        self._help_frame.columnconfigure((1, 2, 3, 4), weight=1)

        self._welcome_message_title = ctk.CTkLabel(
            self._help_frame, text="Welcome to Poker Squares",
            font=("Lobster two", 50))

        self._info_message = ctk.CTkLabel(
            self._help_frame, text="""The object of this game is to get the best
            possible poker hand for each row and column. You can place a card by
            pressing the blue button. The game ends when the whole table is full
            """,
            font=("Helvetica", 18))

        self._card_hands_label = ctk.CTkLabel(
            self._help_frame, text="", font=("Helvetica", 18))

        self._logout_button = ctk.CTkButton(
            master=self._help_frame,
            text="Logout",
            command=self._handle_logout
        )
        self._back_to_game = ctk.CTkButton(
            master=self._help_frame,
            text="Back to game",
            command=self._handle_back
        )

        self._initialize()

    def _initialize(self):
        """Initialize the help view

        This method places the widgets for the help view
        """

        self._welcome_message_title.grid(row=0, column=2, pady=5, columnspan=2)
        self._info_message.grid(row=1, column=2, pady=20, columnspan=2)

        self._update_card_hands_label()
        self._card_hands_label.grid(
            row=2, column=2, pady=5, padx=10, columnspan=2)

        self._back_to_game.grid(row=3, column=2, pady=5,
                                padx=10, columnspan=2, sticky="n")
        self._logout_button.grid(row=4, column=2, pady=10,
                                 padx=10, columnspan=2, sticky="n")

    def _update_card_hands_label(self):
        """Update the card hands label

        This method updates the label with hand names and scores
        """
        text = "Points for each hand:\n\n"
        for i in range(10):
            hand_name = self._app_service.get_hand_name(i)
            hand_score = self._app_service.get_hand_score(i)
            text += f"{hand_name} is {hand_score}\n"

        self._card_hands_label.configure(text=text)

    def destroy(self):
        self._help_frame.destroy()
