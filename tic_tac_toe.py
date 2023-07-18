import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_board_gui()

    def create_board_gui(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 20),
                    width=6,
                    height=3,
                    command=lambda row=row, col=col: self.make_move(row, col)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_win():
                self.game_over()
            elif self.check_tie():
                self.game_over(tie=True)
            else:
                self.toggle_player()

    def check_win(self):
        lines = (
            self.board[0],  # Rows
            self.board[1],
            self.board[2],
            [self.board[0][0], self.board[1][0], self.board[2][0]],  # Columns
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],  # Diagonals
            [self.board[0][2], self.board[1][1], self.board[2][0]]
        )

        for line in lines:
            if line[0] == line[1] == line[2] != "":
                return True

        return False

    def check_tie(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def game_over(self, tie=False):
        message = ""
        if tie:
            message = "It's a tie!"
        else:
            message = f"Player {self.current_player} wins!"

        messagebox.showinfo("Game Over", message)
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToeGame()
    game.run()
