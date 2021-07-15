# Johns Solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def climb():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while at_goal() != True:
    if front_is_clear():
        move()
    else:
        climb()


# Angela Solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def spin():
    turn_right()
    move()
    turn_right()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    spin()
    while front_is_clear():
        move()
    turn_left()

while at_goal() != True:
    if front_is_clear():
       move()
    else:
        jump()