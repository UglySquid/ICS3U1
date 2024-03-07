"""
Author: Christine Wei
Date: March 27, 2023,
Description: Accepts one-word string and returns a word that is a jumble of the letters in the argument
"""
import random


def main():
    """
    Main line, accepts no arguments, jumbles words
    """
    string = input("What would you like to jumble: ")
    string = word_jumble(string)
    print(string)


def word_jumble(string):
    """
    Accepts string input
    Displays jumbled string in random order
    """
    new_string = ""
    for x in string:
        rand_index = random.randint(0, len(string)-1)
        new_string += string[rand_index]

        string = string.replace(string[rand_index], "")

    return new_string


main()
