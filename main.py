from tkinter import *
from words_class import Words
from score import Score
import time

first = True
score = {}

current = ""

# Setup
window = Tk()


def end_game(score):
    score_card =Label(text=f"You got {score.score} words in 60 seconds. Meaning your wpm is  {score.score}", background="#7FDBFF", foreground="#FF851B",font=("Arial", 15),
          justify='left')
    score_card.grid(column=0, row=1)


# 3. ToDo Call word class and compare user input to current word, if same add point and next word
# Show the current words list
def show_words(next_words, current_word):
    global current
    # Start list
    current = current_word

    upcoming_words = " ".join(next_words)
    words_list = Label(text=f"{upcoming_words}", background="#7FDBFF", foreground='white',
                       font=('Times New Roman', 20), wraplength=400)
    words_list.grid(column=0, row=3, sticky="EW")
    current_word_show = Label(text=f"{current_word}", background="#7FDBFF", foreground='red',
                              font=('Times New Roman', 20), wraplength=400)
    current_word_show.grid(column=0, row=2, sticky="EW")


def check_word(answer):
    global first, score
    if first:
        first = False
        score = Score()
        website_label2.destroy()

    done = score.cont_countdown()
    if done:
        end_game(score)
    else:
        typed_word = answer.strip().lower()
        current = Words.words_list[Words.word_num]
        if typed_word == current:
            score.add_to_score()

        words_field.delete(0, END)
        Words.next_word()
        new_words_inner = Words.new_words()
        show_words(new_words_inner[0], new_words_inner[1])


# 1. ToDo Setup the screen
window = window
window.config(padx=80, pady=80, background="#7FDBFF")
window.title("Typing speed test")
canvas = Canvas(width=200, height=200, background="#7FDBFF", highlightthickness=0)
canvas.grid(row=0, column=1)

# Add title
website_label = Label(text="Typing test: ", background="#7FDBFF", font=("Arial", 20), justify='left')
website_label.grid(column=0, row=0)

#add text under
website_label2 = Label(text="The game will start once you finish the first word ", background="#7FDBFF", font=("Arial", 10), justify='left')
website_label2.grid(column=0, row=1)

# 2. Todo Allow user input
# add input field
words_field = Entry(width=21, font=('Times New Roman', 20))
words_field.grid(column=0, row=4, sticky="EW", rowspan=2, padx=5, pady=10, ipady=10)

# Add words to screen
Words = Words()
new_words = Words.new_words()
show_words(new_words[0], new_words[1])

# 4. ToDo on space check if word matches else
words_field.bind("<space>", lambda x: check_word(words_field.get()))

window.mainloop()
