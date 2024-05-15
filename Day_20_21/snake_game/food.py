from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color('cyan')
        self.speed('fastest')
        self.go_to_random_location()

    def go_to_random_location(self):
        x, y = (randint(-280, 280), randint(-280, 250))
        self.goto(x, y)

