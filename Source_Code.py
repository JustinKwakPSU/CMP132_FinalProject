import tkinter as tk
import random

class PlinkoGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Plinko Game")

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.plinko_board = PlinkoBoard(self.canvas)

        self.ball_radius = 10
        self.ball = self.canvas.create_oval(195, 10, 205, 20, fill="red")

        self.start_button = tk.Button(self.master, text="Start Plinko", command=self.start_plinko)
        self.start_button.pack()

    def start_plinko(self):
        column = random.randint(0, PlinkoBoard.num_columns - 1)
        initial_x = PlinkoBoard.column_width * column + PlinkoBoard.column_width // 2
        initial_y = 30

        final_column = self.animate_ball(initial_x, initial_y)
        value = PlinkoBoard.get_column_value(final_column)
        print(f"The ball landed in column {final_column} with a value of {value}")

    def animate_ball(self, x, y):
        target_y = 370
        steps = 50
        step_size = (target_y - y) / steps

        for _ in range(steps):
            self.canvas.move(self.ball, 0, step_size)
            self.master.update()
            self.master.after(20)

        # Determine the final column where the ball landed
        final_coords = self.canvas.coords(self.ball)
        final_x = (final_coords[0] + final_coords[2]) / 2  # Calculate the average x coordinate

        final_column = int(final_x / PlinkoBoard.column_width)

        # Reset the ball to the top for the next run
        self.canvas.coords(self.ball, x - self.ball_radius, 10, x + self.ball_radius, 20)

        return final_column

class PlinkoBoard:
    num_columns = 7
    column_width = 400 // num_columns

    @staticmethod
    def get_column_value(column):
        # Assign values to each column (you can customize these values)
        # Also I just made these like the score amount but we can change it to $ if we want
        column_values = [100, 200, 300, 400, 500, 600, 700]
        return column_values[column]

    def __init__(self, canvas):
        self.canvas = canvas
        self.draw_board()

    def draw_board(self):
        for i in range(self.num_columns + 1):
            x = i * self.column_width
            self.canvas.create_line(x, 0, x, 400, fill="black")

# Create the main application window
root = tk.Tk()
plinko_game = PlinkoGame(root)
root.mainloop()


