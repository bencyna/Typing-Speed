import pandas
import random
from screen_setup import SetupScreen


class Words(SetupScreen):
    def __init__(self):
        data = pandas.read_csv("./assets/csv/words.csv")
        for word in data['view']:
            print(word)


    def new_words(self):
        pass;

    def old_words(self):
        pass;

    def create_input(self):
        pass;
