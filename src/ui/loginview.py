import customtkinter as ctk


class LoginView:
    def __init__(self, root, handle_quickplay):
        self._root = root
        self._handle_quickplay = handle_quickplay
        self._frame = ctk.CTkFrame(master=self._root)

        self._frame.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self._frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        self._frame.place(x=0, y=0, relwidth=1, relheight=1)

        self._title_label = ctk.CTkLabel(
            self._frame, text="Poker Squares", font=("Lobster two", 50))
        self.username_label = ctk.CTkLabel(master=self._frame, text="Username")
        self.username_entry = ctk.CTkEntry(master=self._frame)

        self.password_label = ctk.CTkLabel(self._frame, text="Password")
        self.password_entry = ctk.CTkEntry(self._frame)

        self.login_button = ctk.CTkButton(
            master=self._frame,
            text="Login",
            command=self._login_button_click
        )
        self.create_user_button = ctk.CTkButton(
            master=self._frame,
            text="Create User",
            command=self._create_user_button_click
        )
        self.create_quickplay_button = ctk.CTkButton(
            master=self._frame,
            text="Quick Play",
            command=self._handle_quickplay
        )

        # self._initialize()
        self._title_label.grid(row=0, column=1, columnspan=2)
        self.username_label.grid(row=1, column=1, pady=0, padx=10, sticky="e")
        self.username_entry.grid(row=1, column=2, pady=0, padx=10, sticky="w")

        self.password_label.grid(row=2, column=1, pady=0, padx=10, sticky="en")
        self.password_entry.grid(row=2, column=2, pady=0, padx=10, sticky="wn")

        self.login_button.grid(row=3, column=1, pady=0, padx=10, sticky="en")
        self.create_user_button.grid(
            row=3, column=2, pady=0, padx=10, sticky="wn")
        self.create_quickplay_button.grid(
            row=4, column=1, pady=0, padx=10, columnspan=2)

    def _initialize(self):
        pass

    def _login_button_click(self):
        pass

    def _create_user_button_click(self):
        pass

    def pack(self):
        pass
        # self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
