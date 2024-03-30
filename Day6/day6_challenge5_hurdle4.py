def turn_right():
    turn_left()
    turn_left()
    turn_left()

def top_of_wall_reached():
    turn_right()
    return not wall_in_front()

def climb():
    turn_left()
    while not top_of_wall_reached():
        turn_left()
        move()
    move()
    
def go_down():
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

def jump():
    climb()
    go_down()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
