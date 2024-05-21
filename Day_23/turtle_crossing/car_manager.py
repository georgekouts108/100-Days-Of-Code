from turtle import Turtle
from random import *

COLORS = ['#f25149', '#00eaff', '#c662f5', '#ff8cf4', '#62f56c', '#f5cb62', '#ff0062']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

MAX_Y = 230
MIN_Y = -250
START_X = 310


class Car(Turtle):
    def __init__(self, car_id, move_dist):
        super().__init__()
        self.penup()
        self.color(choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.y = randint(MIN_Y, MAX_Y)
        self.x = START_X
        self.goto((self.x, self.y))
        self.move_distance = move_dist
        self.id = car_id

    def move(self):
        self.x -= self.move_distance
        self.setx(self.x)


class CarManager:
    CAR_ID = 0
    MOVE_DISTANCE = STARTING_MOVE_DISTANCE

    def __init__(self):
        self.cars = []

    def collision_occurred(self, player):
        for car in self.cars:
            if car.distance(player.xcor(), player.ycor()) <= 20:
                return True

        return False

    def add_car(self):
        self.CAR_ID += 1
        new_car = Car(self.CAR_ID, move_dist=self.MOVE_DISTANCE)
        self.cars.append(new_car)

    def remove_car(self, _car):
        for car in self.cars:
            if car.id == _car.id:
                self.cars.remove(car)
                break

    def move_cars(self):
        for car in self.cars:
            car.move()

    def remove_off_screen_cars(self):
        for car in self.cars:
            if car.xcor() <= -330:
                self.cars.remove(car)

    def speed_up_cars(self):
        self.MOVE_DISTANCE += MOVE_INCREMENT
        for car in self.cars:
            car.move_distance = self.MOVE_DISTANCE
