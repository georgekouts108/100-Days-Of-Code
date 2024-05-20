from turtle import Turtle
from random import *

FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.goto(-100, 200)
        self.write(self.score1, align='center', font=FONT)
        self.goto(100, 200)
        self.write(self.score2, align='center', font=FONT)

    def increment(self, side):
        if side == 1:
            self.score1 += 1
        elif side == 2:
            self.score2 += 1

        self.clear()
        self.goto(-100, 200)
        self.write(self.score1, align='center', font=FONT)
        self.goto(100, 200)
        self.write(self.score2, align='center', font=FONT)


class Net:
    def __init__(self):
        self.segments = []
        x, y = (0, 275)
        for _ in range(19):
            tt = Turtle('square')
            tt.speed('fastest')
            tt.penup()
            tt.color('white')
            tt.shapesize(stretch_wid=1, stretch_len=0.5)
            tt.setx(x)
            tt.sety(y)
            y -= 30
            self.segments.append(tt)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ball_speed = 0.1
        self.color('white')
        self.shape('circle')
        self.setheading(choice([30, 150, 210, 330]))

    def reset(self):
        self.setx(0)
        self.sety(0)

        quad1 = 0 <= self.heading() < 90
        quad2 = 90 <= self.heading() < 180
        quad3 = 180 <= self.heading() < 270
        quad4 = 270 <= self.heading() < 360

        if quad1 or quad4:
            self.setheading(choice([150, 210]))
        elif quad2 or quad3:
            self.setheading(choice([30, 330]))

        self.ball_speed = 0.1

    def bounce_off_ceiling(self):
        angle = self.heading()
        new_angle = 0

        if 0 < angle < 90:
            new_angle = 360 - angle

        elif 90 < angle < 180:
            new_angle = angle + (2 * (180 - angle))

        self.setheading(new_angle)

    def bounce_off_floor(self):
        angle = self.heading()
        new_angle = 0

        if 270 < angle < 360:
            new_angle = (360 - angle)

        elif 180 < angle < 270:
            new_angle = 360 - angle

        self.setheading(new_angle)

    def bounce_off_paddle1(self):
        angle = self.heading()
        new_angle = 0

        if 180 < angle < 270:
            new_angle = 540 - angle

        elif 90 < angle < 180:
            new_angle = 180 - angle

        elif angle == 180:
            new_angle = 0

        self.setheading(new_angle)

    def bounce_off_paddle2(self):
        angle = self.heading()
        new_angle = 0

        if 270 < angle < 360:
            new_angle = 540 - angle

        elif 0 < angle < 90:
            new_angle = 180 - angle

        elif angle == 0:
            new_angle = 180

        self.setheading(new_angle)

    def is_on_ceil_or_floor(self):
        ceiling = self.ycor() > 280 and (-400 <= self.xcor() <= 400)
        floor = self.ycor() < -280 and (-400 <= self.xcor() <= 400)

        if ceiling:
            return 1
        if floor:
            return 0

        return -1

    def passed_paddle(self):
        if self.xcor() < -400 and (-280 <= self.ycor() <= 280):
            return 1
        if self.xcor() > 400 and (-280 <= self.ycor() <= 280):
            return 2

        return 0

    def touched_paddle(self, paddle):
        for p in paddle.units:
            if self.distance(p.xcor(), p.ycor()) < 30:
                return True

        return False

    def move(self):
        self.forward(20)


class Paddle:
    def __init__(self, player_num):
        self.player_num = player_num
        self.x = 350 * (-1 if player_num == 1 else 1)

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
        if max([seg.ycor() for seg in self.units]) < 280:
            for seg in self.units:
                seg.sety(seg.ycor() + 20)

    def move_down(self):
        if min([seg.ycor() for seg in self.units]) > -280:
            for seg in self.units:
                seg.sety(seg.ycor() - 20)
