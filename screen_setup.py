from tkinter import *


# from word import Words


class SetupScreen():
    def __init__(self, window):
        self.window = window
        self.window.config(padx=80, pady=80, background="#7FDBFF")
        self.window.title("Typing speed test")
        canvas = Canvas(width=200, height=200, background="#7FDBFF", highlightthickness=0)
        canvas.grid(row=0, column=1)
        self.add_items_to_scren()

    def add_items_to_scren(self):
        # Add title
        website_label = Label(text="Typing test: ", background="#7FDBFF", font=("Arial", 20), justify='left')
        website_label.grid(column=0, row=0)

        # Start list
        words_list = Label(text="one, two, three, words", background="#7FDBFF")
        words_list.grid(column=0, row=1)

        # title for input
        # password_label = Label(text="Enter your words here: ", font=("Arial", 10))
        # password_label.grid(column=0, row=3)

        # add input field
        words_field = Entry(width=21)
        words_field.grid(column=0, row=3, sticky="EW", rowspan=2)
