from turtle import Turtle, Screen
from random import randint,choice

# CHALLENGE 4 - generate random walk
def random_color():
    col = "#"
    for _ in range(6):
        col += hex(randint(0, 15))[2:]
    return col

def random_walk(turtle, displacements):
    for _ in range(displacements):
        turtle.pencolor(random_color()) # random color
        turtle.rt(choice([0, 90, 180, 270])) # random direction
        turtle.forward(50)

default_turtle = Turtle()
default_turtle.shape('turtle')
default_turtle.color('green')
default_turtle.pensize(20)

random_walk(default_turtle, 50)

screen = Screen()
screen.title("Finished")
screen.exitonclick()