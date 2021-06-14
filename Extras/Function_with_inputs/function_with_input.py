## Single Input ##

def greet_with_name(name):
     print(f"Hello {name}!")

greet_with_name("David")


## Double Input ##

def greet_with_name_address(name, address):
     print(f"Welcome to {address} {name}!")

greet_with_name_address("John", "125 Epic Drive")


## Keyword arguments ## 

def multiple_arguments(a, b, c):
    print(f"The numbers are {a}, {b}, {c}")

multiple_arguments(b=5, a=1, c=10)