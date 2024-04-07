from tkinter import ttk, constants, Canvas

class LoginView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        '''
        self.username_label = ttk.Label(master=self._frame, text="Username")
        self.username_entry = ttk.Entry(master=self._frame)

        self.password_label = ttk.Label(master=self._frame, text="Password")
        self.password_entry = ttk.Entry(master=self._frame)

        self.login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_button_click
        )
        self.create_user_button = ttk.Button(
            master=self._frame,
            text="Create User",
            command=self._create_user_button_click
        )
        '''
        self._initialize()
        
    def _login_button_click(self):
        pass

    def _create_user_button_click(self):
        pass
    
    def _quick_play_button_click(self):
        pass

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame)

        label = ttk.Label(master=self._frame, text="Poker Squares", font=("Lobster two", 42)) 

        login_button = ttk.Button(master=self._frame, text="Login", command=self._login_button_click)
        create_button = ttk.Button(master=self._frame, text="New Account", command=self._create_user_button_click)
        quick_play_button = ttk.Button(master=self._frame, text="Quick Play", command=self._quick_play_button_click)

        
        #canvas = Canvas(master=self._frame, width=200, height=200)
        #image = canvas.create_image(0, 0, anchor="nw", image=my_image)
        
        self._frame.grid(row=0, column=0, sticky=(constants.N, constants.W, constants.E, constants.S))
        self._frame.grid_rowconfigure((1,2), weight=1)


        self._frame.grid_rowconfigure(3, weight=2)
        self._frame.grid_columnconfigure((0,1), weight=1)
        label.grid(row=0, column=0, columnspan=2, pady=50)
        username_label.grid(row=1, column=0, sticky="e", pady=5)
        username_entry.grid(row=1, column=1, sticky="w", pady=5)

        password_label.grid(row=2, column=0, sticky="e", pady=5)
        password_entry.grid(row=2, column=1, sticky="w", pady=5)
        login_button.grid(row=3, column=1, sticky="w", pady=5)
        create_button.grid(row=4, column=1, sticky="w", pady=5)
        quick_play_button.grid(row=5, column=1, sticky="w", pady=5)
        #canvas.grid(row=6, column=0, columnspan=2, pady=10)


    
