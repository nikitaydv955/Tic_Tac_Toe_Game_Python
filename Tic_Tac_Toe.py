import tkinter as tk
from tkinter import messagebox

# Function to check if someone has won
def check_winner():
    global winner
    # All winning combinations
    for combo in [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight winning buttons
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return

# Function for button click
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

# Switch player turn
def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    if not winner:
        label.config(text=f"Player {current_player}'s turn")

# Main window
root = tk.Tk()
root.title("Tic-Tac-Toe")  # Fixed typo

# Create buttons
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                     command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"
winner = False

# Label to show player turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()