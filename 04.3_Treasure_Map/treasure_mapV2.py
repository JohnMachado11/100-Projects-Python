# WORK IN PROGRESS. TRYING TO MAKE USE OF A HASHTABLE. 
# HAVING ISSUES RELATED TO LOGIC AND GETTING THE VALUE FROM
# THE HASHTABLE THATS INDICATED BY THE USER 
# TO MAP TO THE EXACT INDEX IN THE LIST CALLED "MAP" THEN
# CHANGE THAT map[][] INDEX VALUE TO = X

import sys

def map_creation():
    print()
    row1 = ["1","2","3"]
    row2 = ["4","5","6"]
    row3 = ["7","8","9"]
    print("       Col1 Col2 Col3")
    map = [row1, row2, row3]
    print(f" Row1 {map[0]}\n Row2 {map[1]}\n Row3 {map[2]}")
    map_spots = {"11": map[0][0], "12": map[0][1], "13": map[0][2], 
                "21": map[1][0], "22": map[1][1], "23": map[1][2], 
                "31": map[2][0], "32": map[2][1], "33": map[2][2]}
    map_input(map, map_spots)

def map_input(map, map_spots):
    try:
        position = int(input(" Where do you want to put the treasure? Type in a 2 digit number from 1-3. Indicate ROW then COLUMN. E.g. 12, 33, etc. "))
    except ValueError:
        print('''\n
            Please only respond with a 2 digit number from 1-3. 
            E.g. 12, 33, etc.
            ''')
        map_creation()
    else:
        if str(position) in map_spots: # <-- This check works
            #map[][] = map_spots[p]
            map[][] = map_spots[str(position)]
            #map[] # <-- Placeholder
            #print(map_spots[str(position)]) # <-- Placeholder
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
    # sys.exit()

map_creation()



# voted = {}
# def check_voter(name):
#     if voted.get(name):
#         print("kick them out!")
#     else:
#         voted[name] = True
#         print("let them vote!")

# check_voter("tom")
# check_voter("mike")
# check_voter("mike")


# map_spots = {"11": 11, "12": 12, "13": 13, "21": 21, "22": 22, "23": 23, "31": 31, "32": 32, "33": 33}
# print(map_spots["11"])
