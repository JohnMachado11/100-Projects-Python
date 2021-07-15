import sys

def map_creation():
    print()
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    print("       Col 1  Col 2  Col 3")
    map = [row1, row2, row3]
    print(f" Row 1 {map[0]}\n Row 2 {map[1]}\n Row 3 {map[2]}")
    map_designation(map)

def map_designation(map):
    try:
        position = int(input(" Where do you want to put the treasure? Type in a 2 digit number from 1-3. Indicate ROW then COLUMN. E.g. 12, 33, etc. "))
    except ValueError:
        print('''\n
            Please only respond with a 2 digit number from 1-3. 
            E.g. 12, 33, etc.
            ''')
        map_creation()
    else:
        if position == 11:
            map[0][0] = "X"
        elif position == 12:
            map[0][1] = "X"
        elif position == 13:
            map[0][2] = "X"
        elif position == 21:
            map[1][0] = "X"
        elif position == 22:
            map[1][1] = "X"
        elif position == 23:
            map[1][2] = "X"
        elif position == 31:
            map[2][0] = "X"
        elif position == 32:
            map[2][1] = "X"
        elif position == 33:
            map[2][2] = "X"
        else:
            print('''\n
                Please only respond with a 2 digit number from 1-3. 
                E.g. 12, 33, etc.
                \n''')
            map_creation()
    map_layout(map)

def map_layout(map):
    print()
    print(f"{map[0]}\n{map[1]}\n{map[2]}")
    sys.exit()

map_creation()