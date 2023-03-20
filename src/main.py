import tkinter as tk
from game import Game
from SOSGameUI import SOSGameUI

def main():
    root = tk.Tk()
    game = Game(3, 'simple', 'human', 'ai')
    app = SOSGameUI(root, game)
    app.mainloop()

if __name__ == "__main__":
    main()
