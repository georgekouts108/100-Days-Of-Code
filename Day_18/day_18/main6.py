import colorgram
from turtle import *
from random import choice


def draw_dots(turtle, palette):
    turtle.penup()

    spots_drawn = 0
    while spots_drawn < 100:

        # set position
        if spots_drawn % 10 == 0:
            turtle.setx(-300)
            turtle.sety(-100 + (50 * (spots_drawn // 10)))

        # draw
        turtle.pendown()
        turtle.dot(20, '#{:02x}{:02x}{:02x}'.format(*choice(palette)))
        turtle.penup()
        turtle.forward(50)

        spots_drawn += 1


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)  # extract 30 colors
for color in colors:
    r, g, b = color.rgb
    rgb_colors.append((r, g, b))

print(rgb_colors)

franklin = Turtle()
franklin.shape('turtle')
franklin.speed(2)
franklin.pensize(20)
franklin.hideturtle()
draw_dots(franklin, rgb_colors)

screen = Screen()
screen.title("Finished")
screen.exitonclick()
