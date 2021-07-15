def map_creation():
    row1 = ["O","O","O"]
    row2 = ["O","O","O"]
    row3 = ["O","O","O"]
    map = [row1, row2, row3]
    
    print("\n       Col1 Col2 Col3")
    print(f" Row1 {map[0]}\n Row2 {map[1]}\n Row3 {map[2]}")
    print("\nWhere do you want to put the treasure?\n")
    
    map_input(map)

def map_input(map):
    try:
        row = 0
        column = 0
        
        while row not in range(1,4):
            row = int(input("Which ROW?. Select 1, 2 or 3: "))
            print(f"You selected Row #{row}.\n")
        while column not in range(1,4):
            column = int(input("Which COLUMN? Select 1, 2 or 3: "))
            print(f"You selected Column #{column}.\n")
    
    except ValueError:
        print("\nERROR: Please only respond with 1, 2 or 3.\n")
        map_creation()
    
    else:
        map[row - 1][column - 1] = "X"
        print(f"You selected Row #{row} and Column #{column}\n")
        print(f"{map[0]}\n{map[1]}\n{map[2]}")

map_creation()