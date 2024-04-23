import customtkinter as ctk
from services.app_service import app_service


class CreateUserView:
    def __init__(self, root, handle_back):
        self._root = root
        self._handle_back = handle_back
        self._frame = ctk.CTkFrame(master=self._root)

        self._frame.columnconfigure((0, 1, 2, 3), weight=1)

        self._frame.place(x=0, y=0, relwidth=1, relheight=1)

        self._title_label = ctk.CTkLabel(
            self._frame, text="Poker Squares", font=("Lobster two", 50))
        self._title_create_user_label = ctk.CTkLabel(
            self._frame, text="Create User", font=("Lobster two", 25))

        self.username_label = ctk.CTkLabel(
            master=self._frame, text="Username",)
        self.username_entry = ctk.CTkEntry(master=self._frame)

        self.password_label = ctk.CTkLabel(self._frame, text="Password")
        self.password_entry = ctk.CTkEntry(self._frame, show="•")

        self.password_label2 = ctk.CTkLabel(self._frame, text="Password again")
        self.password_entry2 = ctk.CTkEntry(self._frame, show="•")

        self.error_message_text = ctk.StringVar()
        self.error_message_label = ctk.CTkLabel(
            self._frame, textvariable=self.error_message_text,
            fg_color="red",
            corner_radius=8,
        )
        self.user_created_label = ctk.CTkLabel(
            self._frame, text="User created!",
            fg_color="green",
            corner_radius=8,

        )

        self.back_button = ctk.CTkButton(
            master=self._frame,
            text="Back",
            command=self._handle_back
        )
        self.create_user_button = ctk.CTkButton(
            master=self._frame,
            text="Create User",
            command=self._create_user_handler
        )

        self._initialize()

    def _initialize(self):
        self._title_label.grid(row=0, column=1, columnspan=2, pady=30)
        self._title_create_user_label.grid(
            row=1, column=1, columnspan=2, pady=40)

        self.username_label.grid(row=2, column=1, pady=5, padx=10, sticky="e")
        self.username_entry.grid(row=2, column=2, pady=5, padx=10, sticky="w")

        self.password_label.grid(row=3, column=1, pady=5, padx=10, sticky="e")
        self.password_entry.grid(row=3, column=2, pady=5, padx=10, sticky="w")

        self.password_label2.grid(row=4, column=1, pady=5, padx=10, sticky="e")
        self.password_entry2.grid(row=4, column=2, pady=5, padx=10, sticky="w")

        self.error_message_label.grid(row=5, column=1, columnspan=2)
        self.error_message_label.grid_forget()
        self.user_created_label.grid(row=5, column=1, columnspan=2)
        self.user_created_label.grid_forget()

        self.back_button.grid(row=6, column=1, pady=30, padx=10, sticky="en")
        self.create_user_button.grid(
            row=6, column=2, pady=30, padx=10, sticky="wn")

    def _create_user_handler(self):
        user = self.username_entry.get()
        password = self.password_entry.get()
        password2 = self.password_entry2.get()

        self.error_message_label.grid_forget()
        self.user_created_label.grid_forget()

        if not user:
            self.error_message_text.set("Username cannot be empty")
            self.error_message_label.grid(row=5, column=1, columnspan=2)

        elif not password or password != password2:
            self.error_message_text.set("Passwords do not match")
            self.error_message_label.grid(row=5, column=1, columnspan=2)

        elif user and password and password == password2:
            success = app_service.create_user(user, password)

            if success:
                self.user_created_label.grid(row=5, column=1, columnspan=2)
            else:
                self.error_message_text.set("Username already exists")
                self.error_message_label.grid(row=5, column=1, columnspan=2)

    def destroy(self):
        self._frame.destroy()
