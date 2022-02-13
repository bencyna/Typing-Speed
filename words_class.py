import pandas
import random


class Words():
    def __init__(self):
        data = pandas.read_csv("./assets/csv/words.csv")
        self.word_num = 0
        self.upcoming_words = []
        self.words_list = data['view']

    def next_word(self):
        self.word_num += 1
        self.new_words()

    def new_words(self):
        self.upcoming_words = self.words_list[self.word_num + 1: self.word_num + 20]
        return self.upcoming_words, self.words_list[self.word_num]

    def old_words(self):
        pass;

    def check_word(self, answer):
        typed_word = answer.strip().lower()
        current = self.words_list[self.word_num]
        if typed_word == current:
            print("yes")
