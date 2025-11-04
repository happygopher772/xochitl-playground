import math
import random
import secrets
import tkinter as tk
import time
import simpleaudio as sa

#symbols = ["🍒","🍋","7️⃣","💎","💀"]

generalTickSound = sa.WaveObject.from_wave_file("general_spin_sound.wav")
generalWinningSound = sa.WaveObject.from_wave_file("general_win_sound.wav")
usagiDinner = sa.WaveObject.from_wave_file("winner_winner_chicken_dinner.wav")

root = tk.Tk()
root.title("Gamble Gambler 9000")

spinDisplay = tk.Label(root)
spinDisplay.pack()

label = tk.Label(root, text="Spin me baby, go ahead, I won't bite...")
label.pack()


loot =\
[
    {"item": "ちいかわ", "weight": 35, "id": 1, "icon": "chii.png"},
    {"item": "ハチワレ", "weight": 35, "id": 2, "icon": "hawa.png"},
    {"item": "大人ボビー", "weight": 20, "id": 3, "icon": "bobbysan.png"},
    {"item": "ミツ星", "weight": 9, "id": 4, "icon": "3stars.png"},
    {"item": "うさぎ", "weight": 1, "id": 5, "icon": "usagiii!!.png"},
]

evil_loot =\
[
    {"item": "ちいかわ", "weight": 10, "id": 1, "icon": "chii.png"},
    {"item": "ハチワレ", "weight": 10, "id": 2, "icon": "hawa.png"},
    {"item": "大人ボビー", "weight": 50, "id": 3, "icon": "bobbysan.png"},
    {"item": "ミツ星", "weight": 15, "id": 4, "icon": "3stars.png"},
    {"item": "うさぎ", "weight": 15, "id": 5, "icon": "usagiii!!.png"},
]

def update_label(new):
    img = tk.PhotoImage(file = new)
    spinDisplay.config(image = img)

    #tinker uses python memeory managment, which deletes unrefrenced objects automatically...
    spinDisplay.image = img
    root.update()
    time.sleep(0.2)
"""""
    if play_tick:
        try:
            generalTickSound.play()
        except:
            pass
"""


def gamble_roller():
    button.config(state="disabled")
    box_1 = []
    total = 0
    roll = 0
    current = 0
    nonWinnings = ""
    winnings = ""

    for i in range(49):
        current = 0
        total = sum(item["weight"] for item in evil_loot)
        roll = secrets.randbelow(total)
        for item in evil_loot:
            current += item["weight"]
            if roll < current:
                nonWinnings = item["icon"]
                break

        box_1.append(nonWinnings)

    current = 0
    total = sum(item["weight"] for item in loot)
    roll = secrets.randbelow(total)

    for item in loot:
        current+= item["weight"]
        if roll < current:
            winnings = item["icon"]
            box_1.append(winnings)
            break

    for i in range(50):
        update_label(box_1[i])
    if box_1[49] == "usagiii!!.png":
        usagiDinner.play()
    else:
        generalWinningSound.play()

    box_1.clear()
    button.config(state="normal")

button = tk.Button(root, text="Click me to gamble!", command=gamble_roller)
button.pack()

root.mainloop()







