import tkinter as tk
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
SNAKE_SPEED = 150
SPACE_SIZE = 20
SNAKE_BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.square = self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body_size = SNAKE_BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, SNAKE_BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class SnakeGame:
    def __init__(self, root, hub):
        self.root = root
        self.hub = hub
        self.root.title("Snake")

        self.score = 0
        self.direction = 'down'

        self.canvas = tk.Canvas(self.root, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.canvas.pack()

        self.root.bind('<Left>', lambda event: self.change_direction('left'))
        self.root.bind('<Right>', lambda event: self.change_direction('right'))
        self.root.bind('<Up>', lambda event: self.change_direction('up'))
        self.root.bind('<Down>', lambda event: self.change_direction('down'))

        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=('consolas', 20))
        self.score_label.pack()

        self.next_turn()

    def next_turn(self):
        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        self.snake.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.snake.squares.insert(0, square)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.delete("food")
            self.food = Food(self.canvas)
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions():
            self.game_over()
        else:
            self.next_turn_id = self.root.after(SNAKE_SPEED, self.next_turn)

    def change_direction(self, new_direction):
        if new_direction == 'left':
            if self.direction != 'right':
                self.direction = new_direction
        elif new_direction == 'right':
            if self.direction != 'left':
                self.direction = new_direction
        elif new_direction == 'up':
            if self.direction != 'down':
                self.direction = new_direction
        elif new_direction == 'down':
            if self.direction != 'up':
                self.direction = new_direction

    def check_collisions(self):
        x, y = self.snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH:
            return True
        if y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2,
                               font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
        self.score_label.config(text=f"Final Score: {self.score}")
        # Add a button to go back to the hub
        back_button = tk.Button(self.canvas, text="Back to Hub", font=('consolas', 20),
                                command=self.hub.show_main_menu)
        self.canvas.create_window(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2 + 100, window=back_button)

    def destroy(self):
        self.root.unbind('<Left>')
        self.root.unbind('<Right>')
        self.root.unbind('<Up>')
        self.root.unbind('<Down>')
        # Stop the game loop
        self.root.after_cancel(self.next_turn_id)
