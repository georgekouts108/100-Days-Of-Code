from utils import *
from turtle import Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

net = Net()
ball = Ball()
paddle1 = Paddle(1)
paddle2 = Paddle(2)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.move_up, paddle1.up_key)
screen.onkey(paddle1.move_down, paddle1.down_key)
screen.onkey(paddle2.move_up, paddle2.up_key)
screen.onkey(paddle2.move_down, paddle2.down_key)


while True:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    cof = ball.is_on_ceil_or_floor()
    if cof == 1:
        ball.bounce_off_ceiling()

    if cof == 0:
        ball.bounce_off_floor()

    if ball.touched_paddle(paddle1):
        ball.bounce_off_paddle1()

    if ball.touched_paddle(paddle2):
        ball.bounce_off_paddle2()

    paddle_passed = ball.passed_paddle()
    if paddle_passed != 0:
        if paddle_passed == 1:
            scoreboard.increment(2)
        elif paddle_passed == 2:
            scoreboard.increment(1)

        ball.reset()
        ball.ball_speed *= 0.9

screen.exitonclick()
