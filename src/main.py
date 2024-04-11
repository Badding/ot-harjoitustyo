import customtkinter as ctk
from ui.ui import UI

def main():
    window = ctk.CTk()
    window.title("Poker Squares")

    ui = UI(window)
    ui.run()
    window.mainloop()

if __name__ == '__main__':
    main()
