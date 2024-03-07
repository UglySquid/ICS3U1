"""
Author: Christine Wei
Date: March 3, 2023,
Description: Magic Guessing Game
"""
# imports random module
import random


def main():
    """
    Computer chooses magic number
    User guesses number
    Determines whether number is the magic number
    If number is not magic number, feedback is given so that user can guess again
    Continues until user guesses the magic number
    Asks user if they want to play again
    """
    # magic number is chosen
    number = random.randint(1, 1000)
    print("I have a number between 1 and 1000. \nCan you guess my number?")

    # start game
    while True:
        # user guesses number
        guess = int(input("Please type your first guess: "))

        # checks if guess is same as magic number
        if guess == number:
            ask = input("Excellent! You guessed the number! Would you like to play again (y or n)? ")
            if ask == 'y':
                continue
            else:
                break
        # checks if guess is greater than magic number
        elif guess > number:
            print("Too high. Try again")
            continue
        # checks if guess is lower than magic number
        elif number > guess:
            print("Too low. Try again")
            continue


main()
