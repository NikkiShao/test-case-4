import tkinter as tk
from tkinter import font

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        board_frame = tk.Frame(self.root)
        board_frame.pack()

        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    board_frame,
                    text="",
                    font=font.Font(size=24, weight="bold"),
                    width=6,
                    height=3,
                    command=lambda r=row, c=col: self.on_button_click(r, c),
                )
                self.buttons[row][col].grid(row=row, column=col)

        self.status_label = tk.Label(
            self.root, text="Player X's turn", font=font.Font(size=16)
        )
        self.status_label.pack(pady=10)

        self.reset_button = tk.Button(
            self.root, text="Reset", font=font.Font(size=16), command=self.reset_game
        )
        self.reset_button.pack(pady=10)

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.status_label.config(text="Player X's turn")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state=tk.NORMAL)

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)

            winner = self.check_winner()
            if winner:
                self.end_game(winner)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        if all(self.board[row][col] != "" for row in range(3) for col in range(3)):
            return "draw"

        return None

    def end_game(self, winner):
        if winner == "draw":
            self.status_label.config(text="It's a draw!")
        else:
            self.status_label.config(text=f"Player {winner} wins!")

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
