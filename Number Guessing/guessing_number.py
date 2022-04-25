""" Number Guessing Game
----------------------------------------
"""

import random

attempts_list = []


def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!\n")
    else:
        print(f"The current high score is {min(attempts_list)} attempts\n")


def game():
    random_number = int(random.randint(1, dic[level]))
    attempts = 0
    while True:
        try:
            number_guess = input(f"Pick a number between 1 and {dic[level]} ")

            if int(number_guess) < 1 or int(number_guess) > dic[level]:
                raise ValueError("Please guess a number within the given range")

            if int(number_guess) == random_number:
                print("Nice! You got it!\n")
                attempts += 1
                attempts_list.append(attempts)
                print(f"It took you {attempts} attempts\n")
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, dic[level]))
                if play_again.lower() == "no" or play_again.lower() == "n":
                    print("That's cool, have a good one!\n")
                    break
            elif int(number_guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(number_guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print(f"Oh no!, that is not a valid value. Try again...\n({err})")


print("Hello ! Welcome to the game of guesses!\n")
level = input("""
pleas chose game level for started
level 1 (default)= guess between 1 and 10 
level 2 = guess between 1 and 100
level 3 = guess between 1 and 1000
»»  """)
dic = {"1": 10, "2": 100, "3": 1000}

if len(level) == 0:
    level = "1"
    game()
else:
    if level in ["1", "2", "3"]:
        game()
    else:
        print("Please guess a number within the given range")
