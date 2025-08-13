import tkinter as tk
from tkinter import font
import random

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.game_mode = None
        self.widgets = {}
        self.create_mode_selection_widgets()

    def create_mode_selection_widgets(self):
        self.clear_widgets()
        self.widgets['mode_frame'] = tk.Frame(self.root)
        self.widgets['mode_frame'].pack(pady=20)

        self.widgets['sp_button'] = tk.Button(
            self.widgets['mode_frame'],
            text="Single Player",
            font=font.Font(size=16),
            command=lambda: self.start_game('single')
        )
        self.widgets['sp_button'].pack(pady=10)

        self.widgets['tp_button'] = tk.Button(
            self.widgets['mode_frame'],
            text="Two Player",
            font=font.Font(size=16),
            command=lambda: self.start_game('two')
        )
        self.widgets['tp_button'].pack(pady=10)

    def start_game(self, mode):
        self.game_mode = mode
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_game_widgets()
        self.update_status_label()

    def create_game_widgets(self):
        self.clear_widgets()
        board_frame = tk.Frame(self.root)
        board_frame.pack()
        self.widgets['board_frame'] = board_frame

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

        self.widgets['status_label'] = tk.Label(
            self.root, text="Player X's turn", font=font.Font(size=16)
        )
        self.widgets['status_label'].pack(pady=10)

        self.widgets['reset_button'] = tk.Button(
            self.root, text="Reset", font=font.Font(size=16), command=self.reset_game
        )
        self.widgets['reset_button'].pack(pady=10)

    def clear_widgets(self):
        for widget in self.widgets.values():
            widget.destroy()
        self.widgets = {}

    def reset_game(self):
        self.create_mode_selection_widgets()

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)

            winner = self.check_winner()
            if winner:
                self.end_game(winner)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_status_label()
                if self.game_mode == 'single' and self.current_player == 'O':
                    self.root.after(500, self.computer_move) # Add a small delay for better UX

    def update_status_label(self):
        if self.game_mode == 'single':
            text = "Your turn" if self.current_player == 'X' else "Computer's turn"
        else:
            text = f"Player {self.current_player}'s turn"
        self.widgets['status_label'].config(text=text)

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
            self.widgets['status_label'].config(text="It's a draw!")
        elif self.game_mode == 'single':
            text = "You win!" if winner == 'X' else "Computer wins!"
            self.widgets['status_label'].config(text=text)
        else:
            self.widgets['status_label'].config(text=f"Player {winner} wins!")

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

    def computer_move(self):
        empty_cells = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    empty_cells.append((r, c))

        if empty_cells:
            row, col = random.choice(empty_cells)
            self.on_button_click(row, col)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
