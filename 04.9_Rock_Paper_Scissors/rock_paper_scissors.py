import random

rock = '''        
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_selection = int(input("1 for Rock, 2 for Paper, 3 for Scissors "))
if user_selection == 1:
    print("You Selected Rock\n")
    print(rock)
elif user_selection == 2:
    print("You Selected Paper\n")
    print(paper)
else:
    print("You Selected Scissors\n")
    print(scissors)

computer_selection = random.randint(1,3)
if computer_selection == 1:
    print("Computer Selected Rock\n")
    print(rock)
elif computer_selection == 2:
    print("Computer Selected Paper\n")
    print(paper)
else:
    print("Computer Selected Scissors\n")
    print(scissors)

if user_selection == 1 and computer_selection == 2:
    print("You Lose")
elif user_selection == 1 and computer_selection == 3:
    print("You Win")
elif user_selection == 2 and computer_selection == 1:
    print("You Win")
elif user_selection == 2 and computer_selection == 3:
    print("You Lose")
elif user_selection == 3 and computer_selection == 1:
    print("You Lose")
elif user_selection == 3 and computer_selection == 2:
    print("You Win")
else:
    print("Tie Game")