from tkinter import *

from tkinter import messagebox
import random
import json

#Setup
window = Tk()
window.config(padx=50, pady=50)
window.title("Typing speed test")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=1)

# 1. ToDo Setup the screen
website_label = Label(text="Website: ", font=("Arial", 10), justify='left')
website_label.grid(column=0, row=1)

# 2. Todo Allow user input


# 3. ToDo Call word class and compare user input to current word, if same add point and next word


# 4. ToDo on space check if word matches else


# 5. ToDo keep score

window.mainloop()
