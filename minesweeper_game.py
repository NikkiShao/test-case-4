import tkinter as tk
from tkinter import font
import random

GRID_SIZE = 10
NUM_MINES = 10

class MinesweeperGame:
    def __init__(self, root, hub):
        self.root = root
        self.hub = hub
        self.root.title("Minesweeper")

        self.buttons = []
        self.mines = set()
        self.flags = set()
        self.revealed = set()
        self.numbers = {}
        self.first_click = True
        self.game_over_flag = False

        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack()

        self.mine_counter_label = tk.Label(self.top_frame, text=f"Mines: {NUM_MINES - len(self.flags)}")
        self.mine_counter_label.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.top_frame, text="Reset", command=self.restart_game)
        self.reset_button.pack(side=tk.RIGHT, padx=10)

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack(pady=10)

        self.create_widgets()

    def restart_game(self):
        self.destroy()
        self.__init__(self.root, self.hub)

    def place_mines(self, first_click_row, first_click_col):
        mine_positions = set()
        while len(mine_positions) < NUM_MINES:
            r = random.randint(0, GRID_SIZE - 1)
            c = random.randint(0, GRID_SIZE - 1)
            if (r, c) != (first_click_row, first_click_col):
                mine_positions.add((r, c))
        self.mines = mine_positions

    def calculate_numbers(self):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if (r, c) in self.mines:
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE and (nr, nc) in self.mines:
                            count += 1
                if count > 0:
                    self.numbers[(r, c)] = count

    def create_widgets(self):
        for r in range(GRID_SIZE):
            row_buttons = []
            for c in range(GRID_SIZE):
                button = tk.Button(
                    self.game_frame,
                    width=2,
                    height=1,
                    command=lambda r=r, c=c: self.on_left_click(r, c)
                )
                button.bind("<Button-3>", lambda event, r=r, c=c: self.on_right_click(r, c))
                button.grid(row=r, column=c)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_left_click(self, row, col):
        if self.game_over_flag or (row, col) in self.revealed:
            return

        if self.first_click:
            self.place_mines(row, col)
            self.calculate_numbers()
            self.first_click = False

        if (row, col) in self.mines:
            self.game_over(won=False)
            return

        self.reveal_cell(row, col)

        # Check for win condition
        if len(self.revealed) == GRID_SIZE * GRID_SIZE - NUM_MINES:
            self.game_over(won=True)

    def reveal_cell(self, row, col):
        if (row, col) in self.revealed or (row, col) in self.flags:
            return

        self.revealed.add((row, col))
        self.buttons[row][col].config(relief=tk.SUNKEN, state=tk.DISABLED)

        if (row, col) in self.numbers:
            self.buttons[row][col].config(text=self.numbers[(row, col)])
        else:
            # It's an empty cell, reveal neighbors
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                        self.reveal_cell(nr, nc)

    def on_right_click(self, event, row, col):
        if self.game_over_flag or (row, col) in self.revealed:
            return

        if (row, col) in self.flags:
            self.flags.remove((row, col))
            self.buttons[row][col].config(text="")
        else:
            self.flags.add((row, col))
            self.buttons[row][col].config(text="🚩")
        self.mine_counter_label.config(text=f"Mines: {NUM_MINES - len(self.flags)}")

    def game_over(self, won):
        self.game_over_flag = True
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                self.buttons[r][c].config(state=tk.DISABLED)
                if (r, c) in self.mines:
                    self.buttons[r][c].config(text="💣")

        message = "You Win!" if won else "You Lose!"
        self.status_label.config(text=message)

    def destroy(self):
        self.top_frame.destroy()
        self.game_frame.destroy()
        self.status_label.destroy()
