from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_in_progress = True
while game_in_progress:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.go_to_random_location()
        scoreboard.add_point()
        snake.extend()

    within_x = -280 <= snake.head.xcor() <= 280
    within_y = -280 <= snake.head.ycor() <= 280

    if not (within_x and within_y):
        game_in_progress = False

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_in_progress = False
            break
scoreboard.game_over()
screen.exitonclick()
