"""
Author: Christine Wei
Date: March 3, 2023,
Description: Rock, Paper, Scissors game
"""
import random


def main():
    """
    Prints menu
    Takes in user input as an integer that corresponds with a play
    Generates a random number from 1 to 3 that corresponds with a play
    Displays winner / loser, unless tie
    If tied, tie-breaker game begins
    """

    # prints menu
    print("Welcome to Rock, Paper, Scissors...!")
    print("=" * 28)
    print("Rock", "1".rjust(23, " "))
    print("Paper", "2".rjust(22, " "))
    print("Scissors", "3".rjust(19, " "))
    print("=" * 28)

    # computer choice/play
    comp_choice = random.randint(1, 3)

    # user choice/play
    while True:
        choice = int(input("What is your play (1, 2, 3)? "))
        if choice == 1 or choice == 2 or choice == 3:
            # checks if there is a tie
            if choice == comp_choice:
                print("Tie. You both chose", choice)
                continue
            # checks if you won
            elif (choice > comp_choice and (choice != 3 and comp_choice != 1)) or (comp_choice == 3 and choice == 1):
                print(f"You win! You chose {choice} and computer chose {comp_choice}")
                break
            # if none of above conditions are met, tells you that you lost
            else:
                print(f"You lost! You chose {choice} and computer chose {comp_choice}")
                break
        else:
            continue

    print("="*27)


main()




