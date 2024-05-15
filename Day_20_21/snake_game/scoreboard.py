from turtle import Turtle

FONT = ("Courier", 24, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.sety(270)
        self.write(f"Score: {self.score}".upper(), align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}".upper(), align=ALIGNMENT, font=FONT)
