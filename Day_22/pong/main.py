from utils import *
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=1300, height=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

net = Net()
ball = Ball()
paddle1 = Paddle(1)
paddle2 = Paddle(2)

ng1 = NumberGraphic(0, 1)
ng2 = NumberGraphic(0, 2)

screen.listen()
screen.onkey(paddle1.move_up, paddle1.up_key)
screen.onkey(paddle1.move_down, paddle1.down_key)
screen.onkey(paddle2.move_up, paddle2.up_key)
screen.onkey(paddle2.move_down, paddle2.down_key)

game_on = True
P1_SCORE = 0
P2_SCORE = 0

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    cof = ball.is_on_ceil_or_floor()
    if cof == 1:
        ball.bounce_off_ceiling()

    if cof == 0:
        ball.bounce_off_floor()

    if ball.touched_paddle(paddle1):
        P1_SCORE += 1
        ball.bounce_off_paddle1()
        ng1 = NumberGraphic(P1_SCORE, 1)

    if ball.touched_paddle(paddle2):
        P2_SCORE += 1
        ball.bounce_off_paddle2()
        ng2 = NumberGraphic(P2_SCORE, 2)

    paddle_passed = ball.passed_paddle()
    if paddle_passed != 0:
        print(f"WINNER = Player {1 if paddle_passed == 2 else 2}")
        game_on = False

screen.exitonclick()
