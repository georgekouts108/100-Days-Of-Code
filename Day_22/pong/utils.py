from turtle import Turtle
from random import *

# rows of 3, top to bottom
NUMBERS = {'1': [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
           '2': [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
           '3': [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
           '4': [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
           '5': [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
           '6': [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
           '7': [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
           '8': [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
           '9': [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
           '0': [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
           }


class NumberGraphic:
    def __init__(self, number, player_num):
        self.y_pos = 300
        self.x_limit = 100 * (-1 if player_num == 1 else 1)
        self.player_num = player_num
        self.number = number

        self.display_number()

    def display_number(self):
        digits = []
        numstr = str(self.number)  # ex. '1234'
        x_ref = self.x_limit

        digit_count = 1

        number_iter = range(len(numstr)) if self.player_num == 2 else range(-1, -len(numstr) - 1, -1)

        for ni in number_iter:

            y = self.y_pos
            x = (x_ref * digit_count) - 60

            graphic = []
            code = NUMBERS[numstr[ni]]
            for i in range(15):
                block = Turtle('square')
                block.speed('fastest')
                block.shapesize(stretch_wid=0.5, stretch_len=0.5)
                block.penup()
                block.color('white')
                block.setx(x)
                block.sety(y)
                if code[i] == 0:
                    block.hideturtle()
                graphic.append(block)

                if i in [2, 5, 8, 11]:
                    x, y = (x - 20, y - 10)
                else:
                    x = x + 10

            digits.append(graphic)
            digit_count += 1


class Net:
    def __init__(self):
        self.segments = []
        x, y = (0, 350)
        for _ in range(21):
            tt = Turtle('square')
            tt.speed('fastest')
            tt.penup()
            tt.color('white')
            tt.shapesize(stretch_wid=1, stretch_len=0.5)
            tt.setx(x)
            tt.sety(y)
            y -= 35
            self.segments.append(tt)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('slowest')
        self.color('white')
        self.shape('square')
        self.setheading(choice([30, 150, 210, 330]))

    def bounce(self):
        # bounce on upper horizontal surface (aka ceiling) ?

        # bounce on lower horizontal surface (aka floor) ?

        # bounce on left vertical surface (paddle 1) ?

        # bounce on right vertical surface (paddle 2) ?
        #self.setheading(360 - self.heading())
        pass


class Paddle:
    def __init__(self, player_num):
        self.player_num = player_num
        self.x = 600 * (-1 if player_num == 1 else 1)

        self.up_key = 'w' if player_num == 1 else 'Up'
        self.down_key = 's' if player_num == 1 else 'Down'

        u1 = Turtle()
        u2 = Turtle()
        u3 = Turtle()

        init_y_positions = [-20, 0, 20]
        self.units = [u1, u2, u3]
        for i in range(3):
            self.units[i].speed('fastest')
            self.units[i].penup()
            self.units[i].shape('square')
            self.units[i].color('white')
            self.units[i].sety(init_y_positions[i])
            self.units[i].setx(self.x)

    def move_up(self):
        if max([seg.ycor() for seg in self.units]) < 380:
            print(f"Paddle {self.player_num} moving up")
            for seg in self.units:
                seg.sety(seg.ycor() + 20)

    def move_down(self):
        if min([seg.ycor() for seg in self.units]) > -380:
            print(f"Paddle {self.player_num} moving down")
            for seg in self.units:
                seg.sety(seg.ycor() - 20)
