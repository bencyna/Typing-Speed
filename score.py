import time


class Score():
    def __init__(self):
        self.score = 0
        self.countdown = time.time()

    def add_to_score(self):
        self.score += 1

    def high_score(self):
        pass;

    def cont_countdown(self):
        if time.time() - self.countdown > 60:
            print(self.score)
            print(time.time() - self.countdown)
            return True
        else:
            return False

