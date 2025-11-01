import math
import random
import secrets
import tkinter as tk

#symbols = ["🍒","🍋","7️⃣","💎","💀"]

root = tk.Tk()
root.title("Gamble Gambler 9000")

label = tk.Label(root, text="Spin me baby, go ahead, I won't bite...")
label.pack()

def update_label(new):
    label.config(text=new)
def gamble_roller():
    gamble_roll = secrets.randbelow(1000000)
    prize = "Nothing"

    if gamble_roll < 900000:
        prize = "Nothing"
    elif 900000 <= gamble_roll <= 980000:
        prize = "50 Cents"
    elif 980000 <= gamble_roll <= 990000:
        prize = "20 Bucks"
    elif 990000 <= gamble_roll <= 995000:
        prize = "50 Bucks"
    elif 995000 <= gamble_roll <= 999998:
        prize = "100 Bucks"
    elif gamble_roll == 999999:
        prize = "Gold Gold Gold Gold"

    update_label(prize)

button = tk.Button(root, text="Click me to gamble!", command=gamble_roller)
button.pack()

root.mainloop()







