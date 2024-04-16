import customtkinter as ctk
from tkinter import constants


class GameView:
    def __init__(self, root, game):
        self._root = root

        self._frame = None
        self._gamestate = game
        self._buttons = []
        self._row_score_labels = []
        self._column_score_labels = []
        self.delt_card_label = None
        self._total_score_label = None
        self._infoframe_hands = None

        self._initialize()
        self.init_scores()
        self.init_board()

        self.init_info()  # frame erikseen
        # self.score_frame()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ctk.CTkFrame(master=self._root, width=800, height=600)
        self._infoframe = ctk.CTkFrame(
            master=self._root, width=400, height=600)
        self._frame.place(x=0, y=0, relwidth=0.7, relheight=1)
        self._infoframe.place(relx=0.7, y=0, relwidth=0.3, relheight=1)

        # self._frame.pack()
        # self._infoframe.pack()

        self._frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')
        self._frame.rowconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, minsize=25, uniform='a')

        self._infoframe.rowconfigure((1, 2, 3), weight=1)
        self._infoframe.columnconfigure((1, 2, 3), weight=1)

    def pack(self):
        pass
        # self._frame.pack(fill=constants.X)

    def _button_callback(self, row):
        card = self._gamestate.get_delt_card()
        board = self._gamestate.get_board()
        index = board[row].index(None)
        card_placed = self._gamestate.place_card(row)

        if card_placed:
            self._buttons[row].destroy()
            self._place_label(row, index, card)
            self._update_scores()
            self._update_delt_card()
            self._update_total_score()

            # add check if game is over, show new game button

        if None in board[row]:
            self._buttons[row] = self._place_button(row, index + 1)

    def make_command(self, row):
        return lambda: self._button_callback(row)

    def _place_newgame_button(self):
        pass

    def _place_button(self, row, column):
        button = ctk.CTkButton(self._frame, text="", width=40, height=80,
                               font=("Lobster two", 16),
                               command=self.make_command(row))
        button.grid(row=row, column=column, pady=10, padx=10)

        return button

    def _place_label(self, row, label_index, card):
        label = ctk.CTkLabel(self._frame, width=55, height=90, font=("Lobster two", 20),
                             text=card.get_rank_symbol() + "\n" + card.get_suit_symbol(),
                             fg_color="white",
                             text_color=card.get_color(),
                             corner_radius=8)
        label.grid(row=row, column=label_index, pady=10, padx=10)  # oikea
        # label.grid(row=row, column=label_index)

        return True

    def init_board(self):
        board = self._gamestate.get_board()
        for i in range(5):
            card = board[i][0]
            self._place_label(i, 0, card)

            button = self._place_button(i, 1)
            self._buttons.append(button)

        # self._frame.grid(row=0, column=0) #not sure if this is necessary

    def init_scores(self):
        row_scores = self._gamestate.get_score_rows()
        column_scores = self._gamestate.get_score_columns()

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
        row_scores = self._gamestate.get_score_rows()
        column_scores = self._gamestate.get_score_columns()

        for i in range(5):
            self._row_score_labels[i].configure(text=row_scores[i])
            self._column_score_labels[i].configure(text=column_scores[i])

    def _update_delt_card(self):
        delt_card = self._gamestate.get_delt_card()

        self.delt_card_label.configure(
            text=delt_card.get_rank_symbol() + "\n" + delt_card.get_suit_symbol())
        self.delt_card_label.configure(text_color=delt_card.get_color())

    def _update_total_score(self):
        total_score = self._gamestate.get_total_score()
        self._total_score_label.configure(text=f"Score: {total_score}")

    def _update_infoframe_hands(self):
        best_hands_row = self._gamestate.get_best_hands_row()
        best_hands_column = self._gamestate.get_best_hands_column()

        for i in range(5):
            pass

    def init_info(self):
        delt_card = self._gamestate.get_delt_card()
        self.delt_card_label = ctk.CTkLabel(self._infoframe, width=55, height=90, font=("Lobster two", 20),
                                            text=delt_card.get_rank_symbol() + "\n" + delt_card.get_suit_symbol(),
                                            fg_color="white",
                                            text_color=delt_card.get_color(),
                                            corner_radius=8)

        self.delt_card_label.grid(row=0, column=2, pady=30)

        total_score = self._gamestate.get_total_score()
        self._total_score_label = ctk.CTkLabel(
            self._infoframe, text=f"Score: {total_score}", font=("Lobster two", 24))
        self._total_score_label.grid(row=1, column=2)

        # self._infoframe_hands = ctk.CTkLabel(self._infoframe, text="", font=("Lobster two", 24))
