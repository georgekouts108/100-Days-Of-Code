from turtle import Turtle, Screen
from random import randint,choice

# CHALLENGE 4 - generate random walk
def random_color():
    col = "#"
    for _ in range(6):
        col += hex(randint(0, 15))[2:]
    return col

def spirograph(turtle, circle_count):
    for _ in range(circle_count):
        turtle.pencolor(random_color())  # random color
        turtle.circle(100)
        turtle.left(5)

default_turtle = Turtle()
default_turtle.shape('turtle')
default_turtle.color('green')
default_turtle.speed(0.5)

spirograph(default_turtle, 100)

screen = Screen()
screen.title("Finished")
screen.exitonclick()