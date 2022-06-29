#functions from Reeborg's World library
def move():pass
def turn_left():pass
def at_goal():pass
def wall_in_front():pass
def right_is_clear():pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()