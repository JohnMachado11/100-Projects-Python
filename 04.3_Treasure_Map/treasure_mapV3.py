def map_creation():
    print()
    row1 = ["-","-","-"]
    row2 = ["-","-","-"]
    row3 = ["-","-","-"]
    position_list = [11,12,13,21,22,23,31,32,33]
    print("       Col1 Col2 Col3")
    map = [row1, row2, row3]
    print(f" Row1 {map[0]}\n Row2 {map[1]}\n Row3 {map[2]}")
    map_input(map, position_list)

def map_input(map, position_list):
    try:
        position = int(input(" Where do you want to put the treasure? Type in a 2 digit number from 1-3. Indicate ROW then COLUMN. E.g. 12, 33, etc. "))
    except ValueError:
        print('''\n
            Please only respond with a 2 digit number from 1-3. 
            E.g. 12, 33, etc.
            ''')
        map_creation()
    else:
        if position in position_list:
            num = [int(i) for i in str(position)]
            row = num[0] - 1
            col = num[1] - 1
            map[row][col] = "X"
            map_layout(map)
        else:
            print('''\n
                Please only respond with a 2 digit number from 1-3. 
                E.g. 12, 33, etc.
                \n''')
            map_creation()

def map_layout(map):
    print()
    print(f"{map[0]}\n{map[1]}\n{map[2]}")

map_creation()
