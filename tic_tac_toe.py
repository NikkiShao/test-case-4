import tkinter as tk
from tkinter import font
import random

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.colors = {
            "bg": "#282c34",
            "text": "#ffffff",
            "button": "#61afef",
            "button_active": "#c678dd",
            "player_x": "#e06c75",
            "player_o": "#98c379",
            "grid": "#3b4048",
        }
        self.root.config(bg=self.colors['bg'])
        self.game_mode = None
        self.widgets = {}
        self.create_mode_selection_widgets()

    def create_mode_selection_widgets(self):
        self.clear_widgets()
        mode_frame = tk.Frame(self.root, bg=self.colors['bg'])
        mode_frame.pack(pady=20, expand=True)
        self.widgets['mode_frame'] = mode_frame

        sp_button = tk.Button(
            mode_frame,
            text="Single Player",
            font=font.Font(size=16),
            bg=self.colors['button'],
            fg=self.colors['text'],
            activebackground=self.colors['button_active'],
            activeforeground=self.colors['text'],
            width=15,
            command=lambda: self.start_game('single')
        )
        sp_button.pack(pady=10)
        self.widgets['sp_button'] = sp_button

        tp_button = tk.Button(
            mode_frame,
            text="Two Player",
            font=font.Font(size=16),
            bg=self.colors['button'],
            fg=self.colors['text'],
            activebackground=self.colors['button_active'],
            activeforeground=self.colors['text'],
            width=15,
            command=lambda: self.start_game('two')
        )
        tp_button.pack(pady=10)
        self.widgets['tp_button'] = tp_button

    def start_game(self, mode):
        self.game_mode = mode
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_game_widgets()
        self.update_status_label()
        self.enable_board()

    def create_game_widgets(self):
        self.clear_widgets()
        board_frame = tk.Frame(self.root, bg=self.colors['bg'])
        board_frame.pack()
        self.widgets['board_frame'] = board_frame

        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    board_frame,
                    text="",
                    font=font.Font(size=24, weight="bold"),
                    width=5,
                    height=2,
                    bg=self.colors['grid'],
                    fg=self.colors['text'],
                    activebackground=self.colors['button_active'],
                    activeforeground=self.colors['text'],
                    command=lambda r=row, c=col: self.on_button_click(r, c),
                )
                button.grid(row=row, column=col, padx=2, pady=2)
                self.buttons[row][col] = button

        status_label = tk.Label(
            self.root,
            text="Player X's turn",
            font=font.Font(size=16),
            bg=self.colors['bg'],
            fg=self.colors['text'],
        )
        status_label.pack(pady=10)
        self.widgets['status_label'] = status_label

        reset_button = tk.Button(
            self.root,
            text="Reset",
            font=font.Font(size=16),
            bg=self.colors['button'],
            fg=self.colors['text'],
            activebackground=self.colors['button_active'],
            activeforeground=self.colors['text'],
            command=self.reset_game,
        )
        reset_button.pack(pady=10)
        self.widgets['reset_button'] = reset_button

    def clear_widgets(self):
        for widget in self.widgets.values():
            widget.destroy()
        self.widgets = {}

    def reset_game(self):
        self.create_mode_selection_widgets()

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            player_color = self.colors['player_x'] if self.current_player == 'X' else self.colors['player_o']
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, fg=player_color, state=tk.DISABLED)

            winner = self.check_winner()
            if winner:
                self.end_game(winner)
                return

            # Switch player
            self.current_player = "O" if self.current_player == "X" else "X"
            self.update_status_label()

            if self.game_mode == 'single' and self.current_player == 'O':
                self.disable_board()
                self.root.after(500, self.computer_move)
            else:
                # In two-player mode, or when it becomes the human's turn in single-player
                self.enable_board()

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

        self.disable_board()

    def computer_move(self):
        empty_cells = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    empty_cells.append((r, c))

        if empty_cells:
            row, col = random.choice(empty_cells)
            self.on_button_click(row, col)

    def disable_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

    def enable_board(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    self.buttons[row][col].config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
