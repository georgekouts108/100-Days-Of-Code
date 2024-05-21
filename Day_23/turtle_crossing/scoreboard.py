from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_num = 1
        self.goto(-220, 250)
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)

    def increment_level(self):
        self.level_num += 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level_num}", align='center', font=FONT)
