from tkinter import *
# from word import Words


class SetupScreen():
    def __init__(self, window):
        self.window = window
        self.window.config(padx=50, pady=50)
        self.window.title("Typing speed test")
        canvas = Canvas(width=200, height=200, highlightthickness=0)
        canvas.grid(row=0, column=1)
        self.add_items_to_scren()

    def add_items_to_scren(self):
        # Add title
        website_label = Label(text="Typing test: ", font=("Arial", 20), justify='left')
        website_label.grid(column=1, row=0)

        # Start list
        words_list = Label(text="one, two, three, words")
        words_list.grid(column=1, row=1)

        # title for input
        password_label = Label(text="Enter your words here: ", font=("Arial", 10))
        password_label.grid(column=0, row=3)

        # add input field
        words_field = Entry(width=21)
        words_field.grid(column=1, row=3, sticky="EW")