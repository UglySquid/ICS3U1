"""
Author: Christine Wei
Date: March 30, 2023,
Description: Word Jumble Game
"""

import random


def main():
    """
    Mainline logic
    Accepts no arguments
    Runs word jumble game
    """
    word = find_word()
    jumbled_word = word_jumble(word)

    while True:
        user_guess = input(f"""This is the jumbled word: {jumbled_word}. \nGuess what word it is: """)
        if user_guess == word:
            print("Good job! That's right!")
            break
        else:
            print("Try again!")
            continue


def find_word():
    """
    Finds a random word in textfile
    returns word as string
    accepts no arguments
    """

    word_list = ["word", "another", "computer", "science"]

    chosen_word = word_list[random.randint(0, len(word_list)-1)]

    return chosen_word


def word_jumble(string):
    """
    Accepts string input
    Displays jumbled string in random order
    """
    new_string = ""
    for x in string:
        rand_index = random.randint(0, len(string)-1)
        # adds character at random index to new string
        new_string += string[rand_index]

        # finds one instance of this random character, removes it from the old list
        string = string.replace(string[rand_index], "", 1)

    return new_string


main()
