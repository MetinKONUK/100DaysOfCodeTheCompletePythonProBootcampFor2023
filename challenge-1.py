#functions from Reeborg's World library
def move():pass
def turn_left():pass

def turn_right():
    for _ in range(0, 3):
        turn_left()
def draw_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
draw_square()
