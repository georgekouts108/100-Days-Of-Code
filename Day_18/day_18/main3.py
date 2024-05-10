from turtle import Turtle, Screen
from random import randint

# CHALLENGE 3 - drawing different shapes
def random_hex_color():
    col = "#"
    for _ in range(6):
        col += hex(randint(0, 15))[2:]
    return col

def draw_shape(turtle, sides):
    turtle.pencolor(random_hex_color())
    for _ in range(sides):
        turtle.forward(200)
        turtle.left(360 / sides)

default_turtle = Turtle()
default_turtle.shape('turtle')
default_turtle.color('green')

for i in range(3, 11):
    draw_shape(default_turtle, i)

screen = Screen()
screen.title("Finished")
screen.exitonclick()