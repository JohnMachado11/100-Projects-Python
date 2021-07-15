#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

import time

print("Welcome to Band Name Generator!")

city_name = input("What city did you grow up in? \n")
pet_name = input("What is the name of your pet? \n")

print("Your band name is...")
time.sleep(1)

print(f"{city_name} {pet_name}")