#functions from Reeborg's World library
def move():pass
def turn_left():pass

def turn_right():
    for _ in range(0, 3):
        turn_left()
        
def turn_move(side):
    if side:
        move()
        turn_right()
    else:
        move()
        turn_left()
        
def hurdle():
    turn_move(0)
    turn_move(1)
    turn_move(1)
    turn_move(0)
    
for _ in range(0, 6):
    hurdle()