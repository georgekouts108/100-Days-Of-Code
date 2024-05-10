from turtle import Turtle, Screen

default_turtle = Turtle()
default_turtle.shape('turtle')
default_turtle.color('green')
default_turtle.pencolor('black')

# CHALLENGE 2 - draw a dashed line
default_turtle.penup()
default_turtle.setx(-300)
default_turtle.pendown()

for _ in range(20):
    default_turtle.forward(10)
    default_turtle.penup()
    default_turtle.forward(20)
    default_turtle.pendown()

screen = Screen()
screen.title("Finished")
screen.exitonclick()