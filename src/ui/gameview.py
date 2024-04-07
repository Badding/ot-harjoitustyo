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

        self._initialize()
        self.init_board()
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ctk.CTkFrame(master=self._root)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _button_callback(self, row):
        card = self._gamestate.get_delt_card()
        board = self._gamestate.get_board()
        index = board[row].index(None)
        card_placed = self._gamestate.place_card(row)

        if card_placed:
            self._buttons[row].destroy()
            self._place_label(row, index, card)

        if None in board[row]:
            self._buttons[row] = self._place_button(row, index + 1)

    def make_command(self, row):
        return lambda: self._button_callback(row)

    def _place_button(self, row, column):
        button = ctk.CTkButton(self._frame, text="", width=40, height=80,
                                font=("Lobster two", 16),
                                command=self.make_command(row))
        button.grid(row=row, column=column, pady=10, padx=10)

        return button
    
    def _place_label(self, row, label_index, card):
        label = ctk.CTkLabel(self._frame, width=40, height=80, font=("Lobster two", 20),
                                text=card.get_rank_symbol() + "\n" + card.get_suit_symbol(),
                                fg_color="white",
                                text_color=card.get_color(),
                                corner_radius=8)
        label.grid(row=row, column=label_index, pady=10, padx=10)

        return True

    def init_board(self):
        board = self._gamestate.get_board()
        for i in range(5):
            card = board[i][0]
            self._place_label(i, 0, card)

            button = self._place_button(i, 1)
            self._buttons.append(button)

    

    def draw_score(self):
        row_scores = self._gamestate.get_row_scores()
        column_scores = self._gamestate.get_column_scores()

        for i in range(5):
            pass