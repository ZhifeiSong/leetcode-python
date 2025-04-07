import tkinter as tk
from tkinter import messagebox

# Initialize the game
root = tk.Tk()
root.title("Tic Tac Toe")

# Player turn tracker
current_player = "X"

# Game board
board = [["" for _ in range(3)] for _ in range(3)]

# Function to check for a winner
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

# Function to handle button clicks
def on_click(row, col):
    global current_player

    if board[row][col] == "" and not check_winner():
        # Update board and button
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        # Check if there's a winner
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        elif all(board[i][j] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

# Function to reset the board
def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

# Create buttons for the grid
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), width=3, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

# Start the main loop
root.mainloop()