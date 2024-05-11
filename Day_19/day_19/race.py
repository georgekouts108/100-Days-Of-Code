from turtle import *
from random import *

TURTLES = {
    '1': {'color': 'purple', 'y_init': 80},
    '2': {'color': 'blue', 'y_init': 50},
    '3': {'color': 'green', 'y_init': 20},
    '4': {'color': 'yellow', 'y_init': -10},
    '5': {'color': 'orange', 'y_init': -40},
    '6': {'color': 'red', 'y_init': -70}
}


class Contestant:

    def __init__(self, id):
        self.id = id

        self.turtle = Turtle()
        self.turtle.shape('turtle')
        self.turtle.penup()
        self.turtle.color(TURTLES[str(self.id)]['color'])
        self.turtle.setx(-370)
        self.turtle.sety(TURTLES[str(self.id)]['y_init'])

    def run(self):
        self.turtle.forward(randint(1, 10))
        self.turtle.setx(min(float(370), self.turtle.xcor()))

    def reached_end(self):
        return self.turtle.xcor() >= 370.0


screen = Screen()
color_bet = screen.textinput('Make your bet', 'Who will win? (enter a color): ').lower()

contestants = []
for i in range(1, 7):
    c = Contestant(id=i)
    contestants.append(c)

done = False
winning_color = ""
while not done:
    for t in contestants:
        t.run()
        if t.reached_end():
            winning_color = TURTLES[str(t.id)]['color']
            done = True
            break

    if done:
        print(f"{winning_color} turtle won the race!")
        print(f"You {'won' if winning_color.lower() == color_bet.lower() else 'did not win'} the bet!")


screen.exitonclick()
