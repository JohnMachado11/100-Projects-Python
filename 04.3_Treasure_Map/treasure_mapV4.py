def map_creation():
    row1 = ["O","O","O"]
    row2 = ["O","O","O"]
    row3 = ["O","O","O"]
    map = [row1, row2, row3]
    checkList = [1,2,3]
    print("\n       Col1 Col2 Col3")
    print(f" Row1 {map[0]}\n Row2 {map[1]}\n Row3 {map[2]}")
    map_input(map, checkList)

def map_input(map, checkList):
    try:
        lines = (44 * "-")
        print("\nWhere do you want to put the treasure?\n")
        row = int(input("Select which ROW. Type 1, 2 or 3: "))
        print(f"You selected Row # {row}.\n")
        column = int(input("Select which COLUMN. Type 1, 2 or 3: "))
        print(f"You selected Column # {column}.\n")
    except ValueError:
        print(f"\n{lines}\n ERROR: Please only respond with 1, 2 or 3. \n{lines}\n")
        map_creation()
    else:
        if (row and column) in checkList: 
            map[row - 1][column - 1] = "X"
            print(f"\n{map[0]}\n{map[1]}\n{map[2]}")
        else:
            print(f"\n{lines}\n ERROR: Please only respond with 1, 2 or 3. \n{lines}\n")
            map_creation()
            row = 0
            column = 0

map_creation()