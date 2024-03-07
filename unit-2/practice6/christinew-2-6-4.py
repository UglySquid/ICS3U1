"""
Author: Christine Wei
Date: March 3, 2023,
Description: Magic Guessing Game. I will guess the number you chose.
"""
import random


def main():
    """
    User chooses magic number
    Computer randomly generates a number guess from 1 to 100
    Determines whether number is the magic number
    If number is not magic number, feedback is given by user
    Range from which the computer can randomly generate a number is adapted based on user feedback
    Continues until user guesses the magic number or user has guessed 10 times
    Asks user if they want to play again
    """
    # magic number is chosen by user
    number = int(input("Pick a number from 1 to 100 and I will guess it: "))

    # defines range of guesses from computer
    low_bound = 1
    up_bound = 100

    # start game
    while True:
        # computer guesses number
        guess = random.randint(low_bound, up_bound)

        # prints menu
        print(f"My guess is: {guess}\n")
        print("Am I?")
        print("1. Too low.")
        print("2. Correct!")
        print("3. Too high.\n")

        # asks for user input
        feedback = int(input("Which one: "))

        if feedback == 1:
            # number must be higher than guess so guess because low bound
            low_bound = guess+1
            continue
        if feedback == 3:
            #  number must be lower than guess so guess because high bound
            up_bound = guess-1
            continue
        else:
            print("\nYay! Thank you for playing with me.")
            break


main()
