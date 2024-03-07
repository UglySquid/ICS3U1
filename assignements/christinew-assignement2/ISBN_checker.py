"""
Author: Christine Wei
Date: March 9, 2023,
Description: Python application that verifies whether 10-digit and 13-digit ISBN (i.e., book) numbers are valid or no
"""

import checkdigits


def main():
    """
    Mainline Logic
    Displays menu
    Checks if ISBN-10 code ir UPC code is valid
    Displays results
    """

    # Input validation so that user can only input 1, 2, 3, Q, or q
    while True:
        # Displays menu
        choice = display_menu()

        # Checks if input is valid

        if check_input(choice):
            # If choice is Q, q, or 3, program ends
            if choice == "q" or choice == "Q" or choice == 3:
                break
            else:
                choice = int(choice)
                # Validates the ISBN-10 code or the UPC code
                validate_code(choice)
            continue
        else:
            # If input is invalid, lets user know their input is invalid and returns to top of while loop
            print("That input is not valid! Try again. \n")
            continue


def display_menu():
    """
    No parameters, accepts no arguments
    Displays menu as string statements
    Returns the choice user chose
    """
    while True:
        # Prints menu.
        print("CHECK DIGIT VALIDATOR", "1. ISBN-10".rjust(30), "\n",
              "2. UPC-12".rjust(50), "\n"
              "What would you like to validate:", "3. Quit Program".rjust(24), "\n")

        # Asks user for choice.
        choice = input("Choice: ".rjust(50))

        return choice


def check_input(input_choice):
    """
    Validates user's choice
    Accepts the argument input_choice as integer
    Returns boolean value True if input is valid
    Returns boolean value False if input is invalid
    """

    # Input is valid if it is 1, 2, 3, Q, or q.
    if input_choice == "1" or input_choice == "2" or input_choice == "3":
        return True

    elif input_choice == "Q" or input_choice == "q":
        return True

    # input is invalid if it is anything else.
    else:
        return False


def validate_code(input_choice):
    """
    Validates ISBN-10 code
    Accepts the integer argument input_choice
    Checks validity of code
    Displays validity of code
    """

    # If choice is 1, it is an ISBN-10 code
    if input_choice == 1:
        # Asks user to input their ISBN code
        while True:
            isbn = int(input("Input your ISBN code: "))
            if 10000000000 > isbn > 999999999:
                break
            else:
                print("That is not a valid ISBN code")
                continue

        # If ISBN code is valid, print valid, else, print invalid
        if checkdigits.is_ISBN10(isbn):
            print("Valid.\n")
        else:
            print("Invalid.\n")

    # If choice is 2, it is a UPC code
    elif input_choice == 2:
        # Asks user to input UPC code
        while True:
            upc = int(input("Input your UPC code: "))
            if 1000000000000 > upc > 99999999999:
                break
            else:
                print("That is not a valid UPC code")
                continue

        # If UPC code is valid, print valid, else, print invalid
        if checkdigits.is_UPC12(upc):
            print("Valid.\n")
        else:
            print("Invalid.\n")
    else:
        print("Invalid.\n")


main()
