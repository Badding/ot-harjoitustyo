import customtkinter as ctk
from services.app_service import app_service


class LoginView:
    def __init__(self, root, handle_quickplay, handle_create_user):
        self._root = root
        self._handle_quickplay = handle_quickplay
        self._handle_create_user = handle_create_user
        self._frame = ctk.CTkFrame(master=self._root)

        self._frame.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self._frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        self._frame.place(x=0, y=0, relwidth=1, relheight=1)

        self._title_label = ctk.CTkLabel(
            self._frame, text="Poker Squares", font=("Lobster two", 50))
        self.username_label = ctk.CTkLabel(master=self._frame, text="Username")
        self.username_entry = ctk.CTkEntry(master=self._frame)

        self.password_label = ctk.CTkLabel(self._frame, text="Password")
        self.password_entry = ctk.CTkEntry(self._frame, show="•")

        self.error_message_label = ctk.CTkLabel(
            self._frame, text="Invalid username or password",
            fg_color="red",
            corner_radius=8,
        )

        self.login_button = ctk.CTkButton(
            master=self._frame,
            text="Login",
            command=self._login_button_click
        )
        self.create_user_button = ctk.CTkButton(
            master=self._frame,
            text="Create User",
            command=self._handle_create_user
        )
        self.create_quickplay_button = ctk.CTkButton(
            master=self._frame,
            text="Quick Play",
            command=self._handle_quickplay
        )

        self._initialize()

    def _initialize(self):
        self._title_label.grid(row=0, column=1, columnspan=2)
        self.username_label.grid(row=1, column=1, pady=0, padx=10, sticky="e")
        self.username_entry.grid(row=1, column=2, pady=0, padx=10, sticky="w")

        self.password_label.grid(row=2, column=1, pady=0, padx=10, sticky="en")
        self.password_entry.grid(row=2, column=2, pady=0, padx=10, sticky="wn")

        self.error_message_label.grid(row=3, column=1, columnspan=2)
        self.error_message_label.grid_forget()

        self.login_button.grid(row=3, column=1, pady=0, padx=10, sticky="en")
        self.create_user_button.grid(
            row=3, column=2, pady=0, padx=10, sticky="wn")
        self.create_quickplay_button.grid(
            row=4, column=1, pady=0, padx=10, columnspan=2)

    def _login_button_click(self):
        user = self.username_entry.get()
        password = self.password_entry.get()
        success = app_service.login(user, password)

        if success:
            self._handle_quickplay()
        else:
            self.error_message_label.grid(row=3, column=1, columnspan=2)

    def destroy(self):
        self._frame.destroy()
