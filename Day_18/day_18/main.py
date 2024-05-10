from turtle import Turtle, Screen

default_turtle = Turtle()
default_turtle.shape('turtle')
default_turtle.color('green')
default_turtle.pencolor('orange')
default_turtle.speed(2)

# CHALLENGE 1 - draw a square
default_turtle.forward(100)
default_turtle.rt(90)
default_turtle.forward(100)
default_turtle.rt(90)
default_turtle.forward(100)
default_turtle.rt(90)
default_turtle.forward(100)


screen = Screen()
screen.title("Finished")
screen.exitonclick()