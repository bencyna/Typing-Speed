import pandas
import random
from screen_setup import SetupScreen


class Words(SetupScreen):
    def __init__(self):
        data = pandas.read_csv("./assets/csv/words.csv")
        self.word_num = 0
        self.upcoming_words = []
        self.words_list = data['view']
        self.new_words()

    def new_words(self):
        self.upcoming_words = self.words_list[self.word_num+1: self.word_num+20]
        self.create_input()

    def old_words(self):
        pass;

    def create_input(self):
        SetupScreen.show_words(1, self.upcoming_words)
