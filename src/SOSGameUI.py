import tkinter as tk
from board import Board
from game import Game

class SOSGameUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("SOS Game")
        self.game = game
        self.frame = tk.Frame(self)
        self.create_widgets()
        self.frame.pack(fill=tk.BOTH, expand=True)

    def create_widgets(self):
        self.frame.destroy()
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.create_board_buttons()
        self.create_status_label()
        self.create_game_type_checkboxes()
        self.create_board_size_entry()
        self.update_window_size()


    def create_status_label(self):
        self.status_label = tk.Label(self.frame, text="Player 1's Turn")
        self.status_label.grid(row=self.game.board.size, column=0, columnspan=self.game.board.size)

    def create_game_type_checkboxes(self):
        self.game_type = tk.StringVar()
        self.game_type.set("simple")
        simple_game_type_checkbox = tk.Checkbutton(self.frame, text="Simple", variable=self.game_type,
                                                    onvalue="simple", command=self.update_game_type)
        simple_game_type_checkbox.grid(row=self.game.board.size + 2, column=0, padx=5, pady=5, sticky=tk.W)
        general_game_type_checkbox = tk.Checkbutton(self.frame, text="General", variable=self.game_type,
                                                    onvalue="general", command=self.update_game_type)
        general_game_type_checkbox.grid(row=self.game.board.size + 2, column=1, padx=5, pady=5, sticky=tk.W)


    def create_board_size_entry(self):
        self.board_size_label = tk.Label(self.frame, text="Board Size:")
        self.board_size_label.grid(row=self.game.board.size + 1, column=0, sticky=tk.W)
        self.board_size_entry = tk.Entry(self.frame, width=4)
        self.board_size_entry.grid(row=self.game.board.size + 1, column=1)
        self.board_size_entry.insert(0, str(self.game.board.size))

        self.board_size_button = tk.Button(self.frame, text="Update", command=self.update_board_size)
        self.board_size_button.grid(row=self.game.board.size + 1, column=2, padx=5, pady=5, sticky=tk.W)

    def create_board_buttons(self):
        for row in range(self.game.board.size):
            for col in range(self.game.board.size):
                button = tk.Button(self.frame, text=" ", width=6, height=3,
                                command=lambda r=row, c=col: self.button_click(r, c))
                button.grid(row=row, column=col)
        self.status_label = tk.Label(self.frame, text="Player 1's Turn")
        self.status_label.grid(row=self.game.board.size, column=0, columnspan=self.game.board.size)

    def button_click(self, row, col):
        # Implement the logic for handling a button click
        pass

    def update_window_size(self):
        padding = 50
        width = self.game.board.size * 50 + padding
        height = self.game.board.size * 50 + padding + 100
        self.frame.config(width=width, height=height)

    def update_game_type(self):
        new_game_type = self.game_type.get()
        if new_game_type != self.game.game_type:
            self.game.game_type = new_game_type
            print(f"Game type changed to {new_game_type}.")


    def update_board_size(self):
        try:
            new_size = int(self.board_size_entry.get())
            if 3 <= new_size <= 10:
                self.game.board = Board(new_size)
                self.create_widgets()

            else:
                print("Board size must be between 3 and 10.")
        except ValueError:
            print("Invalid board size. Please enter a number between 3 and 10.")


def main():
    game = Game(3, "simple", "human", "ai")
    app = SOSGameUI(game)
    app.mainloop()

if __name__ == "__main__":
    main()
