import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, 'Up')


game_is_on = True
loops = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loops += 1

    if (loops % 6) == 0:
        car_manager.add_car()

    car_manager.move_cars()
    car_manager.remove_off_screen_cars()

    if player.reached_finish_line():
        car_manager.speed_up_cars()
        scoreboard.increment_level()
        player.restart()

    game_is_on = not car_manager.collision_occurred(player)

scoreboard.game_over()

screen.exitonclick()