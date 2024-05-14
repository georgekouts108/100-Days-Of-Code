from turtle import *

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN, UP, LEFT, RIGHT = (270, 90, 180, 0)


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        # create initial snake body
        for p in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(p)
            self.body.append(new_segment)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
