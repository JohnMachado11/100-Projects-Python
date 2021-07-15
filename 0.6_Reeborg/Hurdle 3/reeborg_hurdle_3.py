#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def main():
    wall_check()
            
def wall_check():
    goal_check()
    if wall_in_front():
        wall_climb()
    else:
        clear_space()
            
def clear_space():
    goal_check()
    while front_is_clear():
        move()
        wall_check()

def goal_check():
    if at_goal():
        print("I made it!")
        done()
    else:
        return

def wall_climb():
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        wall_check()
        
main()

# Angela Yu's Solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()