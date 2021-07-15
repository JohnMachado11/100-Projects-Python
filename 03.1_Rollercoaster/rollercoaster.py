print("=============================")
print("WELCOME TO THE ROLLERCOASTER!")
print("=============================")

def height_check():
    try:
        height = int(input("What is your height in cm? "))
    except:
        print("\nPlease respond with a whole number. E.g. 134\n")
        height_check()
    else:
        if height >= 120:
            print("\nYou can ride the rollercoaster.\n")
            age_check()
        elif height < 120: 
            print("\nSorry you have to grow taller.\n")

def age_check():
    try: 
        age = int(input("What is your age? "))
    except:
        print("\nPlease respond with a whole number. E.g. 25\n")
        age_check()
    else:
        total_bill = 0
        if age < 12:
            print("\nChild tickets are $5.\n")
            total_bill += 5
            photograph(total_bill)
        elif age < 18:
            print("\nYouth tickets are $7.\n")
            total_bill += 7
            photograph(total_bill)
        elif age < 45 or age > 55:
            print("\nAdult tickets are $12.\n")
            total_bill += 12
            photograph(total_bill)
        else: 
            print("\nEverything is going to be ok. Have a free ride on us!\n")
            photograph(total_bill)

def photograph(total_bill):
    question = str(input("Want photos? ")).upper()
    if question == "YES":
        total_bill += 3
        print("\nPhotographs are $3.\n")
        print(f"\nThe total bill is ${total_bill}.\n")
    elif question == "NO":
        print(f"\nThe total bill is ${total_bill}.\n")
    else: 
        print("\nPlease respond with Yes or No\n")
        photograph(total_bill)

height_check()