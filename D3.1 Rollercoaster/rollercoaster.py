print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
total_bill = 0

def photograph():
    question = str(input("Want photos? ")).upper()
    if question == "YES":
        print("Photographs are $3.")
        global total_bill
        total_bill += 3
        print(f"The total bill is ${total_bill}.")
    elif question == "NO":
        print(f"The total bill is ${total_bill}.")
    else: 
        print("Please respond with Yes or No")
        photograph()

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        total_bill += 5
        photograph()
    elif age <= 18:
        print("Youth tickets are $7.")
        total_bill += 7
        photograph()
    else:
        print("Adult tickets are $12.")
        total_bill += 12
        photograph()
else: 
    print("Sorry you have to grow taller.")
