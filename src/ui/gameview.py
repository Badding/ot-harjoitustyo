import customtkinter as ctk
from services.app_service import app_service


class GameView:
    """View for the game screen"""

    def __init__(self, root, handle_help, handle_gameover):
        """Constructor for the GameView class

        Args:
            root (ctk.CTk):
                The root window of the application
            handle_help (function):
                The function to call when the help button is clicked
        """

        self._root = root
        self._handle_help = handle_help
        self._handle_gameover = handle_gameover
        self._frame = None
        self._app_service = app_service
        self._buttons = [None] * 5
        self._row_score_labels = []
        self._column_score_labels = []
        self.delt_card_label = None
        self._total_score_label = None
        self._infoframe_hands = None

        self._initialize()

    def destroy(self):
        """Destroy the game view"""

        self._frame.destroy()
        self._infoframe.destroy()

    def _initialize(self):
        """Initialize the game view"""

        self._frame = ctk.CTkFrame(master=self._root, width=800, height=600)
        self._infoframe = ctk.CTkFrame(
            master=self._root, width=400, height=600)
        self._frame.place(x=0, y=0, relwidth=0.7, relheight=1)
        self._infoframe.place(relx=0.7, y=0, relwidth=0.3, relheight=1)

        self._frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')
        self._frame.rowconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, minsize=25, uniform='a')

        self._infoframe.rowconfigure((1, 2, 3), weight=1)
        self._infoframe.columnconfigure((1, 2, 3), weight=1)

        if self._app_service.is_game_over():
            self._app_service.new_game()

        self.init_scores()

        if self._app_service.get_game_mode() == 0:
            self._init_board_default()
        else:
            self._init_board_anywhere()

        self.init_info()

    def _button_callback(self, row, column):
        """Callback function for placing the card on the board

        If the card is placed successfully, the button is removed and the scores are updated
        If the row is not full, a new button is placed on the board
        """

        card = self._app_service.get_delt_card()
        board = self._app_service.get_board()
        # index = board[row].index(None)
        card_placed = self._app_service.place_card(row, column)

        if card_placed:

            self._buttons[row] = None
            self._place_label(row, column, card)
            self._update_scores()
            self._update_delt_card()
            self._update_total_score()

            if self._app_service.is_game_over():
                self._app_service.save_stats()
                self._handle_gameover()

        if None in board[row] and self._app_service.get_game_mode() == 0:
            self._buttons[row] = self._place_button(row, column + 1)

    def make_command(self, row, column):
        """Create a command for the button

        Args:
            row (int): The row to place the card on

        Returns:
            function: The command function
        """

        return lambda: self._button_callback(row, column)

    def _init_newgame(self):
        """Initialize a new game"""

        self._app_service.new_game()
        self._initialize()

    def _place_button(self, row, column):
        """Place a button on the board

        Args:
            row (int): The row to place the button on
            column (int): The column to place the button on

        Returns:
            ctk.CTkButton: The button that was placed
        """

        button = ctk.CTkButton(self._frame, text="", width=40, height=80,
                               font=("Lobster two", 16),
                               command=self.make_command(row, column))
        button.grid(row=row, column=column, pady=10, padx=10)

        return button

    def _place_label(self, row, label_index, card):
        """Place a label on the board

        This method places a label on the board with the rank and suit of the card

        Args:
            row (int): The row to place the label on
            label_index (int): The column to place the label on
            card (Card): The card to place on the label

        Returns:
            bool: True if the label was placed successfully
        """

        label = ctk.CTkLabel(self._frame, width=55, height=90, font=("Lobster two", 20),
                             text=card.get_rank_symbol() + "\n" + card.get_suit_symbol(),
                             fg_color="white",
                             text_color=card.get_color(),
                             corner_radius=8)
        label.grid(row=row, column=label_index, pady=10, padx=10)

        return True

    def _init_board_default(self):
        """Places cards on the board and initializes the buttons for placing cards

        method gets current board from app_service and places cards on the board
        """

        board = self._app_service.get_board()
        for i in range(5):
            row_complete = False

            for j in range(5):
                if row_complete:
                    continue

                if board[i][j] is not None:
                    card = board[i][j]
                    self._place_label(i, j, card)
                else:
                    button = self._place_button(i, j)
                    self._buttons.append(button)
                    row_complete = True

    def _init_board_anywhere(self):
        """Places cards on the board and initializes the buttons for placing cards

        method gets current board from app_service and places cards on the board
        """

        board = self._app_service.get_board()
        for i in range(5):
            for j in range(5):
                if board[i][j] is not None:
                    card = board[i][j]
                    self._place_label(i, j, card)
                else:
                    button = self._place_button(i, j)
                    self._buttons.append(button)

    def init_scores(self):
        """Initializes the score labels for the rows and columns"""

        self._row_score_labels = []
        self._column_score_labels = []
        row_scores = self._app_service.get_score_rows()
        column_scores = self._app_service.get_score_columns()

        for i in range(5):
            row_label = ctk.CTkLabel(
                self._frame, text=row_scores[i], font=("Lobster two", 20))
            row_label.grid(row=i, column=5)

            column_label = ctk.CTkLabel(
                self._frame, text=column_scores[i], font=("Lobster two", 20))
            column_label.grid(row=5, column=i)

            self._row_score_labels.append(row_label)
            self._column_score_labels.append(column_label)

    def _update_scores(self):
        """Update the score labels for the rows and columns"""

        row_scores = self._app_service.get_score_rows()
        column_scores = self._app_service.get_score_columns()

        for i in range(5):
            self._row_score_labels[i].configure(text=row_scores[i])
            self._column_score_labels[i].configure(text=column_scores[i])

    def _update_delt_card(self):
        """Update the delt card label with the new delt card"""

        delt_card = self._app_service.get_delt_card()

        self.delt_card_label.configure(
            text=delt_card.get_rank_symbol() + "\n" + delt_card.get_suit_symbol())
        self.delt_card_label.configure(text_color=delt_card.get_color())

    def _update_total_score(self):
        """Update the total score label with the new total score"""

        total_score = self._app_service.get_total_score()
        self._total_score_label.configure(text=f"Score: {total_score}")

    def init_info(self):
        """Initializes the info frame contains delt card, and total score labels and help button"""

        helpview = ctk.CTkButton(
            self._infoframe, text="i", command=self._handle_help,
            width=40, height=40,
            font=("Lobster two", 30))

        helpview.place(relx=0.95, rely=0.1, anchor="se")
        delt_card = self._app_service.get_delt_card()
        self.delt_card_label = ctk.CTkLabel(self._infoframe, width=55, height=90, font=("Lobster two", 20),
                                            text=delt_card.get_rank_symbol() + "\n" + delt_card.get_suit_symbol(),
                                            fg_color="white",
                                            text_color=delt_card.get_color(),
                                            corner_radius=8)

        self.delt_card_label.grid(row=1, column=2, pady=30)

        total_score = self._app_service.get_total_score()

        self._total_score_label = ctk.CTkLabel(
            self._infoframe, text=f"Score: {total_score}", font=("Lobster two", 24))
        self._total_score_label.grid(row=2, column=2)
