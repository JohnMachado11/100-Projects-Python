#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

tip_total = bill * (percentage / 100)
total_bill = bill + tip_total
individual_tip = total_bill / people_count
final_amount = round(individual_tip, 2)

print(f"Each person should pay ${final_amount}")