print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

tip = bill * (percentage / 100)
total_bill = bill + tip
individual_amount = total_bill / people_count
final_amount = round(individual_amount, 2)

print(f"Each person should pay ${final_amount}")
