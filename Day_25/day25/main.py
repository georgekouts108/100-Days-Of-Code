import pandas
import pandas as pd
from turtle import Turtle, Screen
import csv

FONT = ("Arial", 10, 'normal')
ALIGNMENT = "center"

data = pd.read_csv('50_states.csv')
states = {}
state_names = list(data.get('state'))
state_xcors = list(data.get('x'))
state_ycors = list(data.get('y'))
for s in range(len(data)):
    state, x, y = (state_names[s], state_xcors[s], state_ycors[s])
    states[state] = (x, y)

screen = Screen()
screen.setup(width=725, height=491)
screen.title('US States Game')
screen.bgpic('blank_states_img.gif')
screen.tracer(0)

correct_states = 0
state_names_remaining = state_names
state_marks = []

while correct_states < 50:
    guessed_state = screen.textinput(f'{correct_states}/50 States Correct', "What's another state name?").title()

    if guessed_state.lower() == 'exit':
        new_data = pandas.DataFrame(state_names_remaining)
        new_data.to_csv('states_to_learn.csv')
        break

    if len(guessed_state) == 0:
        pass

    elif guessed_state in state_names_remaining:
        correct_states += 1
        state_names_remaining.remove(guessed_state)

        state_name = Turtle()
        state_name.penup()
        state_name.color('green')
        state_name.goto(states[guessed_state])
        state_name.write(guessed_state, align=ALIGNMENT, font=FONT)


screen.exitonclick()

