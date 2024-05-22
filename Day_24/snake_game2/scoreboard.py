from turtle import Turtle

FONT = ("Courier", 24, 'normal')
ALIGNMENT = "center"


def update_high_score(new_hi_score):
    hs_file = open(file='high_score.txt', mode='w')
    hs_file.write(str(new_hi_score))
    hs_file.close()


def get_high_score():
    hs_file = open(file='high_score.txt', mode='r')
    hs = int(hs_file.read())
    hs_file.close()

    return hs


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = get_high_score()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.sety(270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()

        if self.score > self.high_score:
            self.high_score = self.score
            update_high_score(self.high_score)
        self.score = 0

        self.sety(270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

