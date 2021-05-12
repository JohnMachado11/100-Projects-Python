import random
from hangman_art import logo, stages
from hangman_words import word_list
from os import system

#Variables 
cls = lambda: system("cls")
chosen_word = random.choice(word_list)
lives = 6
display = []
list_size = len(chosen_word) * ("_")
display.extend(list_size)
blanks = "_"
game_running = True
tracked_letters = []

print(f"{logo}\n")
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

while game_running:
    guess = input("Guess a letter: ").lower()
    cls()
    print(f"You guessed the letter(s): {guess}\n")
    
    if guess not in tracked_letters:
        tracked_letters.append(guess)
    else:
        print("You've already guessed this letter!\n")
    
    index = 0  
    completed = False

    for letter in chosen_word:
        if guess not in chosen_word and completed == False or len(guess) > 1 and completed == False:
            print(stages[lives])
            lives -= 1
            completed = True
            if lives < 0:
                game_running = False
                print("You Lose!\n")
        if letter == guess:
            display[index] = letter
        if blanks not in display: 
            print("You win!\n")
            game_running = False
            break
        index += 1
    print(f"{' '.join(display)}\n")