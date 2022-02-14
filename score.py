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
        print(time.time() - self.countdown )
        print(self.score)

        if time.time() - self.countdown > 10:
            print("FINSIHED BITCJ")
            print(self.score)
            # print(time.time() - self.countdown)
