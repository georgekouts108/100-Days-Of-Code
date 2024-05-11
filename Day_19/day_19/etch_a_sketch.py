from turtle import *

marker = Turtle()
screen = Screen()
screen.listen()


def clear_screen():
    marker.penup()
    marker.clear()
    marker.setx(0)
    marker.sety(0)
    marker.pendown()
    marker.setheading(0)


def forwards():
    marker.forward(20)


def backwards():
    marker.backward(20)


def rotate_ccw():
    marker.setheading(marker.heading() + 10)


def rotate_cw():
    marker.setheading(marker.heading() - 10)


screen.onkey(fun=forwards, key='w')
screen.onkey(fun=backwards, key='s')
screen.onkey(fun=rotate_ccw, key='a')
screen.onkey(fun=rotate_cw, key='d')
screen.onkey(fun=clear_screen, key='c')

screen.exitonclick()
