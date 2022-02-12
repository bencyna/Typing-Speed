from tkinter import *

from tkinter import messagebox
import random
import json


window = Tk()
window.config(padx=50, pady=50)
window.title("Typing speed test")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=1)

window.mainloop()
