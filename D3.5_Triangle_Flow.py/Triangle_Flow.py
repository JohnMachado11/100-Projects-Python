# BJJ Triangle Flow 

def triangle_part1():
    response = input("Can you do a triangle? ").upper()
    if response == "NO":
        print("Get back to training!")
    elif response == "YES":
        print("Nice!")
        triangle_part2()
    else:
        print("Please respond with Yes or No")
        triangle_part1()

def triangle_part2():
    response = input("Able to do flying triangles? ").upper()
    if response == "NO":
        print("Get back to training!")
    elif response == "YES":
        print("You're a ninja!")
    else:
        print("Please respond with Yes or No")
        triangle_part2()

triangle_part1()
