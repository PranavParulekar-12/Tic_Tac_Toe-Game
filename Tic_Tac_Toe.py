import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    for i in range(3):
    
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "" or \
           buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
            reset_game()
            return

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "" or \
       buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
        reset_game()
        return

    if all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        reset_game()

def button_click(row, col):
    global player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player
        check_winner()
        player = "O" if player == "X" else "X"

def reset_game():
    global player
    player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()