#functions from Reeborg's World library
def move():pass
def turn_left():pass
def at_goal():pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    hurdle()
