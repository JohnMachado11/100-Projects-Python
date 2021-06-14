# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello!")
    name = input("Whats your name? ").lower()
    if name.isalpha() != True:
        print("\nERROR: Please only respond with letters.\n")
        greet()
    else:
        print(f"Your name is {name}")
        print("Welcome!")

greet()