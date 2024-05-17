from utils import *
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1300, height=800)
screen.bgcolor('black')
screen.title('Pong')

net = Net()

paddle1 = Paddle(1)
paddle2 = Paddle(2)

#ng1 = NumberGraphic(0, 1)
#ng2 = NumberGraphic(0, 2)

ball = Ball()

screen.listen()
screen.onkey(paddle1.move_up, paddle1.up_key)
screen.onkey(paddle1.move_down, paddle1.down_key)
screen.onkey(paddle2.move_up, paddle2.up_key)
screen.onkey(paddle2.move_down, paddle2.down_key)




screen.exitonclick()